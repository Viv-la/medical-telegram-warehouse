from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI(title="Medical Telegram Warehouse API")


@app.get("/")
def home():
    return {
        "message": "Medical Telegram Warehouse API is running."
    }


@app.get("/messages/{channel}")
def get_messages(channel: str):

    data_folder = Path("data/raw/telegram_messages")

    json_files = list(data_folder.rglob(f"{channel}.json"))

    if not json_files:
        return {"error": "Channel not found"}

    with open(json_files[0], "r", encoding="utf-8") as file:
        return json.load(file)