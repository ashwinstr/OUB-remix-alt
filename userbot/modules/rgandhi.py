# (c) @Unknown
# Original written by @Unknown edit by @Unbornkiller

from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.rgandhi$")
async def rgandhi(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\nEk side se allu dalunga dusre side se sona niklega`")
