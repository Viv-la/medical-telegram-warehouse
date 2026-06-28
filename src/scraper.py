import os
import json
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
from telethon import TelegramClient
from config import CHANNELS, MESSAGE_LIMIT

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

client = TelegramClient("telegram_session", API_ID, API_HASH)


async def scrape_channel(channel_name):
    print(f"\nReading messages from {channel_name}...")

    messages = []

    async for message in client.iter_messages(channel_name, limit=MESSAGE_LIMIT):
        image_path = None

        if message.photo:
            image_dir = Path(f"data/raw/images/{channel_name}")
            image_dir.mkdir(parents=True, exist_ok=True)

            image_path = image_dir / f"{message.id}.jpg"
            await message.download_media(file=image_path)

        messages.append({
            "message_id": message.id,
            "channel_name": channel_name,
            "message_date": str(message.date),
            "message_text": message.text,
            "has_media": message.media is not None,
            "image_path": str(image_path) if image_path else None,
            "views": message.views,
            "forwards": message.forwards
        })

    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = Path(f"data/raw/telegram_messages/{today}")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{channel_name}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4, ensure_ascii=False)

    print(f"Saved {len(messages)} messages to {output_file}")


async def main():
    print("Connecting to Telegram...")
    await client.start(phone=PHONE_NUMBER)

    me = await client.get_me()
    print(f"Connected successfully as: {me.first_name}")

    for channel in CHANNELS:
        try:
            await scrape_channel(channel)
        except Exception as e:
            print(f"Failed to scrape {channel}: {e}")


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())