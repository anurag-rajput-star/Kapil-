import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import urllib.parse

# बॉट टोकन
BOT_TOKEN = "8366606958:AAHCfepMaw8Xsfq0c7ExRD51azq96zmUoNU"

# यहाँ वह URL डालें जो Netlify से मिली
WEB_PAGE_URL = "https://wonderful-moonbeam-12345.netlify.app/video_player.html"

print("🤖 Starting TeraBox Web Player Bot...")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 **TeraBox Web Video Player**\n\n"
        "Send me any TeraBox link and I'll create instant web player!\n\n"
        "Just paste your TeraBox video link below... ⬇️"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    
    if "terabox.com" in user_text and "/s/" in user_text:
        try:
            # Web player URL बनाएं
            encoded_url = urllib.parse.quote(user_text)
            web_player_url = f"{WEB_PAGE_URL}?video_url={encoded_url}"
            
            # Buttons बनाएं
            buttons = [
                [InlineKeyboardButton("🎥 PLAY IN WEB PLAYER", url=web_player_url)],
                [InlineKeyboardButton("🔗 DIRECT TERABOX LINK", url=user_text)]
            ]
            keyboard = InlineKeyboardMarkup(buttons)
            
            await update.message.reply_text(
                "✅ **Web Video Player Ready!**\n\n"
                "🎯 **Recommended:** PLAY IN WEB PLAYER\n"
                "• Better video quality\n"
                "• Instant playback\n"
                "• Mobile friendly\n\n"
                "Click below to start watching! 👇",
                reply_markup=keyboard
            )
            print(f"🎯 Web player created for: {user_text}")
            
        except Exception as e:
            await update.message.reply_text("❌ Error. Please try again.")
    
    else:
        await update.message.reply_text(
            "❌ Please send valid TeraBox video link\n\n"
            "Example: https://terabox.com/s/1xyz123..."
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    
    print("✅ Bot Started Successfully!")
    print("🌐 Web Player System Active!")
    app.run_polling()

if __name__ == '__main__':
    main()
