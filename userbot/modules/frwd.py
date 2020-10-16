"""Enable Seen Counter in any message,
to know how many users have seen your message
Syntax: .frwd as reply to any message"""
from userbot.events import register
from userbot import (PRIVATE_CHANNEL_BOT_API_ID, TEMP_DOWNLOAD_DIRECTORY, LOGS, bot)


@register(incoming=True, disable_edited=True)
async def _(event):
    if event.fwd_from:
        return
    try:
        e = await event.client.get_entity(int(PRIVATE_CHANNEL_BOT_API_ID))
    except Exception as e:
        LOGS.warn(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await event.client.forward_messages(e, re_message, silent=True)
        await event.client.forward_messages(event.chat_id, fwd_message)
        await event.delete()
