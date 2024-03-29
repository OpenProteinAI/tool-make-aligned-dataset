# tool-make-aligned-dataset
This repository provides a Python script for creating a dataset with aligned sequences
from a dataset with unaligned sequences. Alignment is performed using [mafft](https://mafft.cbrc.jp/alignment/software/).

## Prerequisites

1. Install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) or [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html). If using `mamba`, replace instances of `conda` below with `mamba`.

## Instructions

1. Create a conda environment with the necessary dependencies.

    a. If you are using Linux or a non-Apple Silicon based Mac, run

    ```
    conda env create -n tool-make-aligned-dataset -f environment.yml
    ```

    Proceed to Step 2.

    b. Otherwise (e.g. using Windows without WSL or an Apple Silicon based Mac), run

    ```
    conda env create -n tool-make-aligned-dataset -f environment-no-mafft.yml
    ```

    Next, install `mafft`. For Apple Silicon, you can simply run `brew install mafft`. For Windows, follow the [instructions on the mafft website](https://mafft.cbrc.jp/alignment/software/windows.html).

    Proceed to Step 2.

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


## Example

1. The file `example_dataset.csv` contains an example dataset of unaligned sequences
   (the data is made up). The name of the column containing sequences is `sequence`,
   and the dataset contains three sequences and measurements for three properties. We
   run the following command to create an aligned version of this dataset:

   ```
    python make_aligned_dataset.py \
        --dataset example_dataset.csv \
        --sequence_column_name sequence
   ```

1. This should create a file called `example_dataset_aligned.csv` which contains the
   aligned dataset i.e. everything the same as the original dataset file except that
   the sequences in the sequence column are now aligned sequences.
