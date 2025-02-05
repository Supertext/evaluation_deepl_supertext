from pathlib import Path

import polars as pl


class ABResult:
    def __init__(self, filename: Path):
        self.filename = filename
        self.df = self._parse_data()

    def _parse_data(self) -> pl.DataFrame:
        df = pl.read_csv(self.filename)
        # remove paragraph boundary rows
        df = df.filter(df["source"].is_not_null())

        # compute winner system based on segment ratings (A / B / equal)
        df = df.with_columns(
            pl.when(pl.col("A"))
            .then(pl.col("label_A"))
            .when(pl.col("B"))
            .then(pl.col("label_B"))
            .when(pl.col("equal"))
            .then(pl.lit("equal"))
            .alias("winner")
        )

        return df

    @staticmethod
    def _write_results(df: pl.DataFrame, outfile: Path) -> None:
        df.write_csv(f"{outfile}_winner.tsv", separator="\t")

    def analyze_by_segment(self, outfile: Path) -> None:
        # compute which system won how many times
        df_wins = self.df.group_by("winner").agg(pl.count("winner").alias("count"))
        self._write_results(df_wins, outfile)

    @staticmethod
    def _get_results_by_text(df: pl.DataFrame, column_name: str) -> pl.DataFrame:
        # compute which system won how many times per text
        df = df.group_by(["text", column_name]).agg(pl.count(column_name).alias("count"))
        # rearrange winning systems as columns
        df = df.pivot(column_name, index="text", values="count")
        # use 0 for missing values
        df = df.fill_null(strategy="zero")
        # determine the winner per document
        df = df.with_columns(
            pl.when(pl.col("DeepL") > pl.col("Supertext"))
            .then(pl.lit("DeepL"))
            .when(pl.col("DeepL") < pl.col("Supertext"))
            .then(pl.lit("Supertext"))
            .otherwise(pl.lit("equal"))
            .alias("winner_by_document")
        )

        return df

    def analyze_by_document(self, outfile: Path) -> None:
        # compute which system won how many times per text
        df_wins = self._get_results_by_text(self.df, "winner")

        # compute how many times each system won
        df_wins = df_wins.group_by("winner_by_document").agg(
            pl.count("winner_by_document").alias("count")
        )
        self._write_results(df_wins, outfile)
