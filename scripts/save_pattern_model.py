from pathlib import Path

import typer
from clumper import Clumper
from spacy.lang.en import English


def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(..., dir_okay=True),
):
    patterns = Clumper.read_jsonl(input_path).collect()
    nlp = English()
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns)
    nlp.to_disk(output_path)
    print(f"Rule-Based model saved at {output_path}.")


if __name__ == "__main__":
    typer.run(main)
