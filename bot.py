import pyrogram
from pyrogram import Client, idle
from datetime import datetime
from pytz import timezone
from plugins.cb_data import app as Client2
from config import *
import config
import pyromod
from datetime import datetime



# Set minimum chat and channel IDs
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

# Initialize the bot
bot = Client("Renamer", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))


class Bot(Client):
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = config.BOT_UPTIME

        print(f"\033[1;96m @{me.username} Sᴛᴀʀᴛᴇᴅ......⚡️⚡️⚡️\033[0m")

        # Notify admins
        try:
            for admin_id in config.ADMIN:
                await self.send_message(admin_id, f"**__{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
        except Exception as e:
            print(f"Failed to notify admins: {e}")

        # Log channel message
        if config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(config.LOG_CHANNEL,
                                        f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n"
                                        f"📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`")
            except Exception as e:
                print(f"Failed to send log message: {e}")


# Functionality when STRING_SESSION is provided
if STRING_SESSION:
    apps = [Client2, bot]
    for app in apps:
        app.start()
    idle()  # Keeps the program running until manually stopped
    for app in apps:
        app.stop()

else:
    bot.run()  # Automatically manages the start/stop lifecycle of the bot
