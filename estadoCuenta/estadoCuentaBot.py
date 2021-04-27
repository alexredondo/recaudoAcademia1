#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

import responses as R

print("Bot started")
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start_command(update: Update, _: CallbackContext):
    update.message.reply_text("Type something random to get started!")

def help_command(update: Update, _: CallbackContext):
    update.message.reply_text("If you need help! google")

def handle_message(update, context):
        text = str(update.message.text).lower()
        response = R.sample_responses(text)

        update.message.reply_text(response)
                
def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("1692061330:AAGesKceLctjO3nc_B8Y2ZCXLTsZ8ARmz64")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

