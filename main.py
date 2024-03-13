# -*- coding: utf-8 -*-
from telethon import functions
from telethon.sync import TelegramClient


api_id = 1234
api_hash = '1234'

phone = +79612539374
username = '79612539374'

client = TelegramClient(username, api_id, api_hash)

async def main():
    await client.connect()

    search = 'linux'
    result = await client(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))
    print(result.stringify())


with client:
    client.loop.run_until_complete(main())
