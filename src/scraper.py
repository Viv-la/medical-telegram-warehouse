import os
import json
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient
from config import CHANNELS, MESSAGE_LIMIT

# Load environment variables
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

# Create Telegram client
client = TelegramClient("telegram_session", API_ID, API_HASH)


async def main():
    print("Connecting to Telegram...")

    await client.start(phone=PHONE_NUMBER)

    me = await client.get_me()
    print(f"Connected successfully as: {me.first_name}")

    # ONE channel only for now
    channel = CHANNELS[0]

    print(f"\nReading messages from {channel}...\n")

    messages = []

    async for message in client.iter_messages(channel, limit=MESSAGE_LIMIT):
        messages.append({
            "message_id": message.id,
            "channel_name": channel,
            "date": str(message.date),
            "text": message.text,
            "has_media": message.media is not None,
            "views": message.views,
            "forwards": message.forwards
        })

    output_dir = Path("data/raw/telegram_messages")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{channel}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4, ensure_ascii=False)

    print(f"Saved {len(messages)} messages to {output_file}")


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())