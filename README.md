# Detecting Programming Languages

This project contains a spaCy project to detect programming languages. We compare spaCy NER models and a pattern matcher model. 

You can find a youtube series on these models on [this playlist](). The first 5 videos are made using spaCy 2.3, if you're interested in learning more about this project structure it'd be better to start watching [here](). 

<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Detecting Programming Languages in Stackoverflow and Reddit (Named Entity Recognition)

This project attempts to detect programming languages.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Convert the data to spaCy's binary format |
| `patternmod` | Generate a named entity recognition model based on rules. |
| `train` | Train a named entity recognition model |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `show-stats` | Show the statistics that compares both models. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `patternmod` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/stackoverflow-train.jsonl`](assets/stackoverflow-train.jsonl) | Local | JSONL-formatted training data |
| [`assets/stackoverflow-valid.jsonl`](assets/stackoverflow-valid.jsonl) | Local | JSONL-formatted validation data |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->