# proglang-project

This project contains a spaCy project to detect programming languages. We compare
spaCy NER models and a pattern matcher model. 

## Data Chain 

The project is set up to move datafiles along. 

```
raw-data -> unlabelled -> assets -> corpus 
```

1. The `raw-data` folder contains the pure raw data. 
2. The `unlabelled` folder contains a subset of the columns. 
3. The `assets` folder contains `.jsonl` files that represent training data. 
4. The `corpus` folder contains `.spacy` files, optimized for training.

## Labelling 

```
prodigy ner.manual proglang blank:en unlabelled/bq-spacy-2015-01.jsonl --label PROGLANG --patterns ./configs/proglang_patterns.jsonl
```
## Installation 

```
pip install prodigy.whl
```

## prodigy 

Not *right* now, but later we'll want to add prodigy. 

```
cat assets/stack-overflow-labels-train.jsonl > assets/labelled.jsonl
prodigy db-out proglang >> assets/labelled.jsonl
```
