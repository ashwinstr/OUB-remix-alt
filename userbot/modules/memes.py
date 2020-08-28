# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#custom cmds by @heyworld to make it look more gayish
#Thanks to @AbhinavShinde for strings
""" Userbot module for having some fun with people. """

from asyncio import sleep
import asyncio
import random
from random import choice, getrandbits, randint
from re import sub
from random import randint
from os import execl
import time
from telethon import events, functions
from userbot import bot




from collections import deque

import requests
import sys
import os
import io
import html

import json

from cowpy import cow

from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
METOOSTR = [
    "Me too thanks",
    "Haha yes, me too",
    "Same lol",
    "Me irl",
    "Same here",
    "Haha yes",
    "Me rn",
]

ZALG_LIST = [[
    "̖",
    " ̗",
    " ̘",
    " ̙",
    " ̜",
    " ̝",
    " ̞",
    " ̟",
    " ̠",
    " ̤",
    " ̥",
    " ̦",
    " ̩",
    " ̪",
    " ̫",
    " ̬",
    " ̭",
    " ̮",
    " ̯",
    " ̰",
    " ̱",
    " ̲",
    " ̳",
    " ̹",
    " ̺",
    " ̻",
    " ̼",
    " ͅ",
    " ͇",
    " ͈",
    " ͉",
    " ͍",
    " ͎",
    " ͓",
    " ͔",
    " ͕",
    " ͖",
    " ͙",
    " ͚",
    " ",
],
             [
                 " ̍",
                 " ̎",
                 " ̄",
                 " ̅",
                 " ̿",
                 " ̑",
                 " ̆",
                 " ̐",
                 " ͒",
                 " ͗",
                 " ͑",
                 " ̇",
                 " ̈",
                 " ̊",
                 " ͂",
                 " ̓",
                 " ̈́",
                 " ͊",
                 " ͋",
                 " ͌",
                 " ̃",
                 " ̂",
                 " ̌",
                 " ͐",
                 " ́",
                 " ̋",
                 " ̏",
                 " ̽",
                 " ̉",
                 " ͣ",
                 " ͤ",
                 " ͥ",
                 " ͦ",
                 " ͧ",
                 " ͨ",
                 " ͩ",
                 " ͪ",
                 " ͫ",
                 " ͬ",
                 " ͭ",
                 " ͮ",
                 " ͯ",
                 " ̾",
                 " ͛",
                 " ͆",
                 " ̚",
             ],
             [
                 " ̕",
                 " ̛",
                 " ̀",
                 " ́",
                 " ͘",
                 " ̡",
                 " ̢",
                 " ̧",
                 " ̨",
                 " ̴",
                 " ̵",
                 " ̶",
                 " ͜",
                 " ͝",
                 " ͞",
                 " ͟",
                 " ͠",
                 " ͢",
                 " ̸",
                 " ̷",
                 " ͡",
             ]]

EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

INSULT_STRINGS = [
    "Owww ... Such a stupid idiot.",
    "Don't drink and type.",
    "I think you should go home or better a mental asylum.",
    "Command not found. Just like your brain.",
    "Do you realize you are making a fool of yourself? Apparently not.",
    "You can type better than that.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "Sorry, we do not sell brains.",
    "Believe me you are not normal.",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "Zombies eat brains... you're safe.",
    "You didn't evolve from apes, they evolved from you.",
    "Come back and talk to me when your I.Q. exceeds your age.",
    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.",
    "What language are you speaking? Cause it sounds like bullshit.",
    "Stupidity is not a crime so you are free to go.",
    "You are proof that evolution CAN go in reverse.",
    "I would ask you how old you are but I know you can't count that high.",
    "As an outsider, what do you think of the human race?",
    "Brains aren't everything. In your case they're nothing.",
    "Ordinarily people live and learn. You just live.",
    "I don't know what makes you so stupid, but it really works.",
    "Keep talking, someday you'll say something intelligent! (I doubt it though)",
    "Shock me, say something intelligent.",
    "Your IQ's lower than your shoe size.",
    "Alas! Your neurotransmitters are no more working.",
    "Are you crazy you fool.",
    "Everyone has the right to be stupid but you are abusing the privilege.",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",
    "You should try tasting cyanide.",
    "Your enzymes are meant to digest rat poison.",
    "You should try sleeping forever.",
    "Pick up a gun and shoot yourself.",
    "You could make a world record by jumping from a plane without parachute.",
    "Stop talking BS and jump in front of a running bullet train.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.",
    "Go Green! Stop inhaling Oxygen.",
    "God was searching for you. You should leave to meet him.",
    "give your 100%. Now, go donate blood.",
    "Try jumping from a hundred story building but you can do it only once.",
    "You should donate your brain seeing that you never used it.",
    "Volunteer for target in an firing range.",
    "Head shots are fun. Get yourself one.",
    "You should try swimming with great white sharks.",
    "You should paint yourself red and run in a bull marathon.",
    "You can stay underwater for the rest of your life without coming back up.",
    "How about you stop breathing for like 1 day? That'll be great.",
    "Try provoking a tiger while you both are in a cage.",
    "Have you tried shooting yourself as high as 100m using a canon.",
    "You should try holding TNT in your mouth and igniting it.",
    "Try playing catch and throw with RDX its fun.",
    "I heard phogine is poisonous but i guess you wont mind inhaling it for fun.",
    "Launch yourself into outer space while forgetting oxygen on Earth.",
    "You should try playing snake and ladders, with real snakes and no ladders.",
    "Dance naked on a couple of HT wires.",
    "Active Volcano is the best swimming pool for you.",
    "You should try hot bath in a volcano.",
    "Try to spend one day in a coffin and it will be yours forever.",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
    "You can be the first person to step on sun. Have a try.",
]

CONGOSTR = [
    "`Congratulations and BRAVO!`",
    "`You did it! So proud of you!`",
    "`This calls for celebrating! Congratulations!`",
    "`I knew it was only a matter of time. Well done!`",
    "`Congratulations on your well-deserved success.`",
    "`Heartfelt congratulations to you.`",
    "`Warmest congratulations on your achievement.`",
    "`Congratulations and best wishes for your next adventure!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
    "`Congrats! This is not a new surprise for us to see your success. Success is all your right from day one when you started achieving.`",
    "`Congratulations for your fabulous victory. You deserve it every bit.`",
    "`Congratulations on your success.`",
    "`Congratulations for making your dreams come true.`",
    "`Congratulations for achieving so much on your own steam.`",
    "`A well earned promotion to a well deserved person Congratulations.`",
    "`Congrats Am in awe of you for the rest of my life.`",
    "`May this moment last forever Congratulations.`",
    "`Congratulations for now and bright future.`",
    "`Your success deserves celebration and a big congratulation.`",
    "`You deserve the biggest congratulation for all your hard works!`",
    "`Congratulations Wishing you all the excitement and very happiness.`",
    "`You’re doing amazing Congrats!`",
    "`Congrats This calls for a huge celebration!`",
]

GDNOON = [
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good Afternoon Dear!`",
    "`With a deep blue sky over my head and a relaxing wind around me, the only thing I am missing right now is the company of you. I wish you a refreshing afternoon!`",
    "`The day has come a halt realizing that I am yet to wish you a great afternoon. My dear, if you thought you were forgotten, you’re so wrong. Good afternoon!`",
    "`Good afternoon! May the sweet peace be part of your heart today and always and there is life shining through your sigh. May you have much light and peace.`",
    "`With you, every part of a day is beautiful. I live every day to love you more than yesterday. Wishing you an enjoyable afternoon my love!`",
    "`This bright afternoon sun always reminds me of how you brighten my life with all the happiness. I miss you a lot this afternoon. Have a good time`!",
    "`Nature looks quieter and more beautiful at this time of the day! You really don’t want to miss the beauty of this time! Wishing you a happy afternoon!`",
    "`What a wonderful afternoon to finish you day with! I hope you’re having a great time sitting on your balcony, enjoying this afternoon beauty!`",
    "`I wish I were with you this time of the day. We hardly have a beautiful afternoon like this nowadays. Wishing you a peaceful afternoon!`",
    "`As you prepare yourself to wave goodbye to another wonderful day, I want you to know that, I am thinking of you all the time. Good afternoon!`",
    "`This afternoon is here to calm your dog-tired mind after a hectic day. Enjoy the blessings it offers you and be thankful always. Good afternoon!`",
    "`The gentle afternoon wind feels like a sweet hug from you. You are in my every thought in this wonderful afternoon. Hope you are enjoying the time!`",
    "`Wishing an amazingly good afternoon to the most beautiful soul I have ever met. I hope you are having a good time relaxing and enjoying the beauty of this time!`",
    "`Afternoon has come to indicate you, Half of your day’s work is over, Just another half a day to go, Be brisk and keep enjoying your works, Have a happy noon!`",
    "`Mornings are for starting a new work, Afternoons are for remembering, Evenings are for refreshing, Nights are for relaxing, So remember people, who are remembering you, Have a happy noon!`",
    "`If you feel tired and sleepy you could use a nap, you will see that it will help you recover your energy and feel much better to finish the day. Have a beautiful afternoon!`",
    "`Time to remember sweet persons in your life, I know I will be first on the list, Thanks for that, Good afternoon my dear!`",
    "`May this afternoon bring a lot of pleasant surprises for you and fills you heart with infinite joy. Wishing you a very warm and love filled afternoon!`",
    "`Good, better, best. Never let it rest. Til your good is better and your better is best. “Good Afternoon`”",
    "`May this beautiful afternoon fill your heart boundless happiness and gives you new hopes to start yours with. May you have lot of fun! Good afternoon dear!`",
    "`As the blazing sun slowly starts making its way to the west, I want you to know that this beautiful afternoon is here to bless your life with success and peace. Good afternoon!`",
    "`The deep blue sky of this bright afternoon reminds me of the deepness of your heart and the brightness of your soul. May you have a memorable afternoon!`",
    "`Your presence could make this afternoon much more pleasurable for me. Your company is what I cherish all the time. Good afternoon!`",
    "`A relaxing afternoon wind and the sweet pleasure of your company can make my day complete. Missing you so badly during this time of the day! Good afternoon!`",
    "`Wishing you an afternoon experience so sweet and pleasant that feel thankful to be alive today. May you have the best afternoon of your life today!`",
    "`My wishes will always be with you, Morning wish to make you feel fresh, Afternoon wish to accompany you, Evening wish to refresh you, Night wish to comfort you with sleep, Good afternoon dear!`",
    "`Noon time – it’s time to have a little break, Take time to breathe the warmth of the sun, Who is shining up in between the clouds, Good afternoon!`",
    "`You are the cure that I need to take three times a day, in the morning, at the night and in the afternoon. I am missing you a lot right now. Good afternoon!`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`I pray to god that he keeps me close to you so we can enjoy these beautiful afternoons together forever! Wishing you a good time this afternoon!`",
    "`You are every bit of special to me just like a relaxing afternoon is special after a toiling noon. Thinking of my special one in this special time of the day!`",
    "`May your Good afternoon be light, blessed, enlightened, productive and happy.`",
    "`Thinking of you is my most favorite hobby every afternoon. Your love is all I desire in life. Wishing my beloved an amazing afternoon!`",
    "`I have tasted things that are so sweet, heard words that are soothing to the soul, but comparing the joy that they both bring, I’ll rather choose to see a smile from your cheeks. You are sweet. I love you.`",
    "`How I wish the sun could obey me for a second, to stop its scorching ride on my angel. So sorry it will be hot there. Don’t worry, the evening will soon come. I love you.`",
    "`I want you when I wake up in the morning, I want you when I go to sleep at night and I want you when I relax under the sun in the afternoon!`",
    "`With you every day is my lucky day. So lucky being your love and don’t know what else to say. Morning night and noon, you make my day.`",
    "`Your love is sweeter than what I read in romantic novels and fulfilling more than I see in epic films. I couldn’t have been me, without you. Good afternoon honey, I love you!`",
    "`No matter what time of the day it is, No matter what I am doing, No matter what is right and what is wrong, I still remember you like this time, Good Afternoon!`",
    "`Things are changing. I see everything turning around for my favor. And the last time I checked, it’s courtesy of your love. 1000 kisses from me to you. I love you dearly and wishing you a very happy noon.`",
    "`You are sometimes my greatest weakness, you are sometimes my biggest strength. I do not have a lot of words to say but let you make sure, you make my day, Good Afternoon!`",
    "`Every afternoon is to remember the one whom my heart beats for. The one I live and sure can die for. Hope you doing good there my love. Missing your face.`",
    "`My love, I hope you are doing well at work and that you remember that I will be waiting for you at home with my arms open to pamper you and give you all my love. I wish you a good afternoon!`",
    "`Afternoons like this makes me think about you more. I desire so deeply to be with you in one of these afternoons just to tell you how much I love you. Good afternoon my love!`",
    "`My heart craves for your company all the time. A beautiful afternoon like this can be made more enjoyable if you just decide to spend it with me. Good afternoon!`",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]

SMILE = [
    "( ͡° ͜ʖ ͡°)",
"∠( ᐛ 」∠)＿",
"(ﾟ⊿ﾟ)",
"ᕕ( ᐛ )ᕗ",
"_へ__(‾◡◝ )>",
"( ᐛ )و",
"( ´ ▽ ` )ﾉ",
"(*^▽^*)",
"(´∇ﾉ｀*)ノ",
"(ノ^∇^)",
"⊂((・▽・))⊃",
"(　＾∇＾)",
"( ﾟ▽ﾟ)/",
"（‐＾▽＾‐）",
"(“⌒∇⌒”)",
"（*´▽｀*）",
"(*＾▽＾)／",
"(*^▽^*)",
"(*~▽~)",
"(*≧▽≦)",
"(*⌒∇⌒*)",
"(*⌒▽⌒*)θ～♪",
"(/^▽^)/",
"(^∇^)",
"(＾▽＾)",
"(￣▽￣)ノ",
"(￣▽+￣*)",
"(゜▽゜;)",
"（=´∇｀=）",
"(＝⌒▽⌒＝)",
"(≡^∇^≡)",
"(≧∇≦)/",
"（⌒▽⌒）",
"(⌒▽⌒)☆",
"（⌒▽⌒ゞ",
"(●⌒∇⌒●)",
"(❁´▽`❁)*✲ﾟ*",
"(ノ*゜▽゜*)",
"°˖✧◝(⁰▿⁰)◜✧˖°",
"~ヾ(＾∇＾)",
"∩(︶▽︶)∩",
"≧(´▽｀)≦",
"ー( ´ ▽ ` )ﾉ",
"ヾ(´▽｀;)ゝ",
"ヾ(＾∇＾)",
"d=(´▽｀)=b",
"o(〃＾▽＾〃)o",
"o(^▽^)o",
"Ｏ(≧∇≦)Ｏ",
"o(≧∇≦o)",
"(๑꒪▿꒪)*",
"(⁎⚈᷀᷁▿⚈᷀᷁⁎)",
"(≧∇≦*)",
"(=^▽^=)",
"o(*^▽^*)o",
"೭੧(❛▿❛✿)੭೨",
"☜(⌒▽⌒)☞",
"☜(˚▽˚)☞",
"ɾ⚈▿⚈ɹ",
"ﾍ(=￣∇￣)ﾉ",
"φ(*⌒▽⌒)ﾉ",
"(*･▽･*)",
"(☆▽☆)",
"≡(*′▽`)っ",
"」(￣▽￣」)",
"(〃⌒∇⌒)",
"〔´∇｀〕",
"(゜▼゜＊）",
"(｡´∀｀)ﾉ",
"(　´∀｀)",
"(・∀・)",
"(´∀`)",
"(°∀°)b",
"(●´∀｀●)",
"(✌ﾟ∀ﾟ)☞",
"*(*´∀｀*)☆",
"( ´ ∀ ` )",
"ヽ(･∀･)ﾉ",
"(。≖ˇ∀ˇ≖。)",
"((o(´∀｀)o))",
"o(´∀｀*)",
"(ﾟ∀ﾟ　)",
"(*≧∀≦*)",
"(*ﾟ∀ﾟ*)",
"ヾ(*´∀｀*)ﾉ",
"(o^∀^o)",
"ヾ(^ิ∀^ิ)",
"o(｀・∀・´)○",
"(ᗒᗊᗕ)",
"(ノ・∀・)ノ",
"o((◕ฺ∀ ◕✿ฺ))o",
"～̎̎٩(⌒͡∀⌒͡⌯̊)̥̊◦",
"(´･∀･`)",
"∩(´∀｀∩)",
"(ﾉ `･∀･)ﾉﾞ",
"( ﾟ∀ ﾟ)",
"Ψ(ﾟ∀ﾟ )Ψ",
"Ψ(　ﾟ∀ﾟ)Ψ",
"Ψ(ﾟ∀ﾟ)Ψ",
"d┃･∀･┃b",
"(*´･∀･)",
"(･∀･○)",
"【°∀°】",
"（★￣∀￣★）",
"(m*´∀`)m",
"=͟͟͞͞( ✌°∀° )☛",
"∩(´∀`∩)",
"∩( ´∀` )∩",
"(∩´∀`)∩",
"⊂( ・ ̫・)⊃",
"(*′☉.̫☉)",
"((ඏ.̫ඏ*))",
"⁽͑˙ˆ˙̫ˆ˙⁾̉",
"(๑★ .̫ ★๑)",
"‧⁺◟( ᵒ̴̶̷̥́ ·̫ ᵒ̴̶̷̣̥̀ )",
"(^～^)",
"(⌯⚈ै〰̇⚈ै)",
"( ‾ʖ̫‾)",
"(̂ ˃̥̥̥ ˑ̫ ˂̥̥̥ )̂",
"⁽ˇ́˙̫ˇ̀˵⁾",
"( ᵕ̤ ‧̫̮ ᵕ̤ )",
"⁽͑΅ ˙̫ ῭⁾̉",
"(⋆ʾ ˙̫̮ ʿ⋆)",
"(*´・ｖ・)",
"(*＾v＾*)",
"（＾ｖ＾）",
"(▰˘v˘▰)",
"(n˘v˘•)¬",
"(´｡･v･｡｀)",
"♡✧( ु•⌄• )",
"( •⌄• ू )✧",
"(⌯⌅⌄⌅)",
"῍̩̞(∗ɞ⌄ɞ∗)◞",
"(′ʘ⌄ʘ‵)",
"( ^_^)／",
"(^ _ ^)/",
"（＾_＾）",
"(^-^*)/",
"（￣ー￣）",
"(∩_∩)",
"(∩▂∩)",
"(☆^ー^☆)",
"（ｖ＾＿＾）ｖ",
"p(*＾-＾*)q",
"(^・ω・^ )",
"(=^-ω-^=)",
"(=^･ω･^)y＝",
"( ﾉ^ω^)ﾉﾟ",
"（＿´ω｀）",
"(｡･ω･｡)",
"(︶ω︶)",
"(｀・ω・´)”",
"(´ω｀★)",
"(＾ω＾)",
"(◐ω◑ )",
"∩( ・ω・)∩",
"ヾ(｡･ω･｡)",
"୧( ॑ധ ॑)୨",
"d(=^･ω･^=)b",
"ｏ（Ｕ・ω・）⊃",
"V(=^･ω･^=)v",
"川´･ω･`川",
"(*´꒳`*)",
"(*^ω^*)",
"(❁´ω`❁)",
"(´-ω-`)",
"ଘ(੭ˊ꒳ˋ)੭✧",
"(´へωへ`*)",
"(　^ω^）",
"（　＾ω＾）",
"(✌’ω’)✌",
"✌(‘ω’)✌",
"✌(‘ω’✌)",
"٩(ↁωↁ❀)",
"˚✧₊⁎( ˘ω˘ )⁎⁺˳✧༚",
"(◜௰◝)",
"✾(〜 ☌ω☌)〜✾",
"(´∩ω∩｀)",
"(¬‿¬)",
"( ⋂‿⋂’)",
"(-‿◦☀)",
"(*‿*✿)",
"(•‿•)",
"(•̀ᴗ•́)و ̑̑",
"(─‿─)",
"(◍•ᴗ•◍)❤",
"(◑‿◐)",
"(✿´‿`)",
"(❀◦‿◦)",
"(❁´‿`❁)*✲ﾟ*",
"(ᅌᴗᅌ* )",
"(•ˇ‿ˇ•)-→",
"♫꒰･‿･๑꒱",
"o (^‿^✿)",
"(◑‿◐✿)",
"(◡‿◡✿)",
"(✿◠‿◠)",
"(◕‿◕✿)",
"(๑>ᴗ<๑)",
"(๑✧◡✧๑)",
"(๑>◡<๑)",
"♪(๑ᴖ◡ᴖ๑)♪",
"(｡◝‿◜｡)",
"(๑^ں^๑)",
"( ்ͦˏ౦͜ˎ ்ͦ)",
"(ෆ ͒•∘̬• ͒)◞",
"(•⚗৺⚗•)",
"(ට˓˳̮ට๑)",
"(๑•͈ᴗ•͈)",
"₍՞◌′ᵕ‵ू◌₎♡",
"(੭ˊ͈ ꒵ˋ͈)੭̸*✧⁺˚",
"꒰⁎ᵉ̷͈ ॣ꒵ ॢᵉ̷͈⁎꒱໊",
"(⑅˘͈ ᵕ ˘͈ )",
":: ೖ(⑅σ̑ᴗσ̑)ೖ ::",
"三⊂( っ⌒◡|",
"(ؑᵒᵕؑ̇ᵒ)◞✧",
"꒰•́ॢ৺•̀ॢ๑͒꒱",
"(｡≍ฺ‿ฺ≍ฺ)",
"(⚈᷁‿᷇⚈᷁)",
"(๑◕ฺ‿ฺ◕ฺ๑)",
"⁽(◍˃̵͈̑ᴗ˂̵͈̑)",
"(人 •͈ᴗ•͈)",
"(*˙︶˙*)☆*°",
"(୨୧ ❛ᴗ❛)✧",
"( ¨̮ )",
"(＊◕ᴗ◕＊)",
"(*´╰╯`๓)♬",
"(∗❛ัᴗ❛ั∗)",
"⊂(◉‿◉)つ",
"(人 •͈ᴗ•͈✿ฺ)",
"( ･ᴗ･̥̥̥ )",
"(≖ ‿ ≖)",
"(๑˃͈꒵˂͈๑)",
"(⑅‾̥̥̥̥̥̑⌣‾̥̥̥̥̥̑⑅)",
"(>̯-̮<̯)",
"(⁎⚈᷀᷁ᴗ⚈᷀᷁⁎)",
"  (⁰ੌ⌣⁰ੌ๑)",
"(⚈᷀᷁ᴗ⚈᷀᷁⁎)",
"✌(-‿-)✌",
"(⋓ื◡⋓ื)",
"（。≖ิ‿≖ิ）",
"(๑￫‿ฺ￩๑)",
"ˆ̭̭͙(๑ ົ̅ ͔৹͜ ົ̅๑)",
"(∗ᵕ̴᷄◡ᵕ̴᷅∗)՞",
"( •॒◞ ͜◟•॒ )",
"(ㆁᴗㆁ✿)",
"(๑’◡͐’๑)",
"(⌒⃝৺⌒⃝)",
"{´◕ ◡ ◕｀}",
"(ට ̥̆ ට)",
"⁽͑˙˚̀ᵕ˚́˙⁾̉",
"(*☌ᴗ☌)｡*ﾟ",
"( ´◡‿ゝ◡`)",
"(　◠ ◡ ◠　)",
"ల(*´= ◡ =｀*)",
"₊⚛⁺(ؔ꒨◡ؔ꒨)ᵌ",
"( ்ͧˏ౦͜ˎ ்ͧ)",
"꒰⁎❛⃘ੌ ᵕ ❛⃘ੌ⁎꒱",
"( ́⋅⃘ˬ̇⋅⃘ ̀ˋ)",
"(. ົ̅ ੭͜ ົ̅.)",
"( ᵘ ᵕ ᵘ ⁎)",
"( ᵘ ᵕ ᵘ ⁎)",
"(๑`･ᴗ･´๑)",
"❀.(*´◡`*)❀.",
"◟(๑•͈ᴗ•͈)◞",
"₍ఠ ͜ఠ₎",
"(•‾̑⌣‾̑•)",
"(∗ᒩ͜∗)",
"( ்ૂ౧͜ ்)",
"(⋈･◡･)✰",
"(⁝̥ꑦᴗꑦ)",
"(︶.̮︶✽)",
"(❍❛‿❛❍❋)",
"₍•͈ᴗ•͈₎",
"(ͼ ̥̆ ͽ)",
"(≖ᴗ≖๑)",
"( °̥̥̥̥̥̥̥̥◡͐°̥̥̥̥̥̥̥̥)",
"( ´͈ ◡ `͈ )",
"( ๑॔•◡ુ•๑॓)",
"  (๑･`◡´･๑)",
",､’`(((;ŏᴗŏ))),､’`’`,､",
"ෆ⃛(ට◡ට⁎)ფ",
"੬ჴ❛‿❛ჴჱ̒̒",
"৵( °͜ °৵)",
"(✿◕ ‿◕ฺ)ノ))。₀: *゜",
"☆(❁‿❁)☆",
"◃┆◉◡◉┆▷",
"q(❂‿❂)p",
"☆(◒‿◒)☆",
"⊂◉‿◉つ",
"(｡✿‿✿｡)",
"໒( ﹒ ͜ر ﹒ )७",
"( ‾̮‿͂‾̮ ꐦ)",
"(˘･ᴗ･˘)",
"(ό‿ὸ)ﾉ",
"ヾ|๑　╹　◡　╹　๑|ﾉ",
"(((;◔ᴗ◔;)))",
"໒( ” ¤ ‿ ¤ ” )७",
"✩*॰ ( ¨̮ ) ॰*✩",
"(✧≖‿ゝ≖)",
"☝( ◠‿◠ )☝",
"(*´◡｀​*)",
"(๑◔‿◔๑)",
"(◕‿‿◕｡)",
"(✿╹◡╹)",
"(◕ฺ ◡ฺ ◕ฺ)",
"(✿ฺ◡ฺ‿ฺ◡ฺ)",
"（◞‿◟）",
"(o˘◡˘o)",
"ꉂꉂ ( ˆᴗˆ )",
"₊·(ϱ॔⌄ᵕ๑॓)‧*",
"-(๑☆‿ ☆#)ᕗ",
"╭ (oㅇ‿ o#)ᕗ",
"／人◕ ‿‿ ◕人＼",
"(o^^)o",
"ヾ(^ ^ゞ",
"o(^^o)",
"(o^^o)♪",
"(o⌒．⌒o)",
"(=^･^=)",
"。(⌒.⌒。)",
"( ﾉ^.^)ﾉﾟ",
"(“⌒.⌒”)",
"(≧.≦*)",
"(*^^*)",
"(ꐦ ´͈ ᗨ `͈ )",
"( ´͈ ॢꇴ  `͈)੭ु",
"（ꉺᗜꉺ）",
"(･ัᗜ･ั)و",
"✌✌(➲ ᗜ ➲)✌✌",
"✌✌(˵¯̴͒ꇴ¯̴͒˵)✌✌",
"( ˙̣̣̣ↂ⃙⃙⃚᷄ᗨↂ⃙⃙⃚ )ꋧ",
"(ᗒᗨᗕ)",
"(๑’ᗢ’๑)ฅ",
"(✤❛⃘ͫ Ʉ̮ ❛⃘ͫ)",
"┌༼ ˵ ° ᗜ ° ˵ ༽┐",
"ˉ̶̡̭̭ ( ´͈ ᗨ `͈ ) ˉ̶̡̭̭",
"(□ᗜ□)",
"(-^〇^-)",
"(.=^・ェ・^=)",
"(・◇・)",
"(*＾ワ＾*)",
"(*¬*)",
"(´ヮ`)",
"(^(I)^)",
"(^(エ)^)",
"（＾⊆＾）",
"(๑^っ^๑)",
"（＞ｙ＜）",
"(⊙ヮ⊙)",
"(☆^O^☆)",
"°˖ ✧◝(○ ヮ ○)◜✧˖ °",
"⊂(^(工)^)⊃",
"ヾ（*⌒ヮ⌒*）ゞ",
"(ⓥꇳⓥ*)",
"((ꉺꈊꉺ)ꀢ༣",
"(๑❛ꆚ❛๑)",
"(ᵒ̴̶̷̤́◞౪◟ ᵒ̴̶̷̤̀ )",
"(^ワ^＝)",
"(*´ч ` *)",
"（｡◑ヮ◑｡）",
"（ꉺ౪ꉺ）",
"( ◑ٹ◐)",
"(´ёٹё)",
"(*^ิ益^ิ*)",
"(´◉◞౪◟◉)",
"(*^｡^*)",
"(๑*౪*๑)",
"（＾凹＾）",
",､’`<(❛ヮ❛✿)>,､’`’`,､",
"ೖ(σ̑˽σ̑)ೖ",
"(●⌃ٹ⌃)",
"(*꒩̐﹀꒩̐*)",
"(^◇^；)",
"(✿ ◜◒◝ )",
"(´◉◞౪◟◉｀)",
"(థฺˇ౪ˇథ)",
"(⁎ؔꇵ ˒̠̮ ؔꇵ)",
"( •˓◞•̀ )",
"(*ꄱͦ︺ꄱͦ*)",
"( ՞ٹ՞)",
"( ´•౪•`)",
"(*´∪`)",
"(◍ȋ ₎໐͜₍ ȋ◍)",
"♪~♪ d(⌒o⌒)b♪~♪",
"♪♪ｖ(⌒ｏ⌒)ｖ♪♪",
"∩`･◇･)",
"(★^O^★)",
"(((o(*ﾟ▽ﾟ*)o)))",
"＼（＠￣∇￣＠）／",
"ヽ(；▽；)ノ",
"ヾ(@^▽^@)ノ",
"o((*^▽^*))o",
"Ｏ(≧▽≦)Ｏ",
"– =͟͟͞͞ ( ꒪౪꒪)ฅ✧",
"“ヽ(´▽｀)ノ”",
"(((＼（＠v＠）／)))",
"(ﾉ´ヮ´)ﾉ*:･ﾟ✧",
"(ノ^_^)ノ",
"(ノ＞▽＜。)ノ",
"(ﾉﾟ▽ﾟ)ﾉ",
"〈( ^.^)ノ",
"＼(*T▽T*)／",
"＼（＾▽＾）／",
"＼(^ω^＼)",
"＼（Ｔ∇Ｔ）／",
"☆*:.｡. o(≧▽≦)o .｡.:*☆",
"ヽ(;^o^ヽ)",
"ヽ(；▽；)ノ",
"ヽ(‘ ∇‘ )ノ",
"ヾ(＠† ▽ †＠）ノ",
"ヾ(＠^∇^＠)ノ",
"ヾ(＠^▽^＠)ﾉ",
"ヾ（＠＾▽＾＠）ノ",
"ヾ(@゜∇゜@)ノ",
"ヾ(＠゜▽゜＠）ノ",
"ヾ(@°▽°@)ノ",
"ヾ(＠⌒ー⌒＠)ノ",
"ヽ(*≧ω≦)ﾉ",
"ヽ(*・ω・)ﾉ",
"ヽ(*⌒∇⌒*)ﾉ",
"ヾ(＾-＾)ノ",
"ヽ(^。^)丿",
"ヽ(＾Д＾)ﾉ",
"ヽ(=^･ω･^=)丿",
"٩(^ᴗ^)۶",
"о(ж＞▽＜)ｙ ☆",
"ヘ(^_^ヘ)",
"ヘ(^o^ヘ)",
"へ(゜∇、°)へ",
"＼＼\ ٩(`(エ)´ )و //／／",
"(／・ω・)／",
"୧(﹒︠ᴗ﹒︡)୨",
"(☝ ՞ਊ ՞)☝",
"⸂⸂⸜(രᴗര๑)⸝⸃⸃",
"˛˛ƪ(⌾⃝ ౪ ⌾⃝ ๑)و ̉ ̉",
"ヾ(๑╹ヮ╹๑)ﾉ”",
"ヾ(๑╹ꇴ◠๑)ﾉ”",
"ヾ(๑ㆁᗜㆁ๑)ﾉ”",
"⁽⁽◞(꒪ͦᴗ̵̍꒪ͦ=͟͟͞͞ ꒪ͦᴗ̵̍꒪ͦ)◟⁾⁾",
"ヾ(Ő∀Ő๑)ﾉ",
"(੭ु｡╹▿╹｡)੭ु⁾⁾",
"₍₍ (ง Ŏ౪Ŏ)ว ⁾⁾",
"(ง •ૅ౪•᷄)ว",
"₍₍⁽⁽(ી(^‿ゝ^)ʃ)₎₎⁾⁾",
"(´ ↂ⃙⃙⃚ꇴↂ⃙⃙⃚ `≡´ ↂ⃙⃙⃚ꇴↂ⃙⃙⃚ `)",
"(ﾉ^_^)ﾉ",
"◦°˚\(*❛‿❛)/˚°◦",
"⌒°(ᴖ◡ᴖ)°⌒",
"⌒(o＾▽＾o)ノﾟ",
"｡:.ﾟヽ(´∀`｡)ﾉﾟ.:｡+ﾟ",
"ﾟ+｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡+ﾟ",
"ヾ(○･ω･)ﾉ☆",
"୧( “̮ )୨✧",
"✌(๑˃̶͈̀◡˂̶͈́๑)✌",
"✩◝(◍⌣̎◍)◜✩",
"∕∕∕ ∕ ∕∕˛₍˴◅ˋ)੭✧∕∕∕ ∕∕",
"(◜▿‾ ≡‾▿◝)",
"୧[ ˵ ͡ᵔ ͜ʟ ͡ᵔ ˵ ]୨",
"ヾ( ~▽~)ﾂ",
"(ﾉ*´▽)ﾉ",
"ヽ(^◇^*)/",
"ヾ（ ❀◕◡◕ฺฺ ）ノ",
"ヽ（◕◡◕❀ฺ ）ノ",
"ヾ(^▽^ヾ)",
"୧〳 ＾ ౪ ＾ 〵୨",
"=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
"(((o(*ﾟ▽ﾟ*)o)))",
"o((*^▽^*))o",
"Ｏ(≧▽≦)Ｏ",
"o(〃＾▽＾〃)o",
"o(^▽^)o",
"Ｏ(≧∇≦)Ｏ",
"o(≧∇≦o)",
"σ(≧ε≦ｏ)",
"o(*^▽^*)o",
"⌒°(❛ᴗ❛)°⌒",
"o(^∀^*)o",
"o(^◇^)o",
"《《o(≧◇≦)o》》",
"o(*≧□≦)o",
"o(*>ω<*)o",
"(ﾉ･ｪ･)ﾉ",
"(/^▽^)/",
"(ﾉ´ヮ´)ﾉ*:･ﾟ✧",
"(ﾉ≧∀≦)ﾉ",
"(ﾉ^ヮ^)ﾉ*:・ﾟ✧",
"(/ ‘з’)/",
"(۶ꈨຶꎁꈨຶ )۶ʸᵉᵃʰᵎ",
"⁽(◍˃̵͈̑ᴗ˂̵͈̑)⁽",
"(╯✧∇✧)╯",
"Σ(ノ°▽°)ノ",
"( ƅ°ਉ°)ƅ",
"ヽ(　･∀･)ﾉ",
"˭̡̞(◞⁎˃ᆺ˂)◞*✰",
"(p^-^)p",
"(ﾉ^∇^)ﾉﾟ",
"ヽ(〃･ω･)ﾉ",
"(۶* ‘ꆚ’)۶”",
"（。＞ω＜）。",
"（ﾉ｡≧◇≦）ﾉ",
"ヾ(｡･ω･)ｼ",
"(ﾉ･д･)ﾉ",
".+:｡(ﾉ･ω･)ﾉﾞ",
"Σ(*ﾉ´>ω<｡`)ﾉ",
"ヾ（〃＾∇＾）ﾉ♪",
".ﾟ☆(ノё∀ё)ノ☆ﾟ.",
"ヽ(;^o^ヽ)",
"╰(✧∇✧╰)",
"٩(◕ั ∀◕ั๑٩)",
"٩(•౪•٩)三",
"₍•͟ ͜ • ₎",
"q(^-^q)",
"＼（・c＿・●）ゞ",
"۹⌤_⌤۹",
"ヾ(０∀０*★)ﾟ*･.｡",
"ヾ│・ェ・ヾ│",
"╰(・∇・╰)",
"。（＞ω＜。）",
"ヾ(･ω･｡)ｼ",
"ヾ(･д･ヾ)",
"ヽ(´∀｀ヽ)",
"ヽ(´ω｀○)ﾉ.+ﾟ*｡:ﾟ+",
"ヾ(≧∇≦*)ゝ",
"＼（＠￣∇￣＠）／",
"＼(^▽^＠)ノ",
"ヾ(@^▽^@)ノ",
"(((＼（＠v＠）／)))",
"＼(*T▽T*)／",
"＼（＾▽＾）／",
"＼（Ｔ∇Ｔ）／",
"ヽ( ★ω★)ノ",
"ヽ(；▽；)ノ",
"ヾ(。◕ฺ∀◕ฺ)ノ",
"ヾ(＠† ▽ †＠）ノ",
"ヾ(＠^∇^＠)ノ",
"ヾ(＠^▽^＠)ﾉ",
"ヾ（＠＾▽＾＠）ノ",
"ヾ(＠゜▽゜＠）ノ",
"ヾ(@°▽°@)ノ",
"ヾ(＠°▽°＠)ﾉ",
"ヽ(*≧ω≦)ﾉ",
"ヽ(*⌒∇⌒*)ﾉ",
"ヽ(^。^)丿",
"ヽ(＾Д＾)ﾉ",
"ヽ(=^･ω･^=)丿",
"⸂⸂⸜(രᴗര๑)⸝⸃⸃",
"⸜(ّᶿധّᶿ)⸝",
"ヽ(｡･ω･｡)ﾉ",
"╰(‘ω’ )╯",
"╰(°ㅂ°)╯",
"┗(＾∀＾)┛",
"ヾ(๑’౪`๑)ﾉﾞ",
"ヾ(*Őฺ∀Őฺ*)ﾉ",
"╰(✧∇✧)╯",
"ヾ(๑⃙⃘´ꇴ｀๑⃙⃘)ﾉ",
"✯⸜(ّᶿ̷ധّᶿ̷)⸝✯",
"◦°˚\(´°౪°`)/˚°◦",
"\(-ㅂ-)/",
"◦°˚\(*❛‿❛)/˚°◦",
"╰(◉ᾥ◉)╯",
"⌒°(ᴖ◡ᴖ)°⌒",
"ヾ(´∀｀○)ﾉ",
"｡ﾟ✶ฺ.ヽ(*´∀`*)ﾉ.✶ฺﾟ｡",
"＼(;ﾟ∇ﾟ)/",
"ヽ(*´∀`)ﾉﾞ",
"⸂⸂⸜(ೆ௰ೆ๑)⸝⸃⸃",
"✧⁺⸜(●′▾‵●)⸝⁺✧",
"ヾ(`ω`　)/",
"◦°˚\☻/˚°◦",
"ヾ(｡^ω^｡)ノ",
"⸜(ّᶿॕധّᶿॕ)⸝",
"⸜(ؔᶿധؔᶿ)⸝",
"╰( ･ ᗜ ･ )╯",
"┏○ ＼(ﾟ 0ﾟ ;)/┓",
"  ヽ(^◇^*)/",
"ヾ(≧∇≦)ゞ",
"o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮(^ ਊ ^)╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡",
"☆*~ﾟ⌒(‘-‘*)⌒ﾟ~*☆",
"ヽ(ﾟ∀ﾟ)ﾉ",
"ヾ(o≧∀≦o)ﾉﾞ",
".｡ﾟ+.ヽ| ゝ∀・*|ﾉ｡+.ﾟ",
"(ﾟ<|＼(･ω･)／|>ﾟ)",
"╰| ° ◞౪◟ ° |╯",
"ヽ༼>ل͜<༽ﾉ",
"ヽ[ヘ ل͟ ヘ]╯",
"＼(・ω・)/",
"ヽ（゜ω゜○）ノ",
"☆~~ヾ(>▽<)ﾉ｡･☆",
"＼（*´･∀･｀*）／",
"＼（゜э゜）／",
"ヾ(￣◇￣)ノ",
"ヾ【*≧д≦】ノ",
"ヽ(^O^)ノ",
"ヾ(´▽｀*)ﾉ☆",
"ヾ(・∀・｀*)ﾉ☆",
"☆ヾ(*´▽｀)ﾉ",
"☆ヾ(*´・∀・)ﾉ",
"ヾ(*・ω・)ノ",
"ヾ(・ω・*)ノ",
"ヽ( ´￢`)ﾉ",
"ヾ(≧∪≦*)ノ〃",
"ヾ(*ゝω・*)ノ",
"＼（○＾ω＾○）／",
"╰(*´︶`*)╯",
"ヽ( ´ー`)ノ",
"┝＼( ‘∇^*)^☆／┥",
"ヽ(^o^)丿",
"┗|⌒O⌒|┛",
"┗|・o・|┛",
"ヾ(●・◇・●)ノ",
"ヽ( ‘ω’ )ﾉ",
"((ヾ(* ´∀｀)ノ))",
"ヽ(´∇｀)ﾉ",
"･:*+.\(( °ω° ))/.:+",
"ヽ(^□^｡)ノ",
"ヾ(o✪‿✪o)ｼ",
"＼(*ﾟ∀ﾟ*)／",
"＼(*^￢^*)／",
"Ψ(≧ω≦)Ψ",
"ヽ(*≧л≦)ﾉ",
"*。ヾ(｡>ｖ<｡)ﾉﾞ*。",
"҉*\( ‘ω’ )/*҉",
"(* >ω<)",
"(*≧▽≦)",
"(๑>ᴗ<๑)",
"( ˃̶ω˂̶ ૃ)",
"(٭°̧̧̧ω°̧̧̧٭)",
"⸍⚙̥ꇴ⚙̥⸌",
"(⊙ꇴ⊙)",
"(*≧∀≦*)",
"(≧∇≦*)",
"（๑✧∀✧๑）",
"(★^O^★)",
"(ᗒᗨᗕ)",
"(⌯꒪͒ ꌂ̇ ꒪͒)",
"(≧∀≦)",
"(⌬̀⌄⌬́)",
"₊·*◟(˶╹̆ꇴ╹̆˵)◜‧*･",
"(ᗒᏬᗕ) ˡ̵˖✮⃛",
"(ؑ⸍⸍ᵕؑ̇⸍⸍)◞✧",
"✮⃛( ◞´•௰•`)✮⃛",
"(ؑᵒᵕؑ̇ᵒ)◞✧",
"₍₍ ◝(●˙꒳˙●)◜ ₎₎",
"(´｡✪ω✪｡｀)",
"｡;+*(★`∪´☆)*+;｡",
"(๑˃̶͈̀o˂̶͈́๑)",
"≧ω≦",
"٩(^ᴗ^)۶",
"٩(๑꒦ິȏ꒦ິ๑)۶",
"٩(●˙▿˙●)۶…⋆ฺ",
"٩(๑ơలơ)۶♡",
"୧(﹒︠ᴗ﹒︡)୨",
"٩(ó｡ò۶ ♡)))♬",
"ε٩( ºωº )۶з",
"٩(๑òωó๑)۶",
"٩( ๑^ ꇴ^)۶",
"٩(๑˃́ꇴ˂̀๑)۶",
"٩(๑∂▿∂๑)۶♡",
"٩(♡ε♡ )۶",
"۹(ÒہÓ)۶",
"٩(⚙ȏ⚙)۶",
"٩(✿∂‿∂✿)۶",
"୧⍢⃝୨",
"⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾",
"(୨৩́ಐ৩̀੧)",
"٩(;ʘ¿ʘ;)۶",
"=。:.ﾟ٩(๑>ω<๑)۶:.｡+ﾟ",
"٩(˘◊˘)۶",
"٩(*ゝڡゝ๑)۶♥",
"٩(｡θᗨθ｡)۶",
"٩(⚙ᴗ⚙)۶",
"୧(˃◡ु˂)୨",
"۹(˒௰˓)۶",
"٩(●ᴗ●)۶",
"♡〜٩( ˃́▿˂̀ )۶〜♡",
"٩(º౪º๑)۶",
"=。:.ﾟ٩(๑>◊<๑)۶:.｡+ﾟ",
"٩(๑❛ᴗ❛๑)۶",
"୧| ͡ᵔ ﹏ ͡ᵔ |୨",
"୧〳 ” ʘ̆ ᗜ ʘ̆ ” 〵୨",
"٩(๑❛ʚ❛๑)۶",
"٩(இ ⌓ இ๑)۶",
"୧| ” •̀ ل͜ •́ ” |୨",
"୧( , ＾ 〰 ＾ , )୨",
"٩| ര ‿ ര |╯",
"୧〳 ＾ ౪ ＾ 〵୨",
"୧( ˵ ° ~ ° ˵ )୨",
"୧། ☉ ౪ ☉ །୨",
"୧༼ ヘ ᗜ ヘ ༽୨",
"❣࿌ིྀ྇°˚࿅୧( ॑ധ ॑)୨࿅˳०࿌ིྀ྇",
"٩(◦`꒳´◦)۶",
"٩(๑˃̌ۿ˂̌๑)۶",
"٩(θ‿θ)۶",
"(⁼̴̀ૢ꒳​⁼̴́ૢ๑)",
"ෆු(*˃ர்˂*)ෆු",
"(ٛɲ˃ ˑ̣̮ ˂ٛɳ)",
"d(๑꒪່౪̮꒪່๑)b",
"( ˃̆ૢ௰˂̆ૢഃ )",
"ლ(*꒪ヮ꒪*)ლ",
"૮(ᶿ̴͈᷇ॢ௰ᶿ̴͈᷆ॢ)ა✧",
"∗˚(* ˃̤൬˂̤ *)˚∗",
"б（＞ε＜）∂",
"∩|*`・ρ・´|∩",
"(gΦ皿Φ)g〃 ",
"о(ж＞▽＜)ｙ ☆",
"*＼( *ω*)┓",
"โ๏∀๏ใ",
"癶(癶✺౪✺ )癶",
"⊂((〃≧▽≦〃))⊃",
"~(≧◇≦)/ﾞﾞﾞﾞ",
"(*•̀ᴗ•́*)و ̑̑",
"╭( ･ㅂ･)و ̑̑",
"(๑•̀ㅂ•́)و",
"(๑˃̵ᴗ˂̵)و",
"╭( ･ㅂ･)و",
"( •̀ᄇ• ́)ﻭ✧",
"(ര̀ᴗര́)و ̑̑",
"╭(♡･ㅂ･)و ̑̑",
"◝( ′ㅂ`)و ̑̑",
"╭( ･ㅂ･)و ̑̑ ＂",
"╭( ･ㅂ･)و )))",
"╭(๑ ॔ㅂ ਂ ॓)و ̑̑",
"( ⁼̴̤̆ ළ̉ ⁼̴̤̆)و ̑̑",
"(๑˃̵ᴗ˂̵)و",
" (๑•̀ㅂ•́)و✧",
"꒰๑͒•̀ुꇵ͒•꒱و ̑̑",
"ଘ꒰ ๑ ˃̶ ᴗ ᵒ̴̶̷๑꒱و ̑̑",
"(ฅ⁍̴̀◊⁍̴́)و ̑̑",
"╭( ･ㅂ･)و ̑̑ ˂ᵒ͜͡ᵏᵎ⁾✩",
"(•́⌄•́๑)૭✧",
"(•̀ᴗ•́)൬༉",
"!(•̀ᴗ•́)و ̑̑",
"٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ",
"ೕ(`･୰･´)",
"ೕ(･ㅂ･ )",
"ೕ(•̀ᴗ•́)",
"٩(ര̀ᴗര́)",
"ೕ(˃̵ᴗ˂̵ ๑)",
"ೕ(•̀ㅂ•́ )",
"✧٩(•́⌄•́๑)",
"ೕ(⁍̴̀◊⁍̴́ฅ)",
"٩(｡•ω•｡)و",
"٩(⸝⸝⸝◕ั ௰ ◕ั⸝⸝⸝ )و",
"٩(✪ꀾ⍟༶)و",
"୧( ⁼̴̶̤̀ω⁼̴̶̤́ )૭",
"٩(˃̶͈̀௰˂̶͈́)و",
"٩( ‘ω’ )و",
"٩(｡•ㅅ•｡)و",
"٩( ´･ш･)و",
"٩(•̤̀ᵕ•̤́๑)૭✧",
"ː̗̀٩꒰ꋃ꒱وː̖́",
"٩(๑❛ワ❛๑)و",
"(۶•̀ᴗ•́)۶",
"٩( ᐛ )و",
"✧٩(•́⌄•́๑)و ✧",
"ೕ(`･୰･´)و ̑̑",
"٩(๑•̀ㅂ•́)و",
"٩(๑˃̵ᴗ˂̵)و",
"(((ೕ( ･ㅂ･)و )))",
"٩( ′ㅂ`)و ̑̑",
"٩(ˊᗜˋ*)و",
"(و ˃̵ᴗ˂̵)و",
"(ง ͡ʘ ͜ʖ ͡ʘ)ง",
"(ง ͠ ͠° ل͜ °)ง",
]

RUNS_STR = [
    "Runs to Thanos..",
    "Runs far, far away from earth..",
    "Running faster than Bolt coz i'mma userbot !!",
    "Runs to Marie..",
    "This Group is too cancerous to deal with.",
    "Cya bois",
    "Kys",
    "I go away",
    "I am just walking off, coz me is too fat.",
    "I Fugged off!",
    "Will run for chocolate.",
    "I run because I really like food.",
    "Running...\nbecause dieting is not an option.",
    "Wicked fast runnah",
    "If you wanna catch me, you got to be fast...\nIf you wanna stay with me, you got to be good...\nBut if you wanna pass me...\nYou've got to be kidding.",
    "Anyone can run a hundred meters, it's the next forty-two thousand and two hundred that count.",
    "Why are all these people following me?",
    "Are the kids still chasing me?",
    "Running a marathon...there's an app for that.",
]

CHASE_STR = [
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "`Get back here!`",
    "`Not so fast...`",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "`Jokes on you, I'm everywhere`",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "`Go bother someone else, no-one here cares.`",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]

HELLOSTR = [
    "Hi !",
    "‘Ello, gov'nor!",
    "What’s crackin’?",
    "Howdy, howdy ,howdy!",
    "Hello, who's there, I'm talking.",
    "You know who this is.",
    "Yo!",
    "Whaddup.",
    "Greetings and salutations!",
    "Hello, sunshine!",
    "`Hey, howdy, hi!`",
    "What’s kickin’, little chicken?",
    "Peek-a-boo!",
    "Howdy-doody!",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`I come for peace!`",
    "Ahoy, matey!",
    "`Hi !`",
]

PROSTR = [
    "`You is pro user.`",
     "`Pros here -_- Time to Leave`",
     "`Pros everywhere`",
     "`Pro Pro Pro ; What a tragedy`",
]

NUBSTR = [
    "`Haha noob trying to act pro`",
    "`Hi Nub what'sup`",
    "`Only i and you know that you are a noob and trying to act like pro`",
    "`Sorry we don't appoint noobs`",
    "`Bot rule 420 section 69 prevents me from replying to stupid nubfuks like you.`",
]

BYESTR = [
    "`Nice talking with you`",
    "`I've gotta go!`",
    "`I've gotta run!`",
    "`I've gotta split`",
    "`I'm off!`",
    "`Great to see you,bye`",
    "`See you soon`",
    "`Farewell!`",
]

GDNIGHT = [
    "`Good night keep your dreams alive`",
    "`Night, night, to a dear friend! May you sleep well!`",
    "`May the night fill with stars for you. May counting every one, give you contentment!`",
    "`Wishing you comfort, happiness, and a good night’s sleep!`",
    "`Now relax. The day is over. You did your best. And tomorrow you’ll do better. Good Night!`",
    "`Good night to a friend who is the best! Get your forty winks!`",
    "`May your pillow be soft, and your rest be long! Good night, friend!`",
    "`Let there be no troubles, dear friend! Have a Good Night!`",
    "`Rest soundly tonight, friend!`",
    "`Have the best night’s sleep, friend! Sleep well!`",
    "`Have a very, good night, friend! You are wonderful!`",
    "`Relaxation is in order for you! Good night, friend!`",
    "`Good night. May you have sweet dreams tonight.`",
    "`Sleep well, dear friend and have sweet dreams.`",
    "`As we wait for a brand new day, good night and have beautiful dreams.`",
    "`Dear friend, I wish you a night of peace and bliss. Good night.`",
    "`Darkness cannot last forever. Keep the hope alive. Good night.`",
    "`By hook or crook you shall have sweet dreams tonight. Have a good night, buddy!`",
    "`Good night, my friend. I pray that the good Lord watches over you as you sleep. Sweet dreams.`",
    "`Good night, friend! May you be filled with tranquility!`",
    "`Wishing you a calm night, friend! I hope it is good!`",
    "`Wishing you a night where you can recharge for tomorrow!`",
    "`Slumber tonight, good friend, and feel well rested, tomorrow!`",
    "`Wishing my good friend relief from a hard day’s work! Good Night!`",
    "`Good night, friend! May you have silence for sleep!`",
    "`Sleep tonight, friend and be well! Know that you have done your very best today, and that you will do your very best, tomorrow!`",
    "`Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow!`",
    "`Friend, I want to remind you that your strong mind has brought you peace, before. May it do that again, tonight! May you hold acknowledgment of this with you!`",
    "`Wishing you a calm, night, friend! Hoping everything winds down to your liking and that the following day meets your standards!`",
    "`May the darkness of the night cloak you in a sleep that is sound and good! Dear friend, may this feeling carry you through the next day!`",
    "`Friend, may the quietude you experience tonight move you to have many more nights like it! May you find your peace and hold on to it!`",
    "`May there be no activity for you tonight, friend! May the rest that you have coming to you arrive swiftly! May the activity that you do tomorrow match your pace and be all of your own making!`",
    "`When the day is done, friend, may you know that you have done well! When you sleep tonight, friend, may you view all the you hope for, tomorrow!`",
    "`When everything is brought to a standstill, friend, I hope that your thoughts are good, as you drift to sleep! May those thoughts remain with you, during all of your days!`",
    "`Every day, you encourage me to do new things, friend! May tonight’s rest bring a new day that overflows with courage and exciting events!`",
]

GDMORNING = [
    "`Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning!`",
    "`It doesn’t matter how bad was your yesterday. Today, you are going to make it a good one. Wishing you a good morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good morning!`",
    "`May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!`",
    "`May the sun shower you with blessings and prosperity in the days ahead. Good morning!`",
    "`Every sunrise marks the rise of life over death, hope over despair and happiness over suffering. Wishing you a very enjoyable morning today!`",
    "`Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time!`",
    "`Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today. Wishing you a very good morning!`",
    "`You have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning! Good morning to you!`",
    "`Waking up in such a beautiful morning is a guaranty for a day that’s beyond amazing. I hope you’ll make the best of it. Good morning!`",
    "`Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile. Good morning! Wishing you a great day.`",
    "`Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. Wishing you a wonderful morning!`",
    "`Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning!`",
    "`A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!`",
    "`The darkness of night has ended. A new sun is up there to guide you towards a life so bright and blissful. Good morning dear!`",
    "`Wake up, have your cup of morning tea and let the morning wind freshen you up like a happiness pill. Wishing you a good morning and a good day ahead!`",
    "`Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning! Have a wonderful day ahead.`",
    "`A bad day will always have a good morning, hope all your worries are gone and everything you wish could find a place. Good morning!`",
    "`A great end may not be decided but a good creative beginning can be planned and achieved. Good morning, have a productive day!`",
    "`Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your “Good Morning” have a nice day!`",
    "`Anything can go wrong in the day but the morning has to be beautiful, so I am making sure your morning starts beautiful. Good morning!`",
    "`Open your eyes with a smile, pray and thank god that you are waking up to a new beginning. Good morning!`",
    "`Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning.`",
    "`Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good Morning!`",
    "`Birds are singing sweet melodies and a gentle breeze is blowing through the trees, what a perfect morning to wake you up. Good morning!`",
    "`This morning is so relaxing and beautiful that I really don’t want you to miss it in any way. So, wake up dear friend. A hearty good morning to you!`",
    "`Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning!`",
    "`Every morning brings you new hopes and new opportunities. Don’t miss any one of them while you’re sleeping. Good morning!`",
    "`Start your day with solid determination and great attitude. You’re going to have a good day today. Good morning my friend!`",
    "`Friendship is what makes life worth living. I want to thank you for being such a special friend of mine. Good morning to you!`",
    "`A friend like you is pretty hard to come by in life. I must consider myself lucky enough to have you. Good morning. Wish you an amazing day ahead!`",
    "`The more you count yourself as blessed, the more blessed you will be. Thank God for this beautiful morning and let friendship and love prevail this morning.`",
    "`Wake up and sip a cup of loving friendship. Eat your heart out from a plate of hope. To top it up, a fork full of kindness and love. Enough for a happy good morning!`",
    "`It is easy to imagine the world coming to an end. But it is difficult to imagine spending a day without my friends. Good morning.`",
]    
SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]

SLAP_TEMPLATES = [
    "{hits} {victim} with a {item}.",
    "{hits} {victim} in the face with a {item}.",
    "{hits} {victim} around a bit with a {item}.",
    "`{throws} a {item} at {victim}.`",
    "grabs a {item} and {throws} it at {victim}'s face.",
    "{hits} a {item} at {victim}.", "{throws} a few {item} at {victim}.",
    "grabs a {item} and {throws} it in {victim}'s face.",
    "launches a {item} in {victim}'s general direction.",
    "sits on {victim}'s face while slamming a {item} {where}.",
    "starts slapping {victim} silly with a {item}.",
    "pins {victim} down and repeatedly {hits} them with a {item}.",
    "grabs up a {item} and {hits} {victim} with it.",
    "starts slapping {victim} silly with a {item}.",
    "holds {victim} down and repeatedly {hits} them with a {item}.",
    "prods {victim} with a {item}.",
    "picks up a {item} and {hits} {victim} with it.",
    "`ties {victim} to a chair and {throws} a {item} at them.`",
    "{hits} {victim} {where} with a {item}.",
    "ties {victim} to a pole and whips them {where} with a {item}."
    "gave a friendly push to help {victim} learn to swim in lava.",
    "sent {victim} to /dev/null.", "sent {victim} down the memory hole.",
    "beheaded {victim}.", "threw {victim} off a building.",
    "replaced all of {victim}'s music with Nickelback.",
    "spammed {victim}'s email.", "made {victim} a knuckle sandwich.",
    "slapped {victim} with pure nothing.",
    "hit {victim} with a small, interstellar spaceship.",
    "quickscoped {victim}.", "put {victim} in check-mate.",
    "RSA-encrypted {victim} and deleted the private key.",
    "put {victim} in the friendzone.",
    "slaps {victim} with a DMCA takedown request!"
]

ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "pair of trousers",
    "CRT monitor",
    "diamond sword",
    "baguette",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "mau5head",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "cobblestone block",
    "lava bucket",
    "rubber chicken",
    "spiked bat",
    "gold block",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
]

WHERE = ["in the chest", "on the head", "on the butt", "on the crotch"]

# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^:/$", ignore_unsafe=True)
async def kek(keks):
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(outgoing=True, pattern=r"^.coinflip (.*)")
async def coin(event):
    r = choice(["heads", "tails"])
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r == "heads":
        if input_str == "heads":
            await event.edit(
                "The coin landed on: **Heads**.\nYou were correct.")
        elif input_str == "tails":
            await event.edit(
                "The coin landed on: **Heads**.\nYou weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Heads**.")
    elif r == "tails":
        if input_str == "tails":
            await event.edit(
                "The coin landed on: **Tails**.\nYou were correct.")
        elif input_str == "heads":
            await event.edit(
                "The coin landed on: **Tails**.\nYou weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Tails**.")


@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    """ slaps a user, or get slapped if not a reply. """
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = choice(SLAP_TEMPLATES)
    item = choice(ITEMS)
    hit = choice(HIT)
    throw = choice(THROW)
    where = choice(WHERE)

    caption = "..." + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw, where=where)

    return caption


@register(outgoing=True, pattern="^-_-$", ignore_unsafe=True)
async def lol(lel):
    """ Ok... """
    okay = "-_-"
    for i in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern="^.(yes|no|maybe|decide)$")
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id if event.reply_to_msg_id else None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get(f"https://yesno.wtf/api").json()
    await event.delete()
    await event.client.send_message(event.chat_id,
                                    str(r["answer"]).upper(),
                                    reply_to=message_id,
                                    file=r["image"])


@register(outgoing=True, pattern="^;_;$", ignore_unsafe=True)
async def fun(e):
    t = ";_;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await e.edit("🤦‍♂")


@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    """ y u du dis, i cry everytime !! """
    await e.edit(choice(CRI))

                      
@register(outgoing=True, pattern="^.smile$")
async def smile(e):
    """ show your smile !! """
    await e.edit(choice(SMILE))


@register(outgoing=True, pattern="^.insult$")
async def insult(e):
    """ I make you cry !! """
    await e.edit(choice(INSULT_STRINGS))


@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
        return

    reply_text = choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
        return

    count = randint(3, 10)
    reply_text = sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count),
                     message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await zgfy.edit(
            "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            textz = randint(0, 2)

            if textz == 0:
                charac = charac.strip() + \
                    choice(ZALG_LIST[0]).strip()
            elif textz == 1:
                charac = charac.strip() + \
                    choice(ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + \
                    choice(ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern="^.hi$")
async def hoi(hello):
    """ Greet everyone! """
    await hello.edit(choice(HELLOSTR))
                      
                      
@register(outgoing=True, pattern="^.gn$")
async def night(night):
    """ Greet everyone! """
    await night.edit(choice(GDNIGHT))

@register(outgoing=True, pattern="^.congo$")
async def congo(congo):
    """ Greet everyone! """
    await congo.edit(choice(CONGOSTR))    
                      
                      
@register(outgoing=True, pattern="^.gm$")
async def morning(morning):
    """ Greet everyone! """
    await morning.edit(choice(GDMORNING))

@register(outgoing=True, pattern="^.gnoon$")
async def noon(noon):
    """ Greet everyone! """
    await noon.edit(choice(GDNOON))    


@register(outgoing=True, pattern="^.pro$")
async def pero(proo):
    """ Greet everyone! """
    await proo.edit(choice(PROSTR))


@register(outgoing=True, pattern="^.nub$")
async def noob(nubdo):
    """ Greet everyone! """
    await nubdo.edit(choice(NUBSTR))
                      
@register(outgoing=True, pattern="^.bye$")
async def bhago(bhagobc):
    """ Greet everyone! """
    await bhagobc.edit(choice(BYESTR))

@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await owo.edit("` UwU no text given! `")
        return

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern="^.chase$")
async def police(chase):
    """ Run boi run, i'm gonna catch you !! """
    await chase.edit(choice(CHASE_STR))


@register(outgoing=True, pattern="^.run$")
async def runner_lol(run):
    """ Run, run, RUNNN! """
    await run.edit(choice(RUNS_STR))


@register(outgoing=True, pattern="^.metoo$")
async def metoo(hahayes):
    """ Haha yes """
    await hahayes.edit(choice(METOOSTR))


@register(outgoing=True, pattern="^.oof$")
async def Oof(e):
    t = "Oof"
    for j in range(16):
        t = t[:-1] + "of"
        await e.edit(t)

                      
@register(outgoing=True, pattern="^.oem$")
async def Oem(e):
    t = "Oem"
    for j in range(16):
        t = t[:-1] + "em"
        await e.edit(t)

@register(outgoing=True, pattern="^.10iq$")
async def iqless(e):
    await e.edit("you low iq idiot")


@register(outgoing=True, pattern="^.moon$")
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.clock$")
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
        return

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await memereview.edit("`Hah, I don't clap pointlessly!`")
        return
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern="^.bt$")
async def bluetext(bt_e):
    """ Believe me, you will find this useful. """
    if await bt_e.get_reply_message() and bt_e.is_group:
        await bt_e.edit(
            "/BLUETEXT /MUST /CLICK.\n"
            "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?")


@register(outgoing=True, pattern=r"^.f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
        paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
        paytext * 2, paytext * 2)
    await event.edit(pay)


@register(outgoing=True, pattern="^.gi (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Here you are, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


#@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
#async def scam(event):
   # """ Just a small command to fake chat actions for fun !! """
   # options = [
      #  'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
     #   'photo', 'document', 'cancel'
    #]
   # input_str = event.pattern_match.group(1)
  #  args = input_str.split()
   # if len(args) is 0:  # Let bot decide action and time
        #scam_action = choice(options)
       # scam_time = randint(30, 60)
    #elif len(args) is 1:  # User decides time/action, bot decides the other.
        #try:
         #   scam_action = str(args[0]).lower()
        #    scam_time = randint(30, 60)
       # except ValueError:
      #      scam_action = choice(options)
     #       scam_time = int(args[0])
    #elif len(args) is 2:  # User decides both action and time
      #  scam_action = str(args[0]).lower()
     #   scam_time = int(args[1])
    #else:
      #  await event.edit("`Invalid Syntax !!`")
     #   return
    #try:
        #if (scam_time > 0):
       #     await event.delete()
      #      async with event.client.action(event.chat_id, scam_action):
     #           await sleep(scam_time)
    #except BaseException:
       # return
                      


@register(pattern=r".type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await typew.edit("`Give a text to type!`")
        return
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)
                      

      
                      
@register(outgoing=True, pattern="^.lols$")
async def lol(e):
    await e.edit("😂\n😂\n😂\n😂\n😂😂😂😂\n\n   😂😂😂\n 😂         😂\n😂           😂\n 😂         😂\n   😂😂😂\n\n😂\n😂\n😂\n😂\n😂😂😂😂")
                      
@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ Just a small command to fake chat actions for fun !! """
    options = [
        'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
        'photo', 'document', 'cancel'
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:  # Let bot decide action and time
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:  # User decides time/action, bot decides the other.
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:  # User decides both action and time
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Invalid Syntax !!`")
        return
    try:
        if (scam_time > 0):
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return

@register(outgoing=True, pattern="^.fail$")  
async def fail(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `" 
                     "`\n████▌▄▌▄▐▐▌█████ `"    
                     "`\n████▌▄▌▄▐▐▌▀████ `"       
                     "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `")    


@register(outgoing=True, pattern="^.lol$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `" 
                     "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"       
                     "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `" 
                     "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `") 
 
 
                                                                                   
@register(outgoing=True, pattern="^.lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")
                     

@register(outgoing=True, pattern="^.stfu$")
async def stfu(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n██████████████████████████████`"
                     "`\n██▀▀▀▀████▀▀▀▀████▀▀▀▀▀███▀▀██▀▀█`"
                     "`\n█──────██──────██───────██──██──█`"
                     "`\n█──██▄▄████──████──███▄▄██──██──█`"
                     "`\n█▄────▀████──████────█████──██──█`"
                     "`\n█▀▀██──████──████──███████──██──█`"        
                     "`\n█──────████──████──███████──────█`"      
                     "`\n██▄▄▄▄█████▄▄████▄▄████████▄▄▄▄██`"    
                     "`\n█████████████████████████████████`")    


@register(outgoing=True, pattern="^.nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n(\_/)`"
                     "`\n(●_●)`"
                     "`\n />🌹 *This is for you`"
                     "`\n                    `"
                     "`\n(\_/)`"
                     "`\n(●_●)`"
                     "`\n🌹<\  *Now give it back`")


@register(outgoing=True, pattern="^.fag$")  
async def gtfo(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n█████████`" 
                     "`\n█▄█████▄█`"    
                     "`\n█▼▼▼▼▼`"       
                     "`\n█       STFU FAGGOT'S`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                    "`\n ██   ██`")               


@register(outgoing=True, pattern="^.taco$")  
async def taco(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n{\__/}"
                     "\n(●_●)"
                     "\n( >🌮 Want a taco?")


@register(outgoing=True, pattern="^.sayhi$")
async def sayhi(e):
    await e.edit(
        "\n💰💰💰💰💰💰💰💰💰💰💰💰"
        "\n💰🔷💰💰💰🔷💰💰🔷🔷🔷💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷🔷🔷🔷🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰🔷🔷🔷💰"
        "\n💰💰💰💰💰💰💰💰💰💰💰💰")
       
                  
@register(outgoing=True, pattern="^.gey$")            
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈NIGGA U GEY`"
                    "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")    


@register(outgoing=True, pattern="^.gay$")            
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈BAPAQ U GAY`"
                    "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")    


@register(outgoing=True, pattern="^.bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")


@register(outgoing=True, pattern="^.hey$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")


@register(outgoing=True, pattern="^.nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
                     "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
                     "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
"`\n┗━━┻━┛`")      
                      
                      
@register(outgoing=True, pattern="^.rain$")
async def rain(event):
    deq = deque(list("☀️🌤⛅️🌥☁️🌧⛈"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return
                      
@register(outgoing=True, pattern="^.love$")
async def love(event):
    deq = deque(list("❤️🧡💛💚💙💜🖤💕💞💓💗💖💘💝"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return

@register(outgoing=True, pattern="^.shout(?: |$)(.*)")
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(' '.join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + ' ' + '  ' * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await args.edit("`"+msg+"`")        

@register(outgoing=True, pattern="^.bigoof$")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,7)
    #input_str = event.pattern_match.group(1)
   # if input_str == "nope":
    await event.edit("┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛")
    animation_chars = [
            "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
            "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
            "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])        

CMD_HELP.update({
    "memes":
    "`.cowsay`\
\nUsage: cow which says things.\
\n\n`:/`\
\nUsage: Check yourself ;)\
\n\n`-_-`\
\nUsage: Ok...\
\n\n`;_;`\
\nUsage: Like `-_-` but crying.\
\n\n`.earth`\
\nusage:type .earth\
\n\n`.cp`\
\nUsage: Copypasta the famous meme\
\n\n`.vapor`\
\nUsage: Vaporize everything!\
\n\n`.str`\
\nUsage: Stretch it.\
\n\n`.10iq`\
\nUsage: You retard !!\
\n\n`.zal`\
\nUsage: Invoke the feeling of chaos.\
\n\n`.oem`\
\nUsage: Oeeeem\
\n\n.oof or .bigoof\
\nUsage: Ooooof\
\n\n`.fp`\
\nUsage: Facepalm :P\
\n\n`.moon`\
\nUsage: kensar moon animation.\
\n\n`.clock`\
\nUsage: kensar clock animation.\
\n\n`.hi`\
\nUsage: Greet everyone!\
\n\n`.coinflip` <heads/tails>\
\nUsage: Flip a coin !!\
\n\n`.owo`\
\nUsage: UwU\
\n\n`.pro` or `.nub` or `.bye`\
\nUsage: see it yourself\
\n\n`.react`\
\nUsage: Make your userbot react to everything.\
\n\n`.slap`\
\nUsage: reply to slap them with random objects !!\
\n\n`.cry`\
\nUsage: y u du dis, i cri.\
\n\n`.smile`\
\nUsage: show your smile.\
\n\n`.shg`\
\nUsage: Shrug at it !!\
\n\n`.run`\
\nUsage: Let Me Run, run, RUNNN!\
\n\n`.chase`\
\nUsage: You better start running\
\n\n`.metoo`\
\nUsage: Haha yes\
\n\n`.gn` or `.gm` or `.gnoon`\
\nUsage: Says goodnight and  godmorning\
\n\n`.mock`\
\nUsage: Do it and find the real fun.\
\n\n Memefied contains<`.love`, `.nou`, `.hey`, `.gey`, `.gay`, `.bot`,\n`.sayhi`, `.taco`, `.fag`, `.nih`, `.stfu`, `.lool`, `.lol`, `.fail`, `.lols`>\
\n\nUsage: Enjoiii\
\n\n`.clap` or `.congo`\
\nUsage: Praise people!\
\n\n`.f` <emoji/character>\
\nUsage: Pay Respects.\
\n\n`.bt`\
\nUsage: Believe me, you will find this useful.\
\n\n`.type` or `.shout` <text>\
\nUsage: Just a small command to make your keyboard become a typewriter!\
\n\n`.gi` <query>\
\nUsage: Let me Google that for you real quick !!\
\n\n`.decide` [Alternates: (.yes, .no, .maybe)]\
\nUsage: Make a quick decision.\
\n\n`.scam` <action> <time>\
\n[Available Actions: (typing, contact, game, location, voice, round, video, photo, document, cancel)]\
\nUsage: Create fake chat actions, for fun. (Default action: typing)\
\n\n\nThanks to 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for some of these."
})
