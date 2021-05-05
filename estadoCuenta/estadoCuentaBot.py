#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

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

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start_command(update: Update, _: CallbackContext):
    update.message.reply_text("Type something random to get started!")

def help_command(update: Update, _: CallbackContext):
    update.message.reply_text("Pronto te ayudaremos o selecciona la opción más adecuada: \n 🔹 Medios de pago: /mediodepago", parse_mode="markdown")

def mediodepago_command(update: Update, _: CallbackContext):                   
    update.message.reply_text("Opción 1️⃣ : Para pagar por internet puede usar este : \n [link de pago por PSE](https://www.mipagoamigo.com/MPA_WebSite/ServicePayments/StartPayment?id=4510&searchedCategoryId=&searchedAgreementName=ACADEMIA%20DE%20LAS%20AMERICAS)\n\nOpción 2️⃣: 1. Ir a la oficina *SERVICER* que le quede más cerca. \n 2. Suministra el número del convenio *15754127* \n 3. Suministra el NUIP del estudiante. (Registro civil o Tarjeta de identidad) \n\nOpción 3️⃣: 1. Ir a la sucursal del *BANCO CAJA SOCIAL*. \n 2. Suministra el número del convenio *15754127* \n 3. Suministra el NUIP del estudiante. (Registro civil o Tarjeta de identidad)", parse_mode="markdown")
    
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
    dispatcher.add_handler(CommandHandler("mediodepago", mediodepago_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))


    # Start the Bot
    updater.start_polling()
    print("Bot started")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()