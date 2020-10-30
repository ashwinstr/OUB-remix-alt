""" Mod downloader plugin by @raina_hanan | Syntax: .mod app name"""
# ported for remix by @ashwinstr(github), @AshSTR(tg)

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.events import register


@register(outgoing=True, pattern="^.mod ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`Searching for the mod!`**Please be patient**")
    else:
        await event.edit("I don't need a Link! Give me a Name")
    bot = "@ModdedApp_bot"
    async with client.conversation("@ModdedApp_bot") as conv:
        try:
            await conv.send_message("/start")
            response = await conv.get_response()
            try:
                await event(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
            except UserAlreadyParticipantError:
                await asyncio.sleep(0.00000069420)
            await conv.send_message(d_link)
            details = await conv.get_response()
            await client.send_message(event.chat_id, details)
            await conv.get_response()
            songh = await conv.get_response()
            await client.send_file(event.chat_id, apk,
                                 caption="Here's the requested app!\n`Check out` [;)](@apkdl_bot)")
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @ModdedApp_bot `and retry!`")

