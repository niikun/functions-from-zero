from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
from mylib.bot import scrape
from pydantic import BaseModel

app = FastAPI()

class Wiki(BaseModel):
    word: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/word/{word}")
def scrape_word(word: str):
    scraped = scrape(word)
    return {"word": word, "ans": scraped}

@app.post("/wiki")
async def scrape_story(wiki: Wiki):
    result = scrape(word=wiki.word)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
