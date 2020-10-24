"""Notification Manager for @UniBorg
"""

import asyncio
import io
#import sql_helpers.no_log_pms_sql as no_log_pms_sql
import userbot.modules.sql_helper.pm_permit_sql as pm_permit_sql
from telethon import events, errors, functions, types
#from userbot.utils import admin_cmd
from userbot.events import register
from userbot import PM_LOGGR_BOT_API_ID, MAX_FLOOD_IN_P_M_s

REMIX_USER_BOT_WARN_ZERO = "I am currently offline. Please do not SPAM me."
REMIX_USER_BOT_NO_WARN = "Hi! I will answer to your message soon. Please wait for my response and don't spam my PM. Thanks"


@register(events())
async def on_new_channel_message(event):
    if PM_LOGGR_BOT_API_ID is None:
        return
    try:
        if tgbot is None:
            return
    except Exception as e:
        logger.info(str(e))
        return
    # logger.info(event.stringify())
    if isinstance(event, types.UpdateChannel):
        channel_id = event.channel_id
        message_id = 2
        # someone added me to channel
        # TODO: https://t.me/TelethonChat/153947
        the_message = ""
        the_message += "#MessageActionChatAddUser\n\n"
        # the_message += f"[User](tg://user?id={added_by_user}): `{added_by_user}`\n"
        the_message += f"[Private Link](https://t.me/c/{channel_id}/{message_id})\n"
        await event.send_message(
            entity=Config.PM_LOGGR_BOT_API_ID,
            message=the_message,
            # reply_to=,
            # parse_mode="html",
            link_preview=False,
            # file=message_media,
            silent=True
        )


"""@borg.on(events.Raw())
async def _(event):
    if Config.PM_LOGGR_BOT_API_ID is None:
        return
    if tgbot is None:
        return
    logger.info(event.stringify())"""


"""if tgbot is not None:
    @tgbot.on(events.Raw())
    async def _(event):
        if Config.PM_LOGGR_BOT_API_ID is None:
            return
        logger.info(event.stringify())"""


async def do_pm_permit_action(chat_id, event):
    if chat_id not in PM_WARNS:
        PM_WARNS.update({chat_id: 0})
    if PM_WARNS[chat_id] == MAX_FLOOD_IN_P_M_s:
        r = await event.reply(REMIX_USER_BOT_WARN_ZERO)
        await asyncio.sleep(3)
        await event.client(functions.contacts.BlockRequest(chat_id))
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        the_message = ""
        the_message += "#BLOCKED_PMs\n\n"
        the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
        the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
        # the_message += f"Media: {message_media}"
        await event.client.send_message(
            entity=PM_LOGGR_BOT_API_ID,
            message=the_message,
            # reply_to=,
            # parse_mode="html",
            link_preview=False,
            # file=message_media,
            silent=True
        )
        return
    r = await event.reply(REMIX_USER_BOT_NO_WARN)
    PM_WARNS[chat_id] += 1
    if chat_id in PREV_REPLY_MESSAGE:
        await PREV_REPLY_MESSAGE[chat_id].delete()
    PREV_REPLY_MESSAGE[chat_id] = r


async def do_log_pm_action(chat_id, event, message_text, message_media):
    the_message = ""
    the_message += "#LOG_PMs\n\n"
    the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
    the_message += f"Message: {message_text}\n"
    # the_message += f"Media: {message_media}"
    await event.client.send_message(
        entity=PM_LOGGR_BOT_API_ID,
        message=the_message,
        # reply_to=,
        # parse_mode="html",
        link_preview=False,
        file=message_media,
        silent=True
    )
