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

#Saludo formal
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
    if user_message in ["1001172739471","1001368730091","690587999","566823099","740479597","774961259","689406794","752044425","594244247","1001302095736","1001278091682","1001328107083","791801131","734477373","611306758","728811067","1001264500088","767162818","510276625","560957978","790584346","1001457216726","757583293","587492183","633478750","724799453","662072738","710900500","535466020","698079942","723545874","732978397","1001338979168","1001266243352","1001445422887","563619371","1001470298709","545054499","1001211791436","581778935","1001221364964","756678131","1001483924582","439651001","786775660","676845958","1001274258420","647748494","785058298","612122202","1001167380937","637490155","672121967","490850457","622292237","422965172","1001150498120","580389531","640252592","599226510","1001302901969","603922579","600154036","528328293","776155007","472357309","1001267993107","756580481","477108352","1001410910756","1001283899591","757466026","1001495905419","557416475","1001305466129","671096309","599089927","1001358586027","1103508213","748250659","623339134","1001440528243","748183480","319341829","568864068","1001196292071","501580454","1001207414865","752083719","545183138","1076512291","451366432","1001189318617","577911714","726621973","795685020","642140962","634237815","516150994","678622863","629386700","791313000","1001206589331"]:
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
