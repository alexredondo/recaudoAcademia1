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
#        aleatorio_hello_informal = choice(["Hola, que tal π","πHola, soy @lajirafabot","Hi! God bless you π","","","","","","","","","","","Blessing π"])
#        if re.search(saludo, user_message) is not None:
#            return aleatorio_hello_informal

#Saludo formal qw
#    intent_saludo_formal_usuario = ("buenos dias", "buenas noches","buenas tardes","good morning","good morning academia","buen dia","buenos dΓ­as")
#    for saludo in intent_saludo_formal_usuario:
#        aleatorio_saludo_formal = choice(["","πTe saluda @lajirafabot","π Hola, cordial saludo @lajirafabot","Dios le bendiga π","","","","","","","","","Bendiciones π"])
#        if re.search(saludo, user_message) is not None:
#            return aleatorio_saludo_formal

#Aviso escuela de padres
#    intent_aviso_escuela_padres = ("mu", "um","pu","up")
#    for x in intent_aviso_escuela_padres:
#        if re.search(x, user_message) is not None:
#            return """
#π PerdΓ³n interrumpo: \n
#Le recordamos que los acudientes deben hacer la Escuela de Padres.\n
#Los capΓ­tulos 1 y 2 estΓ‘n disponibles.\n
#Ingrese a este link:\n
#/escuela
#"""

#Escuela de padres
    intent_escuela_padres = ("escuela de padres", "escuela padres")
    for x in intent_escuela_padres:
        if re.search(x, user_message) is not None:
            return "π Por favor vaya a : \n /escuela"

#Emojis
    intent_emoji = ("πππ","β­οΈβ­οΈβ­οΈ","πππ")
    for emoji in intent_emoji:
        aleatorio_emocion_emoji = choice(["Maravilloso πΊ","Genial π»","Me gusta π·"])
        if re.search(emoji, user_message) is not None:
            return aleatorio_emocion_emoji

#Agradecimiento
    if user_message in ("muchas gracias","thanks you","gracias teacher"):
        aleatorio_gracias = choice(["π§‘ππβ€οΈ","π π’π΅π΄","Wonderfull π«","Genial ππ½","Me gusta ππ½","Maravilloso πΊ","πΌ","π»","π"])
        return aleatorio_gracias



#Medios de pago
    intent_estadocuenta = ("medios de pago", "medio de pago")
    for x in intent_estadocuenta:
        if re.search(x, user_message) is not None:
            return """\n
Hola πΊ,\n\n Para conocer los medios de pago vaya a /mediodepago\n"""

# Pago por pse
    intent_pagopse = ("pago por internet", "pago por pse", "pse","pagar por pse")
    for x in intent_pagopse:
    	if re.search(x, user_message) is not None:
        	return "π¦ Por favor vaya a : \n /mediodepago"

#Evidencia pago    
    if user_message in ("π*","π**"):
        mensaje_pago_recibido=("Muchas gracias!\n\nπ¬ Al correo se le envΓ­a el recibo de caja ")
        
        return  mensaje_pago_recibido

# Link recaudo
    if user_message in ("link rec", "link recaudo"):
        link_recaudo = """
        [Link recaudo](https://docs.google.com/spreadsheets/d/11P7-Eq_MGWGSjqirMawN3pS0t6Jsc5W4fb6UfGUeqQI/edit?usp=sharing)
        """
        return link_recaudo

#Solicitud estado de Cuenta
    intent_estado_cuenta = ("estado de cuenta","cuΓ‘nto debo")
    for solicitud_estado_cuenta in intent_estado_cuenta:
        if re.search(solicitud_estado_cuenta, user_message) is not None:    
            return  "Si necesita informaciΓ³n sobre su estado de cuenta por favor ingrese a este link: \n\n   /cuenta"

#enfermo
    intent_enfermo = ("amaneciΓ³ enfermo","amaneciΓ³ con gripa", "amaneciΓ³ con fiebre","oramos por")
    for enfermo in intent_enfermo:	
        aleatorio_enfermo = choice(["π» El SeΓ±or alejarΓ‘ de ti toda enfermedad. Deut. 7:15","πΊ He escuchado tu oraciΓ³n, y he visto tus lΓ‘grimas. Te voy a devolver la salud... 2 Reyes 20:5","πΌ Cuando estΓ© enfermo, el SeΓ±or lo sustentarΓ‘; suavizarΓ‘ sus males mientras recobra la salud. Salmo 41:3-4","π Γl sana a los de corazΓ³n quebrantado y les venda las heridas. Salmo 147:3","πΊ Γl perdona todos mis pecados y sana todas mis enfermedades. Me redime de la muerte y me corona de amor y tiernas misericordias. Salmo 103:3-4","πΌ Oh SeΓ±or mi Dios, clamΓ© a ti por ayuda, y me devolviste la salud. Salmo 30:2","π» βIrΓ© a sanarloβdijo JesΓΊs. Mateo 8:7","π Γl mismo cargΓ³ nuestros pecados sobre su cuerpo en la cruz, para que nosotros podamos estar muertos al pecado y vivir para lo que es recto. Por sus heridas, ustedes son sanados. 1 Pedro 2:24"])
        if re.search(enfermo, user_message) is not None:
            return aleatorio_enfermo

#Solicitud certificado
    intent_certificado = ("certificado","necesito un certificado", "necesito unos certificados", "necesito el observador")
    for x in intent_certificado:
        if re.search(x, user_message) is not None:
            return  " π EL certificado se le enviara en formato PDF por este medio.\n π Si lo necesita impreso debe solicitarlo.\n π Pronto se lo enviaremos, si el certificado estΓ‘ pago.\n  Ingrese a este link para mayor informaciΓ³n:\n\n   /certificados \n\n"

###### GENERA LISTADOS ######
# FunciΓ³n que genera listados
    def genera_lista():
        f = open("list_student.txt","w", encoding="utf-8") #Se crea y se abre el archivo de texto donde se almacenarΓ‘n los datos. De manera escribible "w"
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
        #apertura del archivo para impresiΓ³n
        f = open("list_student_text_3.txt", "r", encoding="utf-8")
        return "*LISTA DE ESTUDIANTES*\n"+"Cantidad: "+"*"+str(len(list_student.index))+"*"+"\n"+f.read() # imprime

# Lista de estudiantes del grado segundo
    if user_message in ("lista segundo", "lista de segundo"): #solicitud del usuario
        list_student = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=578605500&single=true&output=csv') # variable con tabla de datos se trae de googlesheet. Hoja compartida como archivo CSV.
        genera_lista()
        #apertura del archivo para impresiΓ³n
        f = open("list_student_text_3.txt", "r", encoding="utf-8")
        return "*LISTA DE ESTUDIANTES*\n"+"Cantidad: "+"*"+str(len(list_student.index))+"*"+"\n"+f.read() # imprime

# generar beneficios de Academia
    if user_message in ("beneficios academia","valor agregado"):  # solicitud del usuario
        return """π« Beneficios que tendrΓ‘ su hijo(a) y su familia en Academia de las AmΓ©ricas.\n
π Colegio legalizado que le ofrece todas las garantΓ­as.\n
βοΈ Formamos en Principios Cristianos. Usamos la Biblia para crear en su hijo(a) una buena conciencia.\n
π¨βπ©βπ§βπ§ Trabajamos con la familia para formar el carΓ‘cter de su hijo(a).\n
π Se hace Γ©nfasis en la autonomΓ­a y autocontrol del estudiante sin descuidar los aspectos acadΓ©micos.\n
π Se tiene en cuenta la individualidad, el ritmo y estilo de aprendizaje de su hijo(a).\n
π¦ EnseΓ±amos a cuidar la CreaciΓ³n.\n
π©π½βπ« Si hijo(a) gozarΓ‘ de cuidado, atenciΓ³n y orientaciΓ³n educativa profesional.\n
πΊπΈ InglΓ©s con enfoque comunicativo. \n
π₯ SupervisiΓ³n permanente con cΓ‘maras de seguridad.\n
βοΈ Aulas Climatizadas.\n
π± PrΓ³ximamente sede campestre.""" 

# imprime estado de cuenta,
    if user_message in [1001267993107,1001495905419,637490155,545054499,1001410910756,477108352,1001445422887,1001470298709,726249836,1001266243352,587492183,1001283899591,566823099,1001221364964,594244247,528328293,748250659,662072738,756678131,710900500,422965172,776155007,633478750,676845958,623339134,752044425,560957978,1001196292071,757466026,740479597,599226510,501580454,581778935,1001368730091,672121967,439651001,1001211791436,1001338979168,748183480,1001167380937,790584346,728612699,698079942,734477373,611306758,535466020,767162818,1001305466129,756580481,1001264500088,557416475,1001461280909,1001192665079,622292237,1001464329565,799222645,1001142933062,472357309,759343522,647748494,1001406436321,552517645,538487341,620071757,351031030,518641853,723545874,732978397,554086935,1001339104279,510276625,575000667,1001440528243,1001182500455,672736997,490850457,699687288,559530067,1001570276588,595069557,551577974,1001302901969,770507589,1001451733819,1001274258420,1001312416160,554322447,1001320754846,1001150498120,1001266990295,1001481165950,612122202,1001457216726,558915467,624580913,755233786,655489125,792102174,545183138,574533361,640252592,1001278091682,1001328107083,563619371,752083719,1001279231726,1001488952760,595199550,1001208965865,1001302095736,689406794,1001404608798,1001477355014,682647226,568864068,1001205518852,788104944,786775660,603922579,503477914,728811067,1001172739471,724799453,619265285,711805812,690587999,481876860,551345504,566487320,656747872,689522479,542153732,791801131,627594336,611831400,785058298,757583293,635882146,770969970,493365506,683321440,774961259,556879023,1001283932268,452871317,723804901,581702445,580389531,637109239,1001469218139,1001483924582,765722062,536682869,451366432,621280014,1001189318617,1001319311940,593397709,432540381,1001404608798,408511221,1001370703658,484414281,600154036,470613869,515092503,599089927,1001223256071,1001496758574,662976236,1001358586027,516150994,678622863,629386700,791313000,671096309,577911714,726621973,795685020,642140962,319341829,634237815,1103508213,1001206589331,360394219,724196433,690912365,1001741297507,1001374770303,794732548,505871413,1001315818754,555771002,524874696,528116276,549528860,1001277784940,728773748,1001199538935,730294525,779969592,1001365628615,1001405770808,1001414647950,1001406444172,692273587,1001288308029,569663296,792104990,740177499,510741897,478229244,554322447,1001487750670,750091325,710560974,732019615,755666935,732059711,526287404]:
        recaudoPD = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=330651820&single=true&output=csv')
        id_est=int(user_message)
        recaudoPD["Pago"] = pd.Series(recaudoPD["Pago"])
        recaudoPD["Pago"] = pd.to_numeric(recaudoPD["Pago"], downcast='integer')
        recaudoPD["Valor"] = pd.Series(recaudoPD["Valor"])
        recaudoPD["Valor"] = pd.to_numeric(recaudoPD["Valor"], downcast='integer')
        filtro = recaudoPD["ID"] == id_est
        my_filtro = recaudoPD[filtro]
        myFiltroSort = my_filtro.sort_values("Fecha")
        myFiltroSort[["Pago","Valor"]]=myFiltroSort[["Pago","Valor"]].applymap("{:.0f}".format)

        file1 = myFiltroSort[["Concepto","Fecha","Pago","Valor"]]

        f = open("recaudo.txt","w", encoding="utf-8")
        f.write("ESTADO DE CUENTA"+"\n\n"+"Estudiante:\n" + str(my_filtro.iloc[0,1])+ '\n\n')
        f.write("Correo de recepciΓ³n facturas DIAN: " + "\n" + str(my_filtro.iloc[0,6]) + '\n\n')
        archivoJson = file1.to_json(orient="split")
        parsed = json.loads(archivoJson)
        f.write("Los costos educativos estΓ‘n en rojo π΄ \n y los pagos realizados en verde π’:\n")

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
        f.write("π’ Pagado       : {:=17,} ".format(totalPagos))
        f.write("\n")
        f.write("π΄ {}   : {:=14,} ".format(a_favor,pendiente))
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
            xf=x.replace("π΄\', \'","π΄\nPlazo: ")
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
            xf=x.replace("π’, ","π’\nFecha:")
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

### FIN LISTA DOCENTES ###

#START Mensaje de cobro
    if user_message in ("β¬"):
        return ("""
        Hola familia !\n\n
        Se registra pago pendiente.\n
        Por favor consultar su estado de cuenta\n
        /cuenta\n\n
        Estar al dΓ­a con los pagos nos ayuda a prestar mejor el servicio.
        """)
#END Mensaje de cobro

#Default _
    aleatorio = ""#choice(["/help π¬","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","π π’π΅π΄",""])
    
    return aleatorio
