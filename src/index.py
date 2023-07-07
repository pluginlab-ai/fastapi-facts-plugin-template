from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import random
import json
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Install your plugin on ChatGPT and ask for a fact."}


@app.get("/fact")
async def get_random_fact():
    current_path = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_path, './data', 'facts.json')

    with open(json_file_path) as f:
        facts = json.load(f)
    random_fact = random.choice(facts)
    response = { "fact": random_fact }
    return JSONResponse(content=response)

