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
    update.message.reply_text("""
👷‍♀️ Para nosotros es un placer ayudarte...\n\n
Seleccion la opción más adecuada: \n\n
🔹 Estado de cuenta: ingrese el *nuip* del estudiante \n
🔹 Medios de pago: /mediodepago \n
🔹 Certificados: /certificados \n
🔹 Horarios: /horarios\n
🔹 Link salas meet: /linkmeet
🔹 Puede escribirle al director @alexredondo
""", parse_mode="markdown")

def mediodepago_command(update: Update, _: CallbackContext):                   
    update.message.reply_text("""
🏦 Estos son los medios de pagos disponibles para usted:\n\n
*Opción* 1️⃣ : \nPara pagar por internet puede usar este : \n
[link de pago por PSE](https://www.mipagoamigo.com/MPA_WebSite/ServicePayments/StartPayment?id=4510&searchedCategoryId=&searchedAgreementName=ACADEMIA%20DE%20LAS%20AMERICAS)\n\n
*Opción* 2️⃣: \n
1. Ir a la oficina *SERVICER* que le quede más cerca. \n
2. Suministra el número del convenio *15754127* \n
3. Suministra el NUIP del estudiante. (Registro civil o Tarjeta de identidad) \n\n
*Opción* 3️⃣: \n
1. Ir a la sucursal del *BANCO CAJA SOCIAL*. \n
2. Suministra el número del convenio *15754127* \n
3. Suministra el NUIP del estudiante. (Registro civil o Tarjeta de identidad)
""", parse_mode="markdown")

def valorpensionesparvulo_command(update: Update, _: CallbackContext):                   
    update.message.reply_text("""
*Costos Educativos 2021*:\n
*Párvulo*:\n
Matricula:\t\t$ 475.000
Pensión:\t\t$ 204.000
""", parse_mode="markdown")

def certificados_command(update: Update, _: CallbackContext):
    update.message.reply_text("📃 Los certificados tienen un plazo de *dos días hábiles*.\nValor: $8.000 cada uno. \n\n 📃📃 El observador del estudiante, *cinco días hábiles*.\nValor: $16.000", parse_mode="markdown")

def horarios_command(update: Update, _: CallbackContext):
    update.message.reply_text("*Horarios de clases*\n\n1️⃣[Primero](https://www.academia.net.co/p/horario-primero-2021.html)\n\n2️⃣[Segundo](https://www.academia.net.co/p/horario-segundo-2021.html)\n\n3️⃣[Tercero](https://www.academia.net.co/p/horario-tercero.html)\n\n4️⃣[Cuarto](https://www.academia.net.co/p/horario-cuarto.html)\n\n5️⃣[Quinto](https://www.academia.net.co/p/horario-quinto-2021.html)\n\n", parse_mode="markdown")

def linkmeet_command(update: Update, _: CallbackContext):
    update.message.reply_text("*CLASES VIRTUALES*\n*Link a Google Meet*\n\nIr a las clases de preescolar ➡️  /linkpreescolar\n\n1️⃣ [Primero](https://meet.google.com/snk-ctsw-nwu)\n\n2️⃣ [Segundo](http://meet.google.com/gtw-mxsm-rdf)\n\n3️⃣ [Tercero](https://meet.google.com/did-oxtt-dcy)\n\n4️⃣ [Cuarto](https://meet.google.com/wxb-vmbb-xds)\n\n5️⃣ [Quinto](https://meet.google.com/gii-yjow-ezc)\n\n", parse_mode="markdown")

def linkpreescolar_command(update: Update, _: CallbackContext):
    update.message.reply_text("*CLASES VIRTUALES PREESCOLAR*\n*Link a Google Meet*\n\n[🐶 Prejardín](https://meet.google.com/jec-nekg-tdu)\n\n[🐱 Jardín](http://meet.google.com/kxp-djhi-igr)\n\n[🐹 Transición](https://meet.google.com/eez-ehpt-zwv)", parse_mode="markdown")


def handle_message(update, context):
        text = str(update.message.text).lower()
        response = R.sample_responses(text)

        update.message.reply_text(response)
                
def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("1673996388:AAG1LqRgDPaAiGDlA0He8c-SQD8sihLgbaA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("mediodepago", mediodepago_command))
    dispatcher.add_handler(CommandHandler("certificados", certificados_command))
    dispatcher.add_handler(CommandHandler("horarios", horarios_command))
    dispatcher.add_handler(CommandHandler("linkmeet", linkmeet_command))
    dispatcher.add_handler(CommandHandler("linkpreescolar", linkpreescolar_command))
    dispatcher.add_handler(CommandHandler("valorpensionesparvulo", valorpensionesparvulo_command))
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