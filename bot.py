import json

import requests


import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os

PORT = int(os.environ.get('PORT', 5000))


# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

level=logging.INFO)



logger = logging.getLogger(__name__)

TOKEN = '1477909236:AAF8YbI0j-RCHs5MGssjacT0BiEWZ_uDM-Y'


def start(update, context):update.message.reply_text('Hi!')
    """Send a message when the command /start is issued."""
    



def help(update, context):update.message.reply_text('Help!')
    """Send a message when the command /help is issued."""
    



def echo(update, context):update.message.reply_text(update.message.text)
    """Echo the user message."""
   



def error(update, context):logger.warning('Update "%s" caused error "%s"', update, context.error)
    """Log Errors caused by Updates."""
    



def echo(update, context):update.message.reply_text(update.message.text)
    """Echo the user message."""
    



def main():updater = Updater(TOKEN, use_context=True)



# Get the dispatcher to register handlers

dp = updater.dispatcher



# on different commands - answer in Telegram

dp.add_handler(CommandHandler("start", start))

dp.add_handler(CommandHandler("help", help))




dp.add_handler(MessageHandler(Filters.text, echo))



# log all errors

dp.add_error_handler(error)



# Start the Bot

updater.start_webhook(listen="0.0.0.0",

port=int(PORT),

url_path=TOKEN)

updater.bot.setWebhook('https://app-teleg-blabot.herokuapp.com/' + TOKEN)



updater.idle()





if __name__ == '__main__':

    main()
