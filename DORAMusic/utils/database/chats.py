# Copyright (C) 2024 by DORA_Help @ Github, < https://github.com/ITZ-dora/DORA-VC >
# Subscribe On YT < PEEYUSH >. All rights reserved. © DORA © Yukki.

""""
TheTeamDORA is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=DORA <https://github.com/ITZ-dora/DORA-VC>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from typing import Dict, List, Union

from DORAMusic.core.mongo import mongodb

chatsdb = db.chats


async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})
