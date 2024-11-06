# Copyright (C) 2024 by DORA_Help @ Github, < https://github.com/ITZ-dora/DORA-VC >
# Subscribe On YT < PEEYUSH >. All rights reserved. © DORA © Yukki.

""""
TheTeamDORA is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=DORA <https://github.com/ITZ-dora/DORA-VC>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
from DORAMusic import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from DORAMusic.core.mongo import db as DORA
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DORAMusic.utils.database import get_served_users, get_served_chats


OWNER_ID = 6439075095
