# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.

from userbot.events.callbackquery.CallbackQuery import CallbackQuery
from telethon import filters
import json
import os
from userbot import BOT_TOKEN, BOT_USERNAME, HU_STRING_SESSION, CMD_HELP, bot
from userbot.event import register

SECRETS = "userbot/modules/secret.txt"


if BOT_TOKEN and BOT_USERNAME:
    if HU_STRING_SESSION:
        ubot = userbot.bot
    else:
        ubot = userbot

       
    @register(outgoing=True, pattern=r"^.secret_(.*)")
    async def alive_callback(c_q, CallbackQuery):
        msg_id = CallbackQuery.pattern_match.group(1)
        if os.path.exists(SECRETS):
            view_data = json.load(open(SECRETS))
            sender = await CallbackQuery.get_me()
            msg = f"🔓 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗳𝗿𝗼𝗺: {sender.first_name}"
            msg += f" {sender.last_name}\n" if sender.last_name else "\n"
            data = view_data[msg_id]
            receiver =  data['user_id']
            msg += data['msg']
            u_id = c_q.from_user.id
            if u_id in [Config.OWNER_ID, receiver]:
                await c_q.answer(msg, show_alert=True)
            else:
                await c_q.answer("This Message is Confidential", show_alert=True)
        else:
            await c_q.answer("This message doesn't exist anymore", show_alert=True)
