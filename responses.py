	#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram import  Update
from random import choice
import pandas as pd
import json
import re

def sample_responses(input_text):
    user_message = str(input_text).lower()
    user_message_name = str(input_text).upper()
#Consulta NUIP
#    intent_consulta_nuip = {"AARON ANDRES OVIEDO OVIEDO":"1030247719"}
#    if user_message_name in ("AARON ANDRES OVIEDO OVIEDO"):
#        return  intent_consulta_nuip[user_message_name]

#Consulta NAME ESTUDIANTE
#    intent_consulta_name = ["AARON ANDRES OVIEDO OVIEDO"]
#    with open ('name_estudiantes.txt','w') as f:
#        f.write("Estudiantes: \n")
#        f.close()

#Consulta NUIP
 #   if user_message in ("^a","^b","^c","^d","^e","^f","^g","^h","^i","^j","^k","^l","^m","^n","^o","^p","^q","^r","^s","^t","^u","^v","^w","^x","^y","^z"):
 #       for name_estudiante in intent_consulta_name:
 #          if re.findall(user_message_name,name_estudiante):
 #               with open ('name_estudiantes.txt','a') as f:
 #                   f.write(name_estudiante+"\n")
 #                   f.close()
 #       f = open("name_estudiantes.txt","r") 
 #       return  f.read()

#Saludo informal
#    intent_saludo_informal_usuario = ("hello", "hi","hola",)
#    for saludo in intent_saludo_informal_usuario:
#        aleatorio_hello_informal = choice(["Hola, que tal 👍","👋Hola, soy @lajirafabot","Hi! God bless you 👍","","","","","","","","","","","Blessing 🙏"])
#        if re.search(saludo, user_message) is not None:
#            return aleatorio_hello_informal

#Saludo formal qw
#    intent_saludo_formal_usuario = ("buenos dias", "buenas noches","buenas tardes","good morning","good morning academia","buen dia","buenos días")
#    for saludo in intent_saludo_formal_usuario:
#        aleatorio_saludo_formal = choice(["","👋Te saluda @lajirafabot","👋 Hola, cordial saludo @lajirafabot","Dios le bendiga 👍","","","","","","","","","Bendiciones 🙏"])
#        if re.search(saludo, user_message) is not None:
#            return aleatorio_saludo_formal

#Escuela de padres
    intent_escuela_padres = ("escuela de padres", "escuela padres")
    for x in intent_escuela_padres:
        if re.search(x, user_message) is not None:
            return "👋 Por favor vaya a : \n /escuela"

#Emojis
    intent_emoji = ("👏👏👏","⭐️⭐️⭐️","👍👍👍")
    for emoji in intent_emoji:
        aleatorio_emocion_emoji = choice(["Maravilloso 🌺","Genial 🌻","Me gusta 🌷"])
        if re.search(emoji, user_message) is not None:
            return aleatorio_emocion_emoji

#Agradecimiento
    if user_message in ("muchas gracias","thanks you","gracias teacher"):
        aleatorio_gracias = choice(["🧡💚💙❤️","🟠🟢🔵🔴","Wonderfull 💫","Genial 👌🏽","Me gusta 👍🏽","Maravilloso 🌺","🌼","🌻","💐"])
        return aleatorio_gracias



#Medios de pago
    intent_estadocuenta = ("medios de pago", "medio de pago")
    for x in intent_estadocuenta:
        if re.search(x, user_message) is not None:
            return """\n
Hola 🌺,\n\n Para conocer los medios de pago vaya a /mediodepago\n"""

# Pago por pse
    intent_pagopse = ("pago por internet", "pago por pse", "pse","pagar por pse")
    for x in intent_pagopse:
    	if re.search(x, user_message) is not None:
        	return "🏦 Por favor vaya a : \n /mediodepago"

#Evidencia pago    
    if user_message in ("👍*","👍**"):
        mensaje_pago_recibido=("Muchas gracias!\n\n📬 Al correo se le envía el recibo de caja ")
        
        return  mensaje_pago_recibido

# Link recaudo
    if user_message in ("link rec", "link recaudo"):
        link_recaudo = """
        [Link recaudo](https://docs.google.com/spreadsheets/d/11P7-Eq_MGWGSjqirMawN3pS0t6Jsc5W4fb6UfGUeqQI/edit?usp=sharing)
        """
        return link_recaudo

#Solicitud estado de Cuenta
    intent_estado_cuenta = ("estado de cuenta","cuánto debo")
    for solicitud_estado_cuenta in intent_estado_cuenta:
        if re.search(solicitud_estado_cuenta, user_message) is not None:    
            return  "Si necesita información sobre su estado de cuenta por favor ingrese a este link: \n\n   /cuenta"

#enfermo
    intent_enfermo = ("amaneció enfermo","amaneció con gripa", "amaneció con fiebre","oramos por")
    for enfermo in intent_enfermo:	
        aleatorio_enfermo = choice(["🌻 El Señor alejará de ti toda enfermedad. Deut. 7:15","🌺 He escuchado tu oración, y he visto tus lágrimas. Te voy a devolver la salud... 2 Reyes 20:5","🌼 Cuando esté enfermo, el Señor lo sustentará; suavizará sus males mientras recobra la salud. Salmo 41:3-4","💐 Él sana a los de corazón quebrantado y les venda las heridas. Salmo 147:3","🌺 Él perdona todos mis pecados y sana todas mis enfermedades. Me redime de la muerte y me corona de amor y tiernas misericordias. Salmo 103:3-4","🌼 Oh Señor mi Dios, clamé a ti por ayuda, y me devolviste la salud. Salmo 30:2","🌻 —Iré a sanarlo—dijo Jesús. Mateo 8:7","💐 Él mismo cargó nuestros pecados sobre su cuerpo en la cruz, para que nosotros podamos estar muertos al pecado y vivir para lo que es recto. Por sus heridas, ustedes son sanados. 1 Pedro 2:24"])
        if re.search(enfermo, user_message) is not None:
            return aleatorio_enfermo

#Solicitud certificado
    intent_certificado = ("certificado","necesito un certificado", "necesito unos certificados", "necesito el observador")
    for x in intent_certificado:
        if re.search(x, user_message) is not None:
            return  " 📝 EL certificado se le enviara en formato PDF por este medio.\n 📝 Si lo necesita impreso debe solicitarlo.\n 📝 Pronto se lo enviaremos, si el certificado está pago.\n  Ingrese a este link para mayor información:\n\n   /certificados \n\n"

###### GENERA LISTADOS ######
# Función que genera listados
    def genera_lista():
        f = open("list_student.txt","w", encoding="utf-8") #Se crea y se abre el archivo de texto donde se almacenarán los datos. De manera escribible "w"
        archivoJson = list_student.to_json(orient="split") # Se pasa el CSV a JSON
        parsed = json.loads(archivoJson)
        with open('list_student.json','w', encoding="utf-8") as f:
            json.dump(parsed,f, indent=4) # ?????
        with open('list_student.json', 'r', encoding="utf-8") as f:
            list_student_json = json.load(f)
        for i in range(len(list_student_json["data"])): #Escribir datos en el archivo
            print (list_student_json["data"][i])

            with open ('list_student.txt','a', encoding="utf-8") as f:
                f.write(str(list_student_json["data"][i])+'\n')

        #Reemplazar caracteres
        registro=open("list_student.txt","r", encoding="utf-8") # Se abre el archivo para reemplazar caracteres.
        f = open("list_student_text.txt","w", encoding="utf-8")
        for x in registro:
            xf=x.replace("]","")
            f.write(xf)
        f.close()

        registro=open("list_student_text.txt","r", encoding="utf-8") # Se abre el archivo para reemplazar caracteres.
        f = open("list_student_text_1.txt","w", encoding="utf-8")
        for x in registro:
            xf = x.replace("[", "")
            f.write(xf)
        f.close()

        registro=open("list_student_text_1.txt","r", encoding="utf-8") # Se abre el archivo para reemplazar caracteres.
        f = open("list_student_text_2.txt","w", encoding="utf-8")
        for x in registro:
            xf = x.replace(",", " ")
            f.write(xf)
        f.close()

        registro=open("list_student_text_2.txt","r", encoding="utf-8") # Se abre el archivo para reemplazar caracteres.
        f = open("list_student_text_3.txt","w", encoding="utf-8")
        for x in registro:
            xf = x.replace("'", " ")
            f.write(xf)
        f.close()

#Lista de estudiantes del grado primero
    if user_message in ("lista primero","lista de primero"): #solicitud del usuario
        list_student = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=1674038382&single=true&output=csv') # variable con tabla de datos se trae de googlesheet. Hoja compartida como archivo CSV.
        genera_lista()
        #apertura del archivo para impresión
        f = open("list_student_text_3.txt", "r", encoding="utf-8")
        return "*LISTA DE ESTUDIANTES*\n"+"Cantidad: "+"*"+str(len(list_student.index))+"*"+"\n"+f.read() # imprime

# Lista de estudiantes del grado segundo
    if user_message in ("lista segundo", "lista de segundo"): #solicitud del usuario
        list_student = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=578605500&single=true&output=csv') # variable con tabla de datos se trae de googlesheet. Hoja compartida como archivo CSV.
        genera_lista()
        #apertura del archivo para impresión
        f = open("list_student_text_3.txt", "r", encoding="utf-8")
        return "*LISTA DE ESTUDIANTES*\n"+"Cantidad: "+"*"+str(len(list_student.index))+"*"+"\n"+f.read() # imprime

# generar beneficios de Academia
    if user_message in ("beneficios academia","valor agregado"):  # solicitud del usuario
        return """💫 Beneficios que tendrá su hijo(a) y su familia en Academia de las Américas.\n
📄 Colegio legalizado que le ofrece todas las garantías.\n
✝️ Formamos en Principios Cristianos. Usamos la Biblia para crear en su hijo(a) una buena conciencia.\n
👨‍👩‍👧‍👧 Trabajamos con la familia para formar el carácter de su hijo(a).\n
📚 Se hace énfasis en la autonomía y autocontrol del estudiante sin descuidar los aspectos académicos.\n
😀 Se tiene en cuenta la individualidad, el ritmo y estilo de aprendizaje de su hijo(a).\n
🦒 Enseñamos a cuidar la Creación.\n
👩🏽‍🏫 Si hijo(a) gozará de cuidado, atención y orientación educativa profesional.\n
🇺🇸 Inglés con enfoque comunicativo. \n
🎥 Supervisión permanente con cámaras de seguridad.\n
❄️ Aulas Climatizadas.\n
🌱 Próximamente sede campestre.""" 

# imprime estado de cuenta
    if user_message in ["1104264601","1187464478","1043489184","1202213620","1103754527","1202213348","1104268355","1104265781","1103751941","1103752312","1103514312","1030247719","1025902842","1138674273","1103513624","1103750555","1103523542","1103511643","1108766619","1103522746","1043481075","1103522196","1103522494","1150188422","1103523086","1103522715","1103754928","1103750732","1103513144","1103520793","1103516148","1202214408","1103510808","1102869539","1103522518","1104267019","1104264968","1104264591","1103755940","1202213738","1104269104","1104270148","1103514601","1103523356","1103517928","1104263333","1104268673","1103511781","1104266789","1231338199","1103754409","1202214022","1043463150","1103748258","1103518355","1103749833","1104267196","1103511714","1103508816","1048078090","1076512291","1103512318","1103515645","1103516754","1104266534","1138675306","1138675305","1231840300","1231840301","1103517925","1103513759","1103756114","1103509334","1103509583","1103748035","1103759633","1103750026","1103756768","1138677367","1048081459","1103508560","1104263365","1103512107","1104268160","1020123319","1103748574","1102868925","1102213645","1102872914","1043313558","1104268067","1103509750","1104270411","1103512911","1023530668","1018260999","1103757134","1042864153","1202213706","1103506939","1201234938","1104270339","1103753551","1103756595","1103509587","1138678969","1138676669","1202214087","1103755533","1103513122","1104267486","1103523853","1125230534","1103757256","1103522600","1103749443","1138677262","1103761043","1103521434","1104268249","1202214233","1103519561","1103511845","1104269413","1103760062","1103516755","1103760551","1103515254","1139434087","1102860504","1231338017","1231339937","1102849604","1231338074","1103515275","1103756445","1231840112","1103759152","1231339973","1103516744","1104262997","1104265537","1231840853","1103758179","1103751028","1103756941","1058357747","1103761972","1103515651","1138674419","1068441433","1102232626","1030243055","1053003031","1104263305","1104266694","1103517537","1102872411","1102849638","1103748906","1103509948","1103758043","1138678391","1104265422","1138677533","1103509274","1138677181","1103507961","1103749236","1103509444","1103510179","1103513303","1103750756","1104264025","1103511870","1104266657","1011205983","1103515598","1103508084","1104267691","1231338763","1138675821","1103514224","1103515571","1103508213","1224953137","1103508124","1103517596"]:
        recaudoPD = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=1830933640&single=true&output=csv')
        id_est=int(user_message)
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
        return f.read()

### LISTA DOCENTES ###

    if user_message in ["teacher_list"]:
        lista_teachers = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vToYFmQPyJzsYhfu7pCrXWrjmGE346tA-i9XNOQbr8anQ5ItWUk0C8UcLj26gQZujc9paPhbe6vWdGa/pub?gid=306647251&single=true&output=csv')

        file1 = lista_teachers[["nombre","grupo"]]

        f = open("lista_teachers.txt","w", encoding="utf-8")
        archivoJson = file1.to_json(orient="split")
        parsed = json.loads(archivoJson)
        f.write("Docentes de Academia de las Américas\n"+"Cantidad: \n"+str(len(lista_teachers.index))+"\n\n")

        with open('lista_teachers.json','w', encoding="utf-8") as f:
            json.dump(parsed,f, indent=4)

        with open ('lista_teachers.json','r', encoding="utf-8") as f:
            lista_json =json.load(f)
	
        for i in range(len(lista_json["data"])):
            print (lista_json["data"][i])

            with open ('lista_teachers.txt','a', encoding="utf-8") as f:
                f.write(str(lista_json["data"][i])+'\n')
        f.close()
	
        registro = open("lista_teachers.txt","r", encoding="utf-8")
        f = open("lista_teachers_1.txt","w", encoding="utf-8")
        for x in registro:
            transTable = x.maketrans(",", ">", "[]'")
            xf = x.translate(transTable)
            f.write(xf)		
        f.close()

        f = open("lista_teachers_1.txt","r", encoding="utf-8") 
        return f.read()

### FIN LISTA DOCENTES ###

#Default 
    aleatorio = ""#choice(["/help 💬","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","🟠🟢🔵🔴",""])
    
    return aleatorio
