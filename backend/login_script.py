"""
CREATE SESSION FOR BOT  &  JOIN GROUPS
"""
import json
import typer
import asyncio
from telethon.sync import TelegramClient
from telethon.tl import functions


app = typer.Typer()

# GROUPS
client_group_id = "LuchaT8Community"
groups = [
    client_group_id,
    "scienceQuiz",
]


async def write_bot(bot_credentials):
  # Write the bot credentials to JSON file
    try:
        json_file_path = f"{bot_credentials['session_name']}.json"
        with open(json_file_path, 'w') as json_file:
            json.dump(bot_credentials, json_file)
    except Exception as e:
        return False
    return True


async def main(
    phone: str,
    api_id: int,
    api_hash: str
):
    bot_credentials = {
        "session_name": phone.replace(" ", ''),
        "api_id": api_id,
        "api_hash": api_hash,
        "phone_number": phone,
    }

    if not await write_bot(bot_credentials):
        print("JSON fail")

    async with TelegramClient(
        bot_credentials["session_name"], bot_credentials["api_id"], bot_credentials["api_hash"]
    ) as client:
        # Add BOT to groups
        for group in groups:
            try:
                await client(functions.channels.JoinChannelRequest(
                    channel=group
                ))
                print(f"Added to {group}")
            except Exception as e:
                print(e)
                print("Continue to add...")


def run_main(
    phone: str = typer.Option(..., "--phone", help="Phone number"),
    api_id: int = typer.Option(..., "--id", help="Api ID"),
    api_hash: str = typer.Option(..., "--hash", help="Api Hash")
):
    asyncio.run(main(phone, api_id, api_hash))


if __name__ == "__main__":
    app.command()(run_main)
    app()