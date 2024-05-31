import wikipedia

def scrape(word="Microsoft", length=1):
    result = wikipedia.summary(word, sentences=length)
    return result