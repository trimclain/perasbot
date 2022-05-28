#!/usr/bin/env python3

import logging
import os

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

from scripts.scraper import getCrypto
from scripts.parser import getData

with open('.token', 'r') as f:
    TOKEN = f.read()[:-1]  # last character is whitespace


# Enable logging

if not os.path.isdir('logs'):
    os.mkdir('logs')

logging.basicConfig(
    filename=os.path.join(os.getcwd(), 'logs', 'activity.log'),
    format='%(asctime)s %(levelname)s   %(name)s: %(message)s',
    level=logging.INFO,  # DEBUG to get all the updates
    filemode='a',
)
logger = logging.getLogger(__name__)


def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    text = (
        'Hello, I\'m PERAS, your personal assistant. '
        'Type "/" to see the list of available commands.'
    )
    update.message.reply_text(text)


def crypto(update: Update, _: CallbackContext) -> None:
    """Get the current bitcoin price"""
    btc = getCrypto('bitcoin')
    eth = getCrypto('ethereum')
    doge = getCrypto('dogecoin')
    cronos = getCrypto('cronos')
    text = f'BTC - {btc}\nETH - {eth}\nDOGE - {doge}\nCRO - {cronos}'
    update.message.reply_text(text)


def motivate(update: Update, _: CallbackContext) -> None:
    """Send a motivation message when the command /motivate is issued."""
    text = getData()
    update.message.reply_text(text)


def main():
    """Start the bot."""

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # On different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    # dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CommandHandler('crypto', crypto))
    dispatcher.add_handler(CommandHandler('motivate', motivate))

    # On noncommand i.e message - echo the message on Telegram
    # For multiple handlers need to change the group each time
    # dispatcher.add_handler(
    #     MessageHandler(Filters.text & ~Filters.command, talk)
    # )

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
