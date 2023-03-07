from typing import Any, Dict, List
import numpy as np
from .datasets import classification, condition_generation, news_articles
from .utils import SaveFile, argParser


def generate_samples(
    num_samples: int, max_length: int, sample_type: str
) -> List[Dict[str, Any]]:
    """Generate `num_samples` samples of type
    `sample_type` with a maximum length of `max_length` tokens"""
    samples = []
    if sample_type == "completion":
        prompts, completions = (
            condition_generation.prompts,
            condition_generation.completions,
        )
    elif sample_type == "classification":
        prompts, completions = classification.prompts, classification.completions
    elif sample_type == "news":
        prompts, completions = news_articles.prompts, news_articles.completions
    for i in range(num_samples):
        # Randomly choose a prompt and completion
        prompt, completion = np.random.choice(prompts, replace=False), np.random.choice(
            completions, replace=False
        )
        # Calculate the maximum token length of the prompt and completion
        max_prompt_length = (
            max_length - len(completion) - 5
        )  # "-5" for "\n\n###\n\n" separator
        prompt = prompt[:max_prompt_length]
        # Append the sample to the list of samples
        samples.append({"prompt": prompt, "completion": f" {completion}"})
    return samples


def cli():
    # parse input arguments
    args = argParser()
    # Define the maximum token length of the prompt and completion
    MAX_LENGTH = args.max_length
    # number of samples to generate
    num_samples = args.num_samples
    # type of datasets to generate
    sample_type = args.sample_type
    # file type
    file_type = args.output_format
    # where to save file
    output_dir = args.output_dir

    if file_type == "jsonl":
        sample = generate_samples(
            num_samples=num_samples, sample_type=sample_type, max_length=MAX_LENGTH
        )
        SaveFile.save_jsonl(data=sample, output_dir=output_dir)
    elif file_type == "csv":
        sample = generate_samples(
            num_samples=num_samples, sample_type=sample_type, max_length=MAX_LENGTH
        )
        SaveFile.save_csv(data=sample, output_dir=output_dir)
    elif file_type == "tsv":
        sample = generate_samples(
            num_samples=num_samples, sample_type=sample_type, max_length=MAX_LENGTH
        )
        SaveFile.save_tsv(data=sample, output_dir=output_dir)
    elif file_type == "json":
        sample = generate_samples(
            num_samples=num_samples, sample_type=sample_type, max_length=MAX_LENGTH
        )
        SaveFile.save_json(data=sample, output_dir=output_dir)
    elif file_type == "xlsx":
        sample = generate_samples(
            num_samples=num_samples, sample_type=sample_type, max_length=MAX_LENGTH
        )
        SaveFile.save_xlsx(data=sample, output_dir=output_dir)


if __name__ == "__main__":
    cli()
