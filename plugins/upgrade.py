from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """**Free Plan User**
Daily  Upload limit 2GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 69  ind /🌎 1$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 169  ind /🌎 2.19$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 199  ind /🌎 3.16$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>9905665309@fam</code>
<b>➜ PayPal :</b> <a href='https://www.paypal.me/ibbs09'>Click Here</a>
<b>➜ QR Code :</b> <a href='https://telegra.ph/ScanPay-09-16'>Click Here</a>

After Payment Send Screenshots Of Payment To Admin @OnAnimeSeriesAdminbot"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/OnAnimeSeriesAdminbot"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
    text = """**Free Plan User**
**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 69  ind /🌎 1$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 169  ind /🌎 2.19$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 199  ind /🌎 3.16$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>9905665309@fam</code>
<b>➜ PayPal :</b> <a href='https://www.paypal.me/ibbs09'>Click Here</a>
<b>➜ QR Code :</b> <a href='https://telegra.ph/ScanPay-09-16'>Click Here</a>

After Payment Send Screenshots Of Payment To Admin @OnAnimeSeriesAdminbot"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/OnAnimeSeriesAdminbot"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)
    
	
