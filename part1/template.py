from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    print("UPDATE:", update)
    print("CONTEXT:", context)

def main():
    # Get telegram bot token from botfather, and do not lose or reveal it
    # TODO: Change below to your bot token
    BOT_TOKEN = "1410991421:AAHrkw_1lTks0w7g_NkvoHtWZMeOM_lp5gg"

    # bot updater, refer to https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html
    updater = Updater(BOT_TOKEN, use_context=True)
    
    # bot dispatcher to register command handlers
    dp = updater.dispatcher

    # put your handlers here
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()