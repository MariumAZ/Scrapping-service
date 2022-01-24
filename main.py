
from fastapi import FastAPI
from scraper import Scraper
app = FastAPI()

#create instance of Scraper 
scrape = Scraper()

@app.get("/{category}")
async def read_item(category):
    return scrape.scrapdata(category)


