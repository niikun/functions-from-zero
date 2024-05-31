#!/usr/bin/env python3

import wikipedia
import click
from mylib.bot import scrape


@click.command()
@click.option("--word", prompt="Enter the word to search", help="The word to search on Wikipedia", default="Microsoft")
def cli(word="Microsoft",length=1):
    result = scrape(word, length)
    click.echo(result)

if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter