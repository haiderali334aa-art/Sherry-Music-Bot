
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable missing!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🎵 Welcome to Sherry Music Bot!\n\n"
        "Send /help to see commands."
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "🎶 Sherry Music Bot Commands:\n"
        "/start - Start bot\n"
        "/help - Help"
    )

print("Sherry Music Bot is running...")
bot.infinity_polling()
