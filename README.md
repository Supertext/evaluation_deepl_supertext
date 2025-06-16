# A/B Test Supertext vs DeepL

We release all evaluation data and scripts for further analysis and reproduction of the accompanying paper: [A comparison of translation performance between DeepL and Supertext](https://arxiv.org/abs/2502.02577).

The dataset is available on Hugging Face as well: https://huggingface.co/datasets/Supertext/mt-doclevel-ab-test


### Installation
```bash
pip install poetry
poetry install
```

### A/B Test Evaluation

To evaluate A/B results, call the script as follows:

```bash
poetry run python analysis/analyze.py -i data/ab_LANGPAIR.csv
```

You will find two TSVs with results in the `results` folder:

- FILENAME_by_segment_winner: Aggregated results of segment wins by system
- FILENAME_by_document_winner: Aggregated results of document wins by system

### Citation

If you use our code or data, please cite our [paper](https://arxiv.org/abs/2502.02577):

    @misc{flueckiger-etal-2025-comparison,
        title={A comparison of translation performance between DeepL and Supertext}, 
        author={Alex Flückiger and Chantal Amrhein and Tim Graf and Frédéric Odermatt and Martin Pömsl and Philippe Schläpfer and Florian Schottmann and Samuel Läubli},
        year={2025},
        eprint={2502.02577},
        archivePrefix={arXiv},
        primaryClass={cs.CL},
        url={https://arxiv.org/abs/2502.02577}, 
    }
