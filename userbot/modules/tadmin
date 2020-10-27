"""
idea from lynda and rose bot
made by @mrconfused
ported for OUB-remix by @ashwinstr (github), @AshSTR (tg)
"""
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, MessageEntityMentionName

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.utils.funtions import extract_time
from userbot.events import register

# =================== CONSTANT ===================
NO_ADMIN = "`I am not an admin!`"
NO_PERM = "`I don't have sufficient permissions!`"


@register(outgoing=True, pattern="^.tmute(?: |$)(.*)")
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
    mtime = await extract_time(tmut, tmuttime)
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

@register(outgoing=True, pattern="^.tban(?: |$)(.*)")
async def ban(tbun):
    chat = await tbun.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await tbun.edit(NO_ADMIN)
        return
    await tbun.edit("`tbanning....`")
    user, reason = await get_user_from_event(tbun)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        tbuntime = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await tbun.edit("you havent mentioned time check `.help tadmin`")
        return
    self_user = await tbun.client.get_me()
    btime = await extract_time(tbun, tbuntime)
    if not btime:
        await tbun.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {tbuntime}"
        )
        return
    if user.id == self_user.id:
        await tbun.edit(f"Sorry, I can't ban my self")
        return
    await tbun.edit("`Whacking the pest!`")
    try:
        await tbun.client(
            EditBannedRequest(
                tbun.chat_id,
                user.id,
                ChatBannedRights(until_date=btime, view_messages=True),
            )
        )
    except BadRequestError:
        await tbun.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await tbun.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await tbun.edit(
            "`I dont have message nuking rights! But still he was banned!`"
        )
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await tbun.edit(
            f"{user.first_name} was banned in {tbun.chat.title}\n"
            f"banned for {tbuntime}\n"
            f"Reason:`{reason}`"
        )
        if BOTLOG:
            await tbun.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{tbun.chat.title}(`{tbun.chat_id}`)\n"
                f"**Banned untill : **`{tbuntime}`\n"
                f"**Reason : **__{reason}__",
            )
    else:
        await tbun.edit(
            f"{user.first_name} was banned in {tbun.chat.title}\n"
            f"banned for {tbuntime}\n"
        )
        if BOTLOG:
            await tbun.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{tbun.chat.title}(`{tbun.chat_id}`)\n"
                f"**Banned untill : **`{tbuntime}`",
            )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await event.edit("Could not fetch info of that user.")
            return None
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


CMD_HELP.update(
    {
        "tadmin": "**Plugin :** `tadmin`\
      \n\n**Syntax : **`.tmute <reply/username/userid> <time> <reason>`\
      \n**Usage : **Temporary mutes the user for given time.\
      \n\n**Syntax : **`.tban <reply/username/userid> <time> <reason>`\
      \n**Usage : **Temporary bans the user for given time.\
      \n\n**Time units : ** (2m = 2 minutes) ,(3h = 3hours)  ,(4d = 4 days) ,(5w = 5 weeks)\
      This times are example u can use anything with those units "
    }
)
