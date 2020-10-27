"""
idea from lynda and rose bot
made by @mrconfused
"""
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, MessageEntityMentionName

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.utils.tools import time_formatter
from userbot.events import register

# =================== CONSTANT ===================
NO_ADMIN = "`I am not an admin!`"
NO_PERM = "`I don't have sufficient permissions!`"


@register(outgoing=True, pattern="^tmute(?: |$)(.*)")
async def tmuter(tmut):
    chat = await tmut.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await tmut.edit(NO_ADMIN)
        return
    await tmut.edit("`muting....`")
    user, reason = await get_user_from_event(tmut)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        tmuttime = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await tmut.edit("you havent mentioned time check `.help tadmin`")
        return
    self_user = await tmut.client.get_me()
    mtime = await time_formatter(tmut, tmuttime)
    if not mtime:
        await tmut.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {tmuttime}"
        )
        return
    if user.id == self_user.id:
        await tmut.edit(f"Sorry, I can't mute my self")
        return
    try:
        await tmut.client(
            EditBannedRequest(
                tmut.chat_id,
                user.id,
                ChatBannedRights(until_date=mtime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await tmut.edit(
                f"{user.first_name} was muted in {tmut.chat.title}\n"
                f"**Mutted for : **{tmuttime}\n"
                f"**Reason : **__{reason}__"
            )
            if BOTLOG:
                await tmut.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{tmut.chat.title}(`{tmut.chat_id}`)\n"
                    f"**Mutted for : **`{tmuttime}`\n"
                    f"**Reason : **`{reason}``",
                )
        else:
            await tmut.edit(
                f"{user.first_name} was muted in {tmut.chat.title}\n"
                f"Mutted for {tmuttime}\n"
            )
            if BOTLOG:
                await tmut.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{tmut.chat.title}(`{tmut.chat_id}`)\n"
                    f"**Mutted for : **`{tmuttime}`",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await tmut.edit("`Uh oh my mute logic broke!`")
