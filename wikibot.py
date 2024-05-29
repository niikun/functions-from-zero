import wikipedia
# import ipython
import click


def scrape(word="Micorsoft",length=1):
    result = wikipedia.summary(word,sentences=length)
    return result

@click.command()
@click.argument('word')
def main(word):
    print(scrape(word))

if __name__ == "__main__":
    main()

# import requests
# from bs4 import BeautifulSoup

# TARGET_URL = "https://en.wikipedia.org/wiki/OpenAI"

# res = requests.get(TARGET_URL)
# soup = BeautifulSoup(res.text,"html.parser")

# print(soup.text)