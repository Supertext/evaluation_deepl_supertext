# A/B Test Supertext vs DeepL

We release all evaluation data and scripts for further analysis and reproduction of the accompanying paper: [A comparison of translation performance between DeepL and Supertext](https://arxiv.org/abs/2502.02577).


### Installation
```bash
pip install poetry
poetry install
```

### A/B Test Evaluation

To evaluate A/B results, call the script as follows:

```bash
    python analysis/analyze.py -i data/ab_LANGPAIR.csv
```

You will find two TSVs with results in the `results` folder:

- FILENAME_by_segment_winner: Aggregated results of segment wins by system
- FILENAME_by_document_winner: Aggregated results of document wins by system

### Citation

If you use our code or data, please cite our [paper](https://arxiv.org/abs/2502.02577):

    @misc{flueckiger-etal-2025-comparison,
        title = "A comparison of translation performance between DeepL and Supertext",
        author = {Flückiger, Alex  and
        Amrhein, Chantal  and
        Graf, Tim and
        Schläpfer, Philippe and
        Schottmann, Florian  and
        Läubli, Samuel},
        year={2025},
        eprint={2502.02577},
        archivePrefix={arXiv},
        primaryClass={cs.CL},
        url={https://arxiv.org/abs/2502.02577}, 
    }
