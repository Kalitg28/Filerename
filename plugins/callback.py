from gc import callbacks

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client , filters
from script import *
from config import *





@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
    text = script.ABOUT_TXT.format(bot.me.mention)
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "home")]
                  ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin",url = "https://t.me/Kalitgadmin_Bot"),
        InlineKeyboardButton("✖️ Close",callback_data = "cancel") ]])
    await message.reply_text(text = text,reply_markup = keybord)    



@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["admin"]))
async def admincm(bot,message):
    text = script.ADMIN_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("✖️ Close ✖️",callback_data = "cancel") ]])
    await message.reply_text(text = text,reply_markup = keybord)    



@Client.on_callback_query(filters.regex('help'))
async def help(bot,update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keybord = InlineKeyboardMarkup([
                    [InlineKeyboardButton('⚙️ Admin', callback_data='admin')],
                    [InlineKeyboardButton('🏞 Thumbnail', callback_data='thumbnail'),
                    InlineKeyboardButton('✏ Caption', callback_data='caption')],
                    [InlineKeyboardButton('🏷️ Metadata', callback_data='metadata'),
                    InlineKeyboardButton('💵 Donate', callback_data='donate')],
                    [InlineKeyboardButton('🏠 Home', callback_data='home')]
                   ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_callback_query(filters.regex('thumbnail'))
async def thumbnail(bot,update):
    text = script.THUMBNAIL_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_callback_query(filters.regex('admin'))
async def admin(bot,update):
    text = script.ADMIN_TXT
    keybord = InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_callback_query(filters.regex('metadata'))
async def metadata(bot,update):
    text = script.METADATA_TXT
    keybord = InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_callback_query(filters.regex('caption'))
async def caption(bot,update):
    text = script.CAPTION_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('donate'))
async def donate(bot,update):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_callback_query(filters.regex('home'))
async def home_callback_handler(bot, query):
    text = f"""Hello {query.from_user.mention} \n\n➻ This Is An Advanced And Yet Powerful Rename Bot.\n\n➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.\n\n➻ You Can Also Convert Video To File Aɴᴅ File To Video.\n\n➻ This Bot Also Supports Custom Thumbnail And Custom Caption.\n\n<b>Bot Is Made By @TamilRockerz_TR</b>"""
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🦋 𝐓𝐚𝐦𝐢𝐥𝐑𝐨𝐜𝐤𝐞𝐫𝐳 𝐓𝐑 🦋", url="https://t.me/TamilRockerz_TR"),
                    InlineKeyboardButton("💬 Support", url="https://t.me/Kali_Botz_Support")],
                    [InlineKeyboardButton("🛠️ Help", callback_data='help'),
		            InlineKeyboardButton("❤️‍🩹 About", callback_data='about')],
                    [InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", url="https://t.me/Kalitgadmin_Bot")]
		  ])
    await query.message.edit_text(text=text, reply_markup=keybord)




