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
    list_search = ['linux', 'Линукс', 'Ubuntu', 'Debian', 'Fedora', 'ArchLinux', 'CentOS', 'Kali Linux', 'Bash',
                   'Shell',
                   'Kernel', 'Systemd', 'Open Source', 'GNU/Linux', 'Terminal', 'Command Line', 'Sysadmin', 'DevOps',
                   'Server Administration', 'Linux Academy', 'Linux Education', 'Linux Users', 'Linux Community',
                   'Linux News', 'Linux Development', 'Linux Gaming', 'Embedded Linux', 'Raspberry Pi', 'Docker',
                   'Kubernetes', 'System Administration', 'Linux Mint', 'Elementary OS', 'LXDE', 'XFCE']

    for search in list_search:
        # search = 'linux'
        result = await client(functions.contacts.SearchRequest(
            q=search,
            limit=100
        ))
        for chat in result.chats:
            print(f'ID группы / канала: {chat.id}, '
                  f'Название группы / канала: {chat.title}, '
                  f'Количество участников группы / канала: {chat.participants_count}, '
                  f'Username группы / канала: {chat.username}, '
                  f'Hash группы / канала: {chat.access_hash}, '
                  f'Дата создания группы / канала: {chat.date}')

with client:
    client.loop.run_until_complete(main())
