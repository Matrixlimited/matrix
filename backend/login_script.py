"""
CREATE SESSION FOR BOT  &  JOIN GROUPS
"""
import json
import typer
import asyncio
import logging
import os
import re
from telethon.sync import TelegramClient
from telethon.tl import functions
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


app = typer.Typer()

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

offset_range = 150
all_participants = []

async def write_bot(bot_credentials):
  # Write the bot credentials to JSON file
    try:
        json_file_path = f"data/{bot_credentials['session_name']}.json"
        with open(json_file_path, 'w') as json_file:
            json.dump(bot_credentials, json_file)
    except Exception as e:
        return False
    return True

script_directory = os.path.dirname(os.path.abspath(__file__))

async def main(
    phone: str,
    api_id: int,
    api_hash: str,
    source_group: str,
    letter_key: str,
    offset: int
):
    bot_credentials = {
        "session_name": phone.replace(" ", ''),
        "api_id": api_id,
        "api_hash": api_hash,
        "phone_number": phone,
    }

    if not await write_bot(bot_credentials):
        print("JSON fail")
    
    session_path = os.path.join(script_directory, "data", bot_credentials["session_name"])

    async with TelegramClient(
        session_path, bot_credentials["api_id"], bot_credentials["api_hash"]
    ) as client:
        # Add BOT to group
        logger = logging.getLogger('msg')
        logger.setLevel(logging.debug)
        try:
            await client(functions.channels.JoinChannelRequest(
                channel=source_group
            ))
        except Exception as e:
                logging.error(f"Greska pri ulazenju u grupu {source_group}: {e}")

        logger.error(f"Poceo da radim za slovo {letter_key}")
        participants = await client(GetParticipantsRequest(
            channel=source_group,
            filter=ChannelParticipantsSearch(letter_key),
            offset=offset,
            limit=offset_range,
            hash=0
        ))
        if not participants.users:
            message = f"Nema vise membera za slovo {letter_key} na nalogu {bot_credentials['phone_number']}"
            logger.error(message)
            file_path = f"{script_directory}/data/{bot_credentials['phone_number']}.txt"
            os.makedirs(os.path.dirname(file_path), exist_ok=True) 
            with open(file_path, "w") as file:
                file.write(message)
            return message
        else:
            logger.error('usao u else, prolazi kroz usere')
            for user in participants.users:
                try:
                    if re.findall(r"\b[a-zA-Z]", user.first_name)[0].lower() == letter_key:
                        if not (user.fake or user.scam or user.bot or user.support):
                            all_participants.append(user)
                except:
                    pass
        logging.info(f"Uzeo {len(all_participants)} membera")
        
        # WRITE TO JSON
        users_info_json = []
        for user in all_participants:
            user_dict = {
                "id": user.id,
                "first_name": user.first_name,
                "username": user.username,
                "access_hash": user.access_hash
            }
            users_info_json.append(user_dict)
        json_file_path = f"data/{bot_credentials['session_name']}_members.json"
        # Write the array of users to the JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(users_info_json, json_file, indent=4)
        return None


def run_main(
    phone: str = typer.Option(..., "--phone", help="Phone number"),
    api_id: int = typer.Option(..., "--id", help="Api ID"),
    api_hash: str = typer.Option(..., "--hash", help="Api Hash"),
    source_group: str = typer.Option(..., "--source_group", help="Source group"),
    letter_key: str = typer.Option(..., "--letter_key", help="Letter"),
    offset: int = typer.Option(..., "--offset", help="Offset")
   
):
    asyncio.run(main(phone, api_id, api_hash, source_group, letter_key, offset))


if __name__ == "__main__":
    app.command()(run_main)
    app()