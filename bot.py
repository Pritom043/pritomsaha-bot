import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7060323721:AAENYf-_FCgkA_whMuypzIDo6lWeAPNX_g0"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "👤 Name: Pritom Saha\n"
        "🏠 Address: Arpara\n"
        "💼 Profession: ADS Expert\n"
        "📘 Facebook: https://www.facebook.com/share/1AbvBCrPEw/\n"
        "🎵 TikTok: https://www.tiktok.com/@pritom1231?_t=ZS-8w7kEouBKwz&_r=1"
    )
    await update.message.reply_text(message)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
