import argparse
import csv
import json
import os

import pandas as pd

from . import VERSION


class SaveFile:
    @staticmethod
    def mkdir(path):
        """Create directory"""
        try:
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print(f" * Directory %s already exists = {path}")
        except OSError as err:
            raise OSError(f"{err}")

    @staticmethod
    def save_jsonl(file_name="data_sample", data=None, output_dir=None):
        # Save the samples to a .jsonl file
        print("Saving results to jsonl...")
        if output_dir is None:
            output_dir = os.getcwd()
            # make a directory at the current working directory
            SaveFile.mkdir(output_dir)
        print(f"File will be save to: {output_dir}")
        with open(f"{output_dir}/{file_name}.jsonl", "w") as f:
            for sample in data:
                f.write(json.dumps(sample) + "\n")
        print(f"{output_dir}/{file_name}.jsonl saved!")

    @staticmethod
    def save_csv(file_name="data_sample", data=None, output_dir=None):
        # Save the samples to a .csv file
        print("Saving results to csv...")
        if output_dir is None:
            output_dir = os.getcwd()
            # make a directory at the current working directory
            SaveFile.mkdir(output_dir)
        print(f"File will be save to: {output_dir}")
        fieldnames = ["prompt", "completion"]
        with open(f"{output_dir}/{file_name}.csv", mode="w", newline="") as file:
            df = pd.DataFrame(data, columns=fieldnames)
            df.to_csv(file, index=False)
        print(f"{output_dir}/{file_name}.csv saved!")

    @staticmethod
    def save_tsv(file_name="data_sample", data=None, output_dir=None):
        # Save the samples to a .tsv file
        print("Saving results to tsv...")
        if output_dir is None:
            output_dir = os.getcwd()
            # make a directory at the current working directory
            SaveFile.mkdir(output_dir)
        print(f"File will be save to: {output_dir}")
        with open(f"{output_dir}/{file_name}.tsv", mode="w", newline="") as file:
            fieldnames = ["prompt", "completion"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            for sample in data:
                writer.writerow(sample)
        print(f"{output_dir}/{file_name}.tsv saved!")

    @staticmethod
    def save_xlsx(file_name="data_sample", data=None, output_dir=None):
        # Save the samples to an .xlsx file
        print("Saving results to xlsx...")
        if output_dir is None:
            output_dir = os.getcwd()
            # make a directory at the current working directory
            SaveFile.mkdir(output_dir)
        print(f"File will be save to: {output_dir}")
        df = pd.DataFrame(data)
        df.to_excel(f"{output_dir}/{file_name}.xlsx", index=False)
        print(f"{output_dir}/{file_name}.xlsx saved!")

    @staticmethod
    def save_json(file_name="data_sample", data=None, output_dir=None):
        # Save the samples to a .json file
        print("Saving results to json...")
        if output_dir is None:
            output_dir = os.getcwd()
            # make a directory at the current working directory
            SaveFile.mkdir(output_dir)
        print(f"File will be save to: {output_dir}")
        with open(f"{output_dir}/{file_name}.json", "w") as f:
            for sample in data:
                f.write(json.dumps(sample) + "\n")
        print(f"{output_dir}/{file_name}.json saved!")


def argParser():
    parser = argparse.ArgumentParser(description="Fine-Tune GPT3 Data Generator")

    parser.add_argument(
        "--num_samples",
        type=int,
        default=500,
        help="Number of samples to generate",
    )
    parser.add_argument(
        "--max_length",
        type=int,
        default=2048,
        help="Maximum tokens (prompt + completion)",
    )
    parser.add_argument(
        "--sample_type",
        type=str,
        default="completion",
        choices=["completion", "classification", "news"],
        help="Type of datasets (Classification, Completion, News Article)",
    )
    parser.add_argument("--version", action="version", version=f"{VERSION}")
    parser.add_argument(
        "--output_dir",
        "-o",
        type=str,
        default=".",
        help="Directory to save the outputs",
    )
    parser.add_argument(
        "--output_format",
        "-f",
        type=str,
        default="jsonl",
        choices=["jsonl", "json", "csv", "tsv", "xlsx"],
        help="format of the output file; if not specified,jsonl formats will be produced",
    )

    return parser.parse_args()
