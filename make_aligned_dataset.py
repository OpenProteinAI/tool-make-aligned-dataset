import argparse
import logging
import subprocess
from pathlib import Path
from tempfile import NamedTemporaryFile

import pandas as pd


def parse_stream(f, comment=b"#", upper=True):
    name = None
    sequence = []
    for line in f:
        if line.startswith(comment):
            continue
        line = line.strip()
        if line.startswith(b">"):
            if name is not None:
                yield name, b"".join(sequence)
            name = line[1:]
            sequence = []
        else:
            if upper:
                sequence.append(line.upper())
            else:
                sequence.append(line)
    if name is not None:
        yield name, b"".join(sequence)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, default="example_dataset.csv")
    parser.add_argument("--sequence_column_name", type=str, default="sequence")
    args = parser.parse_args()

    # read input
    path = Path(args.dataset_path)
    if path.suffix != ".csv":
        logging.warning("This script only accepts csvs, but the file extension is not csv. Proceeding anyways...")
    output_path = path.with_stem(path.stem + "_aligned")
    if output_path.exists():
        raise Exception(f"Output path {output_path} already exists! Exiting to avoid overwriting...")

    # align
    df = pd.read_csv(path)
    if args.sequence_column_name not in df.columns:
        raise ValueError(f"Sequence column {args.sequence_column_name} not found in input file.")
    sequences = df[args.sequence_column_name]
    with NamedTemporaryFile() as fp:
        for idx, sequence in enumerate(sequences):
            fp.write(f">{idx}\n".encode())
            fp.write(f"{sequence}\n".encode())
        fp.flush()
        result = subprocess.run(
            [
                "mafft",
                "--auto",
                fp.name,
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            logging.error(f"Alignment error: {result.stderr}")
        aligned_sequences = []
        for _, sequence in parse_stream(result.stdout.encode().split(b"\n"), upper=False):
            aligned_sequences.append(sequence.decode())
        df[args.sequence_column_name] = aligned_sequences

    # write output
    df.to_csv(output_path, index=False)
    print(f"Success! Aligned dataset written to {output_path}")


if __name__ == "__main__":
    main()
