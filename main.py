from typing import Final
import os
import keyboard
from dotenv import load_dotenv
from discord import Intents, Client


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
SESSION: Final[int] = int(os.getenv('SESSION')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message() -> None:
    try:
        channel = client.get_channel(SESSION)
        if channel:
            response = "hello there how are you!"
            await channel.send(response)
        else:
            print("channel not found")
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    print("bot is ready!")

    def on_space_press():
        client.loop.create_task(send_message())

    keyboard.on_release_key("space", lambda _: on_space_press())
    await send_message()

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()
