# -*- coding: utf-8 -*-
from telethon import functions
from telethon.sync import TelegramClient
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']


client = TelegramClient(username, int(api_id), api_hash)


async def main():
    await client.connect()

    search = 'linux'
    result = await client(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))
    for chat in result.chats:
        print(f"ID группы / канала: {chat.id}")
        print(f"Название группы / канала: {chat.title}")
        print(f'Количество участников группы / канала: {chat.participants_count}')
        print(f"Username группы / канала: {chat.username}")
        print(f'Hash группы / канала: {chat.access_hash}')
        print(f"Дата создания группы / канала: {chat.date}")
        print("------------------------------")

with client:
    client.loop.run_until_complete(main())
