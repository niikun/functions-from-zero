#!/usr/bin/env python3

import wikipedia
import click

def scrape(word="Microsoft", length=1):
    result = wikipedia.summary(word, sentences=length)
    return result

@click.command()
@click.option("--word", prompt="Enter the word to search", help="The word to search on Wikipedia", default="Microsoft")
def main(word):
    print(scrape(word))

if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter