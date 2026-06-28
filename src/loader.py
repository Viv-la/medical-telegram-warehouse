import json
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/medical_warehouse"
)

engine = create_engine(DATABASE_URL)


def load_json_to_postgres():
    json_files = Path("data/raw/telegram_messages").rglob("*.json")
    records = []

    for file_path in json_files:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            records.extend(data)

    df = pd.DataFrame(records)

    if df.empty:
        print("No records found.")
        return

    df.to_sql(
        "telegram_messages",
        engine,
        schema="raw",
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} records into raw.telegram_messages")


if __name__ == "__main__":
    load_json_to_postgres()