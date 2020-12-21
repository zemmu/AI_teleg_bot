import json

import requests

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os

PORT = int(os.environ.get('PORT', 5000))


# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = '1477909236:AAF8YbI0j-RCHs5MGssjacT0BiEWZ_uDM-Y'

def start(update, context): 
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context): 
    """Send a message when the command /help is issued.""" 
    update.message.reply_text('Help!')

def echo(update, context): 
    """Echo the user message.""" 
    update.message.reply_text(update.message.text)

def error(update, context): 
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def echo(update, context): 
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def main(): updater = Updater(TOKEN, use_context=True)


# Get the dispatcher to register handlers

dp = updater.dispatcher


# on different commands - answer in Telegram

dp.add_handler(CommandHandler("start", start))

dp.add_handler(CommandHandler("help", help))

dp.add_handler(MessageHandler(Filters.text, echo))


# log all errors

dp.add_error_handler(error)


# Start the Bot

updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)

updater.bot.setWebhook('https://app-teleg-blabot.herokuapp.com/' + TOKEN)

updater.idle()

if __name__ == '__main__':

    main()
