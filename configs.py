# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 25882792))
    API_HASH = os.getenv("API_HASH", "846699536cd018e1b55b7ea895156f08")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "kill")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001818441571))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "")
    BOT_OWNER = int(os.getenv("BOT_OWNER", 1534651884))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "Primeflix_Cinema")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", '''Hᴇʏ Bᴜᴅᴅʏ! 😃

I'ᴍ A Bᴏᴛ Fᴏʀ Sᴇɴᴅɪɴɢ Fʀᴏᴍ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ.😚

Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ.☺️

Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ Cʟɪᴄᴋ Oɴ Hᴇʟᴘ ✅''')
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/9fb99c91f6e887dbc4bd0.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", '''ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ,
ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Primeflix5557:Primeflix5557@cluster0.d0tnqb6.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001875916506"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "12334")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "365"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, i ᴅᴏ ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.✅ ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @Help_Primeflix_Cinema''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", '''Requirements to use bot inside group!
 Step 1 - Apko ek goup ki jarurat hogi, jisme member bhi ho, aur ek private channel ki jarurat hogi, jisme aapke saare post honge!

 Step 2 - Bot ko apne group aor channel ka admin bnana hoga.
                               
 Step 3 - group me "/request" type krke send krna hoga!
 fir bot ke owner apka ye request accept krr lenge. @yash_yadav99
                               
 Step 4 - Group me "/addb - private channel id" type kr ke send krna hoga.
 fir bot ke owner apka ye request accept krr lenge. @yash_yadav99
                                                        
 Step 5 - Ab aapko apne private channel me post daalni hogi.
                            
 Note : Bot Admin aapke channel me join hona chahiye,
 agr bot admin apka request accept nhi kar rhe hai to unhe personal msg karen.
  @yash_yadav99''')
