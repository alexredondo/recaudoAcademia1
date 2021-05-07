from random import choice
import pandas as pd
import json
import re

def sample_responses(input_text):
    user_message = str(input_text).lower()
#Saludo
    intent_saludo_usuario = ("hello", "hi","hola","buenos dias", "buenas noches","buenas tardes","good morning","good morning academia","buen dia","buenos días","hola !")
    for saludo in intent_saludo_usuario:
        aleatorio_hello = choice(["👋 Hola, cordial saludo!","Hi ! Dios le bendiga 👍","Hola, que tal !","Hi 😃!","Bendiciones 🙏","*♥.•´¸.•*´✶´♡ ¸.•*´´♡*💚˚*\n*_○💙   Greetings  💙*˚*\n*💚.•´¸.•*´✶´♡ ¸.•*´´♡⛅*\n*° ☆ ° ˛*˛☆_Π____*_*˚☆*\n*˚ ˛★˛•˚ */______/ ~＼。˚ ˚\n*˚ ˛•˛•🌈｜ 田田 ｜門｜ ˚*\n*🌴╬═🌴╬╬🌴╬╬🌴═╬╬═🌴"])
        if re.search(saludo, user_message) is not None:
            return aleatorio_hello
#Emojis
    intent_emoji = ("👏","excelente","⭐️")
    for emoji in intent_emoji:
        aleatorio_emocion_emoji = choice(["Maravilloso 🌺","Genial 🌻","Me gusta 🌷"])
        if re.search(emoji, user_message) is not None:
            return aleatorio_emocion_emoji

#Agradecimiento
    if user_message in ("gracias", "muchas gracias","thanks you","thanks","gracias teacher"):
        aleatorio_gracias = choice(["🧡💚💙❤️","🟠🟢🔵🔴","Wonderfull 💫","Genial 👌🏽","Me gusta 👍🏽","Maravilloso 🌺","🌼","🌻","💐"])
        return aleatorio_gracias

#Evidencia pago    
    if user_message in ("👍 :", ):
        mensaje_pago_recibido=("Muchas gracias!\n\n📬 Al correo se le envía el recibo de caja ")
        return  mensaje_pago_recibido

#Solicitud estado de Cuenta
    intent_estado_cuenta = ("estado de cuenta","estado")

    for solicitud_estado_cuenta in intent_estado_cuenta:

        if re.search(solicitud_estado_cuenta, user_message) is not None:
    
            return  "Para generar el estado de cuenta, \n\nPor favor escirba el NUIP del estudiante..." 

#Estado de cuenta
    if user_message in ["1030247719","1103754527","1103515254","1025555579","1102847991","1103510179","1043481075","1103515205","1103748757","1138677533","1103757793","1103750555","1102860979","1068435161","1103513122","1104265422","1104263305","1202214087","1103509838","1102872411","1090486177","1103754409","1202213348","1138674376","1103756941","1027808387","1103753690","1103756140","1104267486","1103508124","1103758561","1202213742","1104264591","1103507608","1102873753","1104263333","1224953137","1102856958","1103748258","1138674413","1104265131","1103749236","1202213106","1103752461","1202213620","1103512107","1020123319","1103519561","1231338199","1104267664","1103513624","1103750756","1103506939","1103749833","1103511845","1138674754","1138674581","1202213738","1103515645","1102869604","1103517925","1102860504","1030246017","1043313558","1138676669","1103508213","1102878043","1103543553","1138677181","1102313645","1202213468","1139434087","1103512911","1104266694","1042263697","1103748574","1103753551","1125230534","1202213662","1103752312","1104265781","1058357747","1103508816","1103751941","1138674184","1202214233","1103515651","1103507961","1103752763","1103513363","1138677933","1104265537","1103749443","1201234938","1104262917","1103748954","1103748317","1100397739","1048081459","1138675306","1138677367","1202213870","1104262947","1103757256","1102850356","1138675305","1103516148","1103748035","1025902842","1103511781","1103509583","1102232626","1100626708","1103752247","1102868925","1103750026","1103513838","1023530668","1103750732","1138678313","1104263365","1103520704","1138674273","1104268355","1103514224","1030243055","1030245715","1104264968","1103754219","1138677262","1052245125","1104264601","1103511714","1103755533","1138677875","1103512840","1102874689","1202214022","1202213766","1102869539","1103756663","1103751028","1103508084","1103509334","1103507287","1103754928","1102872914","1043463150","1138674856","1103510317","1104268067","1102849604","1138674419","1103509948","1103512318","1103509750","1104264025","1103518629","1103748906","1103510808","1231340085","1103509444","1104266203","1103508560","1104262857","1103513759","1103514312","1104262997","1104267019","1103514744","1103509587","1103756114","1187464478","1103514320","1102849638","1103756595"]:
        recaudoPD = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vSqcAIkMJVJi5ehJB9TtTaRktBfj9eTLXizEZQAUQThOXmLx-k8k4w686ZpP0fEbwzIkKryYc4SW3Dt/pub?gid=1830933640&single=true&output=csv')
        id_est=int(input_text)
        filtro = recaudoPD["ID"] == id_est
        my_filtro = recaudoPD[filtro]
        myFiltroSort = my_filtro.sort_values("Fecha")
        myFiltroSort[["Pago","Valor"]]=myFiltroSort[["Pago","Valor"]].applymap("{:,}".format)

        file1 = myFiltroSort[["Concepto","Fecha","Pago","Valor"]]

        f = open("recaudo.txt","w")
        f.write("ESTADO DE CUENTA"+"\n\n"+str("Estudiante:\n"+my_filtro.iloc[1,1])+'\n\n')
        f.write("Conceptos y pagos:\n")
        archivoJson = file1.to_json(orient="split")
        parsed = json.loads(archivoJson)

        with open('recaudo.json','w') as f:
            json.dump(parsed,f, indent=4)


        with open ('recaudo.json','r') as f:
            recaudo_json =json.load(f)

        for i in range(len(recaudo_json["data"])):
            print (recaudo_json["data"][i])

            with open ('recaudo.txt','a') as f:
                f.write("_______________________________"+'\n')
                f.write(str(recaudo_json["data"][i])+'\n')

        f=open("recaudo.txt","a")
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

        registro=open("recaudo.txt","r")
        f = open("recaudoText.txt","w")
        for x in registro:
            xf=x.replace("]","")
            f.write(xf)
        f.close()

        registro=open("recaudoText.txt","r")
        f = open("recaudoText1.txt","w")
        for x in registro:
            xf=x.replace("[","")
            f.write(xf)
        f.close()

        registro=open("recaudoText1.txt","r")
        f = open("recaudoText2.txt","w")
        for x in registro:
            xf=x.replace("🔴\', \'","🔴\nPlazo: ")
            f.write(xf)
        f.close()

        registro=open("recaudoText2.txt","r")
        f = open("recaudoText3.txt","w")
        for x in registro:
            xf=x.replace("\', \'0\', \'","\nValor a pagar: $")
            f.write(xf)
        f.close()

        registro=open("recaudoText3.txt","r")
        f = open("recaudoText4.txt","w")
        for x in registro:
            xf=x.replace("\'","")
            f.write(xf)
        f.close()

        registro=open("recaudoText4.txt","r")
        f = open("recaudoText5.txt","w")
        for x in registro:
            xf=x.replace("🟢, ","🟢\nFecha:")
            f.write(xf)
        f.close()

        registro=open("recaudoText5.txt","r")
        f = open("recaudoText6.txt","w")
        for x in registro:
            xf=x.replace(", 0","")
            f.write(xf)
        f.close()

        registro=open("recaudoText6.txt","r")
        f = open("recaudoText7.txt","w")
        for x in registro:
            xf=x.replace(", ","\nPagado: $")
            f.write(xf)
        f.close()

        f = open("recaudoText7.txt","r") 
        return f.read()

#Default 
    aleatorio = choice(["/help 💬","","","","","","","","","","","","","","","","","","","","","🟠🟢🔵🔴","🟧🟧🟧🟦🟦🟦🟩🟩🟩🟥🟥🟥","*•.¸♥️¸.•*´💖 *•.¸♥️¸.•*´*\nFeliz mes de las madres",""])
    
    return aleatorio