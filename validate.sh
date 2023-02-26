#!/bin/bash

pip install --upgrade openai

export OPENAI_API_KEY="<OPENAI_API_KEY>"

openai tools fine_tunes.prepare_data -f <SAMPLE_DATA>.jsonl