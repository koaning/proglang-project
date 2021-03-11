from pathlib import Path

import typer
from clumper import Clumper
from rich.table import Table
from rich.console import Console
from spacy.lang.en import English

def cast_item(item):
    if isinstance(item, float):
        item = round(item, 4)
    return str(item)

def print_rich_table(clump, n_row=None, cols=None, title=None, rounding=5):    
    c = Console()
    t = Table()
    if cols:
        clump = clump.select(*cols)
    data = clump.collect()
    
    table = Table(title=title)
    for name in data[0].keys():
        table.add_column(name, style="cyan")

    for d in data:
        vals = [cast_item(_) for _ in d.values()]
        table.add_row(*vals)

    console = Console()
    console.print(table)


def main():
    (Clumper
     .read_json("training/*-metrics.json", add_path=True)
     .mutate(read_path=lambda d: d['read_path'].replace("training/", ""),
             speed=lambda d: int(d['speed']))
     .drop("ents_per_type")
     .select("read_path", "speed", "ents_p", "ents_r", "ents_f")
     .pipe(print_rich_table))

if __name__ == "__main__":
    typer.run(main)
