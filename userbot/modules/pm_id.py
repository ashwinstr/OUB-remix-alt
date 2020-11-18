# pm and tagged messages logger for catuserbot by @mrconfused (@sandy1709)
# port for remix by @AshSTR (@ashwinstr)

import asyncio
from userbot import PM_LOGGR_BOT_API_ID, NC_LOG_P_M_S, LOGS
from userbot.events import register

RECENT_USER = None
NEWPM = None
COUNT = 0

@register(incoming=True, func=lambda e: e.is_private)
async def monito_p_m_s(event):
    global RECENT_USER
    global NEWPM
    global COUNT
    if not PM_LOGGR_BOT_API_ID:
        return
    sender = await event.get_sender()
    if NC_LOG_P_M_S and not sender.bot:
        chat = await event.get_chat()
        if chat.id != 777000:
            if RECENT_USER != chat.id:
                RECENT_USER = chat.id
                if NEWPM:
                    if COUNT > 1:
                        await NEWPM.edit(
                            NEWPM.text.replace("new message", f"{COUNT} messages")
                        )
                    else:
                        await NEWPM.edit(
                            NEWPM.text.replace("new message", f"{COUNT} message")
                        )
                    COUNT = 0
                await event.client.send_message(
                    PM_LOGGR_BOT_API_ID,
                    f"[{sender.first_name}](tg://user?id={sender.id}) has sent a new message \n**Id : **`{chat.id}`",
                )
                COUNT += 1
