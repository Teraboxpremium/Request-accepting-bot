
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserIsBlocked, PeerIdInvalid


@Client.on_chat_join_request()
async def accept_request(bot, r):

    rm = InlineKeyboardMarkup([[         
            InlineKeyboardButton("👥 𝐆𝐑𝐎𝐔𝐏 - 𝟏", url=f"https://t.me/+XzVIX3lhqzAyYTQ1"),
            ],[
            InlineKeyboardButton("🖥 𝐍𝐄𝐖 𝐎𝐓𝐓 𝐔𝐏𝐃𝐓𝐄𝐒 🖥", url="https://t.me/+zyn6Ieosz5o4OTVl")
            ],[            
            InlineKeyboardButton("⭕️ 𝐆𝐄𝐓 𝐎𝐔𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐋𝐈𝐍𝐊𝐒 ⭕️", url="https://t.me/+XzVIX3lhqzAyYTQ1")
        ]])
    
    try:
        await bot.send_message(
            r.from_user.id,           
            f"**𝖧𝖾𝗅𝗅𝗈 {r.from_user.mention} 👻\n\n 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {r.chat.title} 𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖠𝗉𝗉𝗋𝗈𝗏𝖾𝖽.\n\nSend /start to know more**",
            )

    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid:
        print("Err")
    except Exception as e:
        print(f"#Error\n{str(e)}")

    await r.approve()
