# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="

@Client.on_message(filters.text & filters.command(["lyrics"]))
async def sng(bot, message):
    vj = await bot.ask(chat_id=message.from_user.id, text="Now send me your song name.")
    if vj.text:
        mee = await vj.reply_text("`Searching 🔎`")
        song = vj.text
        chat_id = message.from_user.id
        rpl = lyrics(song)
        await mee.delete()
        try:
            await mee.delete()
            await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("𝗠𝗼𝘃𝗶𝗲𝘀 𝗨𝗽𝗱𝗮𝘁𝗲 ", url = f"t.me/MoviesUpdate_07")]]))
        except Exception as e:                            
            await vj.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("𝗠𝗼𝘃𝗶𝗲𝘀 𝗨𝗽𝗱𝗮𝘁𝗲", url = f"t.me/MoviesUpdate_07")]]))
    else:
        await vj.reply_text("Send me only text Buddy.")


def search(song):
    r = requests.get(API + song)
    find = r.json()
    return find
       
def lyrics(song):
    fin = search(song)
    text = f'**🎶 Sᴜᴄᴄᴇꜱꜰᴜʟʟy Exᴛʀᴀᴄᴛᴇᴅ Lyɪʀɪᴄꜱ Oꜰ {song}**\n\n'
    text += f'`{fin["lyrics"]}`'
    text += '\n\n\n**Made By Artificial Intelligence**'
    return text



