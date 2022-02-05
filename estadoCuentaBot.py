#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

import logging
import pandas as pd
import json
import re
import csv
from fpdf import FPDF

from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# librerias propias
import responses as R

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Probando botón
def boton_command(update: Update, _: CallbackContext):
    # Configuración de los botones
    button1 = InlineKeyboardButton(
        text ="información",
        url="www.academia.net.co"
    )

    button2 = InlineKeyboardButton(
        text ="Medios de Pago",
        url="https://telegra.ph/Titulo-de-ejemplo-01-23"
    )
    # Impresión de los botones
    update.message.reply_text(
        text="Hola mundo",
        reply_markup=InlineKeyboardMarkup([
         [button1, button2]
        ])
    )

# comando de inicio
def start_command(update: Update, _: CallbackContext):
    update.message.reply_text("""Un saludo de paz de parte de *Academia de las Américas*.
    *Dios* es el principio. Estamos completos por Él. Esto es la *PAZ*:
    El orden, la belleza y el bienestar en nuestros corazones y alrededor nuestro.""", parse_mode="markdown")
    update.message.reply_photo("https://docs.pyrogram.org/index.html")
    update.message.reply_document("https://github.com/alexredondo/recaudoAcademia1/raw/master/certificado.pdf")

# Comando para consultar el ID del estudiante
def consulta_id_chat_command(update: Update, _: CallbackContext):
#    update.message.reply_text(f'*Hello* {update.effective_user.first_name}\n{update.effective_user.last_name}\n{update.effective_user.id}\n{update.effective_user.username}', parse_mode="markdown")
#    update.message.reply_text(f'*Hello* {update.effective_chat.id}',parse_mode="markdown")
    update.message.reply_text("Este es el *ID* que lo identifica en *Academia de las Américas*: \n\n" +str(update.effective_chat.id)+"\n\n"+"Por favor no lo comparta.",parse_mode="markdown")

# Comando de ayuda /ayuda
def help_command(update: Update, _: CallbackContext):
    update.message.reply_text("""
👷‍♀️ Para nosotros es un placer ayudarte...\n\n
Seleccion la opción más adecuada: \n\n
🔹 Estado de cuenta: ingrese el *ID* del estudiante \n
🔹 Medios de pago: /mediodepago \n
🔹 Certificados: /certificados \n
🔹 Horarios: /horarios\n
🔹 Puede escribirle al director @alexredondo
""", parse_mode="markdown")

# Medios de pago /mediodepago
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

# Link de pagos por pse
def link_pse_command(update: Update, _: CallbackContext):
    update.message.reply_text("""\n\n
    🏦 Para pagar por internet puede usar este : \n
    [link de pago por PSE](https://www.mipagoamigo.com/MPA_WebSite/ServicePayments/StartPayment?id=4510&searchedCategoryId=&searchedAgreementName=ACADEMIA%20DE%20LAS%20AMERICAS)"""
        , parse_mode="markdown")

# certificados
def certificados_command(update: Update, _: CallbackContext):
    update.message.reply_text("Específique por este medio el tipo de certificado que necesita.\n Tenga en cuenta el plazo para la entrega", parse_mode="markdown")
    update.message.reply_text("📃 Los certificados tienen un plazo de *dos días hábiles*.\nValor: $9.500 cada uno. \n\n 📃📃 El observador del estudiante, *cinco días hábiles*.\nValor: $17.600", parse_mode="markdown")
    update.message.reply_text("""\n\n
    🏦 Para pagar el certificado por internet puede usar este : \n
    [link de pago por PSE](https://www.mipagoamigo.com/MPA_WebSite/ServicePayments/StartPayment?id=4510&searchedCategoryId=&searchedAgreementName=ACADEMIA%20DE%20LAS%20AMERICAS)\n
    Usar otros /mediodepago"""
        , parse_mode="markdown")
                              
# horarios
def horarios_command(update: Update, _: CallbackContext):
    update.message.reply_text("*Horarios de clases*\n\n1️⃣[Primero](https://www.academia.net.co/p/horario-primero-2021.html)\n\n2️⃣[Segundo](https://www.academia.net.co/p/horario-segundo-2021.html)\n\n3️⃣[Tercero](https://www.academia.net.co/p/horario-tercero.html)\n\n4️⃣[Cuarto](https://www.academia.net.co/p/horario-cuarto.html)\n\n5️⃣[Quinto](https://www.academia.net.co/p/horario-quinto-2021.html)\n\n", parse_mode="markdown")

# LLamar archivo de respuestas
def handle_message(update, context):
        text = str(update.message.text).lower()
        response = R.sample_responses(text)

        update.message.reply_text(response)

#Estado de cuenta
def estadocuenta_command(update: Update, _: CallbackContext):
    update.message.reply_text("Cordial saludo ! \n A continuación los pagos actualizados hasta ayer.\n")
    id_chat_guion = str(update.effective_chat.id)
    id_chat_string = id_chat_guion.replace("-", "")
    recaudoPD = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=1830933640&single=true&output=csv')
    id_est=int(id_chat_string)
    filtro = recaudoPD["ID"] == id_est
    my_filtro = recaudoPD[filtro]
    myFiltroSort = my_filtro.sort_values("Fecha")
    myFiltroSort[["Pago","Valor"]]=myFiltroSort[["Pago","Valor"]].applymap("{:.0f}".format)

    file1 = myFiltroSort[["Concepto","Fecha","Pago","Valor"]]

    f = open("recaudo.txt","w", encoding="utf-8")
    f.write("ESTADO DE CUENTA"+"\n\n"+str("Estudiante:\n"+my_filtro.iloc[1,1])+'\n\n')
    f.write("Correo de recepción facturas DIAN: " + "\n" + str(my_filtro.iloc[1,6]) + '\n\n')
    archivoJson = file1.to_json(orient="split")
    parsed = json.loads(archivoJson)
    f.write("Los costos educativos están en rojo 🔴 y los pagos realizados en verde 🟢:\n")

    with open('recaudo.json','w', encoding="utf-8") as f:
        json.dump(parsed,f, indent=4)


    with open ('recaudo.json','r', encoding="utf-8") as f:
        recaudo_json =json.load(f)

    for i in range(len(recaudo_json["data"])):
        print (recaudo_json["data"][i])

        with open ('recaudo.txt','a', encoding="utf-8") as f:
            f.write("_______________________________"+'\n')
            f.write(str(recaudo_json["data"][i])+'\n')

    f=open("recaudo.txt","a", encoding="utf-8")
    totalCostos = my_filtro["Valor"].sum()
    totalPagos = my_filtro["Pago"].sum()
    pendiente = totalCostos-totalPagos
    a_favor="Pendientes"
    if pendiente<0:
        a_favor=" A favor."
    f.write("\n")
    f.write("Total a la fecha : {:=17,} ".format(totalCostos))
    f.write("\n")
    f.write("🟢 Pagado       : {:=17,} ".format(totalPagos))
    f.write("\n")
    f.write("🔴 {}   : {:=14,} ".format(a_favor,pendiente))
    f.write("\n\n"+"Ir al siguiente link para acceder a los medios de pago: "+"\n")
    f.write("/mediodepago")
    f.close()

    registro=open("recaudo.txt","r", encoding="utf-8")
    f = open("recaudoText.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace("]","")
        f.write(xf)
    f.close()

    registro=open("recaudoText.txt","r", encoding="utf-8")
    f = open("recaudoText1.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace("[","")
        f.write(xf)
    f.close()

    registro=open("recaudoText1.txt","r", encoding="utf-8")
    f = open("recaudoText2.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace("🔴\', \'","🔴\nPlazo: ")
        f.write(xf)
    f.close()

    registro=open("recaudoText2.txt","r", encoding="utf-8")
    f = open("recaudoText3.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace("\', \'0\', \'","\nValor a pagar: $")
        f.write(xf)
    f.close()

    registro=open("recaudoText3.txt","r", encoding="utf-8")
    f = open("recaudoText4.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace("\'","")
        f.write(xf)
    f.close()

    registro=open("recaudoText4.txt","r", encoding="utf-8")
    f = open("recaudoText5.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace("🟢, ","🟢\nFecha:")
        f.write(xf)
    f.close()

    registro=open("recaudoText5.txt","r", encoding="utf-8")
    f = open("recaudoText6.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace(", 0","")
        f.write(xf)
    f.close()

    registro=open("recaudoText6.txt","r", encoding="utf-8")
    f = open("recaudoText7.txt","w", encoding="utf-8")
    for x in registro:
        xf=x.replace(", ","\nPagado: $")
        f.write(xf)
    f.close()

    f = open("recaudoText7.txt","r", encoding="utf-8")
    update.message.reply_text(f.read())

############# ESCUELA DE PADRES #################
# Escuela de padres
def escuelapadres_command(update: Update, _: CallbackContext):
    update.message.reply_text(f"*Cordial saludo* {update.effective_user.first_name}:"+"""\n
    🤝Bienvenidos a nuestra escuela de padres.\n
    *Metodología*
    1. Leer cada capítulo de libro
    2. Ver el vídeo
    3. Resolver el cuestionario
    4. Recordar las ideas fundacionales
    
    ▶️ /tablacontenido""", parse_mode="markdown")
  

# Tabla de contenido
def tablacontenido_command(update: Update, _: CallbackContext):
    update.message.reply_text("""*TABLA DE CONTENIDO*:
    /cap1 Dios piensa en individuos, naciones y generaciones
    /cap2 Dios instruye la familia y Sus leyes para ella
    /cap3 ¿Cuál es la base de la familia y su acción?
    /cap4 Lo que deben hacer los padres
    /cap5 Lo que no deben hacer los padres
    /cap6 La edades que Dios nos dio en la vida
    /cap7 Diseño diferente y complementario
    /cap8 Educando en comodato
    /cap9 Familias cristianas, naciones y generaciones en libertad
    /cap10 Eligiendo una nueva familia
    Ir a /escuela""", parse_mode="markdown")

#Capitulo 1
def capitulo1_command(update: Update, _: CallbackContext):
    update.message.reply_text("""*1️⃣ Dios piensa en individuos, naciones y generaciones*\n
    📺 [Vídeo](https://www.youtube.com/watch?v=JQCiqKQT1t8)
    📝 [Formulario](https://docs.google.com/forms/d/e/1FAIpQLSeVXR0DxsS8v6IvZwWM59lN1_vD74b-IVdPSJWvcdrT3Asmvg/viewform)
    ▶️ [Encuentro](https://www.youtube.com/watch?v=JQCiqKQT1t8)
    ▶️ /tablacontenido
    ▶️ /escuela""", parse_mode="markdown")

############# LISTADOS KIT #################
def kit_command(update: Update, _: CallbackContext): #f"*Hola* {update.effective_user.first_name}:"+
    update.message.reply_text("""
    🤝 Elige el grupo respectivo en este _link_:\n
    
    ▶️ [Lista pagos y entrega de kit](https://docs.google.com/spreadsheets/d/1fKt4x70n3gfto281aB_sGzuXN9YY_3ZSPyN8zWPdKNY/edit#gid=383016375)

    """, parse_mode="markdown")

############# IMPRIMIR PDF #################
def imprimirpdf ():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'ESTADO CUENTA')
    pdf.output('estado_cuenta_academia.pdf', 'F')

def imprimirpdf_command(update: Update, _: CallbackContext): #f"*Hola* {update.effective_user.first_name}:"+
    imprimirpdf ()
    update.message.reply_document("/estado_cuenta_academia.pdf")

# código de sistema
def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("1673996388:AAG1LqRgDPaAiGDlA0He8c-SQD8sihLgbaA")

# Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("boton", boton_command)) #probando botón
    dispatcher.add_handler(CommandHandler("id", consulta_id_chat_command))
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("ayuda", help_command))
    dispatcher.add_handler(CommandHandler("mediodepago", mediodepago_command))
    dispatcher.add_handler(CommandHandler("certificados", certificados_command))
    dispatcher.add_handler(CommandHandler("horarios", horarios_command))
    dispatcher.add_handler(CommandHandler("cuenta", estadocuenta_command))
    dispatcher.add_handler(CommandHandler("linkpse", link_pse_command))
    dispatcher.add_handler(CommandHandler("kitsi", kit_command))
    dispatcher.add_handler(CommandHandler("pdf", imprimirpdf_command))
    dispatcher.add_handler(CommandHandler("escuela", escuelapadres_command))
    dispatcher.add_handler(CommandHandler("tablacontenido", tablacontenido_command))
    dispatcher.add_handler(CommandHandler("cap1", capitulo1_command))
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
