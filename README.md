[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![CI](https://github.com/donwany/gpt3datagen/actions/workflows/CI.yml/badge.svg)](https://github.com/donwany/gpt3datagen/actions/workflows/CI.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## GPT3DataGen
GPT3DataGen is a python package that generates fake data for fine-tuning your `openai` models.
```markdown
               _      ___      _         _
              ( )_  /'_  )    ( )       ( )_
   __   _ _   | ,_)(_)_) |   _| |   _ _ | ,_)   _ _    __     __    ___
 /'_ `\( '_`\ | |   _(_ <  /'_` | /'_` )| |   /'_` ) /'_ `\ /'__`\/' _ `\
( (_) || (_) )| |_ ( )_) |( (_| |( (_| || |_ ( (_| |( (_) |(  ___/| ( ) |
`\__  || ,__/'`\__)`\____)`\__,_)`\__,_)`\__)`\__,_)`\__  |`\____)(_) (_)v1.0.3
( )_) || |                                          ( )_) |
 \___/'(_)                                           \___/'


```

### Install with pip. See [Install & Usage Guide](https://pypi.org/project/gpt3datagen/)
```shell
pip install -U gpt3datagen
```
Alternatively, the following command will pull and install the latest commit
from this repository, along with its Python dependencies:
```shell
pip install git+https://github.com/donwany/gpt3datagen.git --use-pep517
```
Or git clone repository:
```shell
git clone https://github.com/donwany/gpt3datagen.git
cd gpt3datagen
make install && pip install -e .
```

To update the package to the latest version of this repository, please run:
```shell
pip install --upgrade --no-deps --force-reinstall git+https://github.com/donwany/gpt3datagen.git
```

### Command-Line Usage
Run the following to view all available options:
```shell
gpt3datagen --help
gpt3datagen --version
```
Output formats: `jsonl`, `json`, `csv`, `tsv`, `xlsx`
```shell
gpt3datagen \
    --num_samples 500 \
    --max_length 2048 \
    --sample_type "classification" \
    --output_format "jsonl" \
    --output_dir .

gpt3datagen \
    --num_samples 500 \
    --max_length 2048 \
    --sample_type completion \
    --output_format csv \
    --output_dir .

gpt3datagen \
    --sample_type completion \
    --output_format jsonl \
    --output_dir .

gpt3datagen --sample_type completion -o . -f jsonl
gpt3datagen --sample_type news -o . -f jsonl
```
### Data Format
```shell
{"prompt": "<prompt text> \n\n###\n\n", "completion": " <ideal generated text> END"}
{"prompt": "<prompt text> \n\n###\n\n", "completion": " <ideal generated text> END"}
{"prompt": "<prompt text> \n\n###\n\n", "completion": " <ideal generated text> END"}
                                    ...
```
### Basic Usage
Only useful if you clone the repository
```shell
python prepare.py \
    --num_samples 500 \
    --max_length 2048 \
    --sample_type "classification" \
    --output_format "jsonl" \
    --output_dir .

python prepare.py \
    --num_samples 500 \
    --max_length 2048 \
    --sample_type "completion" \
    --output_format "csv" \
    --output_dir .

python prepare.py \
    --num_samples 500 \
    --max_length 2048 \
    --sample_type "completion" \
    --output_format "json" \
    --output_dir /Users/<tsiameh>/Desktop
```
### Validate Sample Data
```shell
pip install --upgrade openai

export OPENAI_API_KEY="<OPENAI_API_KEY>"

# validate sample datasets generated
openai tools fine_tunes.prepare_data -f <SAMPLE_DATA>.jsonl
openai tools fine_tunes.prepare_data -f <SAMPLE_DATA>.csv
openai tools fine_tunes.prepare_data -f <SAMPLE_DATA>.tsv
openai tools fine_tunes.prepare_data -f <SAMPLE_DATA>.json
openai tools fine_tunes.prepare_data -f <SAMPLE_DATA>.xlsx
openai tools fine_tunes.prepare_data -f /Users/<tsiameh>/Desktop/data_prepared.jsonl

# fine-tune
openai api fine_tunes.create \
  -t <DATA_PREPARED>.jsonl \
  -m <BASE_MODEL: davinci, curie, ada, babbage>

# List all created fine-tunes
openai api fine_tunes.list
```

### Test Runs
```shell
# For multiclass classification
openai api fine_tunes.create \
  -t <TRAIN_FILE_ID_OR_PATH> \
  -v <VALIDATION_FILE_OR_PATH> \
  -m <MODEL> \
  --compute_classification_metrics \
  --classification_n_classes <N_CLASSES>

# For binary classification
openai api fine_tunes.create \
  -t <TRAIN_FILE_ID_OR_PATH> \
  -v <VALIDATION_FILE_OR_PATH> \
  -m <MODEL> \
  --compute_classification_metrics \
  --classification_n_classes 2 \
  --classification_positive_class <POSITIVE_CLASS_FROM_DATASET>
```

Contribute
----------
Please see [CONTRIBUTING](https://github.com/donwany/gpt3datagen/blob/main/CONTRIBUTING.rst).

License
-------
GPT3DataGen is released under the MIT License. See the bundled [LICENSE](https://github.com/donwany/gpt3datagen/blob/main/LICENCE.txt) file
for details.

Credits
-------
-  `Theophilus Siameh`
