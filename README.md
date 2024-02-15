# tool-make-aligned-dataset
This repository provides a Python script for creating a dataset of aligned sequences
from a dataset with unaligned sequences. Alignment is performed using [mafft](https://mafft.cbrc.jp/alignment/software/).

NOTE: **Apple Silicon e.g. M1 is not supported**

## Prerequisites

1. Install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Miniconda is recommeded.

## Instructions

1. Create a conda environment with the necessary dependencies

    ```
    conda env create -n tool-make-aligned-dataset -f environment.yml
    ```

1. Activate the conda environment

    ```
    conda activate tool-make-aligned-dataset
    ```

1. Run the `make_aligned_dataset.py` script on your dataset:

    ```
    python make_aligned_dataset.py \
        --dataset <path-to-dataset> \
        --sequence_column_name <name-of-column-with-sequences>
    ```

  The dataset must be in csv format. Remember to replace the values in angle brackets <>!

  The script will output a file with the aligned dataset and the name of the file will
  be the name of the input file with `_aligned` appended to it. The file will be
  located in the same directory as the input file.
