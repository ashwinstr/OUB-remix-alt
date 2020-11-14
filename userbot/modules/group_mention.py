from userbot.events import register
from userbot import NO_PM_LOG_USERS, PM_LOGGR_BOT_API_ID

@register(outgoing=True, incoming=True, func=lambda e: e.mentioned))
async def log_tagged_messages(event):
    hmm = await event.get_chat()
    if hmm.id in NO_PM_LOG_USERS:
        return
        
    if PM_LOGGR_BOT_API_ID:
        sender = await event.get_sender()
        await asyncio.sleep(5)
        if not event.is_private:
            await event.client.send_message(
                Config.PM_LOGGR_BOT_API_ID,
                f"#TAGS \n<b>Group : </b><code>{hmm.title}</code>\
                        \n<b>Message : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>",
                parse_mode="html",
                link_preview=False,
            )
