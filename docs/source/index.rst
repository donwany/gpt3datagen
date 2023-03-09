.. gpt3datagen documentation master file, created by
   sphinx-quickstart on Sat Feb 25 14:18:14 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to gpt3datagen’s documentation!
=======================================
GPT3DataGen is a python package that generates fake data for fine-tuning your openai models.

Installation
============

Pip
---
Install via pip

.. code-block:: bash

    pip install -U gpt3datagen

Alternatively, the following command will pull and install the latest commit
from this repository, along with its Python dependencies:

.. code-block:: bash

   pip install git+https://github.com/donwany/gpt3datagen.git --use-pep517


Or git clone repository:

.. code-block:: bash

    git clone https://github.com/donwany/gpt3datagen.git
    cd gpt3datagen
    make install && pip install -e .


Command-Line Usage
==================
Run the following to view all available options:

.. code-block:: bash

   gpt3datagen --help
   gpt3datagen --version

Output formats: `jsonl`, `json`, `csv`, `tsv`, `xlsx`

.. code-block::

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

Data Format
===========
.. code-block:: bash

   {"prompt": "<prompt text> \n\n###\n\n", "completion": " <ideal generated text> END"}
   {"prompt": "<prompt text> \n\n###\n\n", "completion": " <ideal generated text> END"}
   {"prompt": "<prompt text> \n\n###\n\n", "completion": " <ideal generated text> END"}
                                       ...

Basic Usage
===========
Only useful if you clone the repository

.. code-block:: python

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




Validate Sample Data
====================

.. code-block:: bash

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

Test Runs
=========
.. code-block::

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


Source Code
===========

The library is maintained on GitHub. Feel free to clone the repository.

.. code-block:: bash

    git clone https://github.com/donwany/gpt3datagen.git

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

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
