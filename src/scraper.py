import os
from dotenv import load_dotenv
from telethon import TelegramClient

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
    channel = "CheMed123"

    print(f"\nReading messages from {channel}...\n")

    async for message in client.iter_messages(channel, limit=5):
        print("-" * 60)
        print(f"Message ID : {message.id}")
        print(f"Date       : {message.date}")
        print(f"Views      : {message.views}")
        print(f"Forwards   : {message.forwards}")
        print(f"Text:\n{message.text}")


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())