import wikipedia
import click

def scrape(word="Microsoft", length=1):
    result = wikipedia.summary(word, sentences=length)
    return result

@click.command()
@click.argument("word")
def main(word):
    print(scrape(word))

if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter