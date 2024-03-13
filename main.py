#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tested with Telethon version 1.14.0

import configparser

from telethon import functions
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient

# no need for quotes

# you can get telegram development credentials in telegram API Development Tools
api_id = 1234
api_hash = 1234

# use full phone number including + and country code
phone = +4411111111111
username = session_user

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
# (1) Use your own values here
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

# (2) Create the client and connect
phone = config['Telegram']['phone']
username = config['Telegram']['username']
client = TelegramClient(username, api_id, api_hash)


async def main():
    await client.start()
    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    search = 'linux'
    result = await client(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))
    print(result.stringify())


with client:
    client.loop.run_until_complete(main())
