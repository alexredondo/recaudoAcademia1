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
#    intent_consulta_nuip = {"AARON ANDRES OVIEDO OVIEDO":"1030247719","ALAN SEBASTIAN GRANADOS GENEY":"1103754527","ALANIS FERNANDEZ ROMERO":"1103515254","ALICIA ISABEL ABUCHAR MONTERROZA":"1025555579","ANA BELEN RODRIGUEZ PEREZ":"1102847991","ANDRES SALIN GUERRA LAZARO":"1103510179","ANNA KAMILA PARRA GARCIA":"1043481075","ANTONELLA GOMEZ GOMEZ":"1103515205","ARIANA SOFIA BENAVIDES POLO":"1103748757","AVIGAIL MARTINEZ COVO":"1138677533","CALEB JOSE BOHORQUEZ MERCADO":"1103757793","CAMILA OSORIO BALLESTERO":"1103750555","CAMILO ANDRES ORTEGA CARRIAZO":"1102860979","CARLOS MARIO PALOMINO PUENTES":"1068435161","DAMIAN JESUS ROMERO BERTEL":"1103513122","DANIEL ANDRES PEREZ OVIEDO":"1104265422","DANIEL DAVID DIAZ TORRES":"1104263305","DANIELA GRAU FERNANDEZ":"1202214087","DARIANA MILLAN MONTES":"1103509838","DAVID ANDRES ORTEGA PEREZ":"1102872411","DILAN ANDRES CASTELLAR MOLINA":"1090486177","DYLAN MOISES BENAVIDES POLO":"1103754409","DYLLAN ALEJANDRO GRANADOS GENEY":"1202213348","ELENA JARABA PEREZ":"1138674376","ELIANA SALOME PATIÑO SOTO":"1103756941","EMANUEL CASAS DUQUE":"1027808387","EMELY SOFIA ALVAREZ MANGONES":"1103753690","EMILIO VILLALBA GARCIA":"1103756140","ESTEBAN JOSE MARTINEZ DIAZ":"1104267486","ESTEFANY BARRAGAN PARRA":"1103508124","ESTHER SOFIA MARTINEZ HERRERA":"1103758561","EVANYELITH ROLLERO BARRETO":"1202213742","EVELYN MARTINEZ ROYO":"1104264591","FATIMA LEMUS SALAZAR":"1103507608","GABRIEL TEJADA REALES":"1102873753","GABRIEL JOSE ARGUMEDO NAVARRO":"1104263333","GABRIEL JOSE CRUZ GARRIDO":"1224953137","GENESIS SOFIA COGOLLO OLMO":"1102856958","GERALDINE RIOS PEREZ":"1103748258","ISAAC DANIEL OBREGON BARRAGAN":"1138674413","ISAAC DAVID OLIVERA ARROYO":"1104265131","ISAAC DAVID VERGARA BARRETO":"1103749236","ISABEL SOFIA HERNANDEZ VERGARA":"1202213106","ISABELA SIERRA RICARDO":"1103752461","ISABELLA BUELVAS SINCELEJO":"1202213620","ISABELLA MONTES GARRIDO":"1103512107","ISABELLA RICARDO PACHECO":"1020123319","ISABELLA ROMERO GOMEZ":"1103519561","ISABELLA VERGARA CARMONA":"1231338199","ISAIAS DANIEL OLIVERA ARROYO":"1104267664","ISAIAS KALED ALVAREZ GUZMAN":"1103513624","JAILIS DIAZ GONZALEZ":"1103750756","JASMED GONZALEZ JASSAN":"1103506939","JAVIER ANDRES BUELVAS SANCHEZ":"1103749833","JERONIMO DIAZ GOMEZ":"1103511845","JESUS ANDRES SAEZ LARIOS":"1138674754","JESUS DAVID BARBOSA POLANCO":"1138674581","JESUS DAVID LUGO SANCHEZ":"1202213738","JOHN RAFAEL BRANGO VELASQUEZ":"1103515645","JONATHAN DAVID DIAZ RIVERA":"1102869604","JORGE ISAAC PALOMINO PUENTES":"1103517925","JOSHUA DAVID TORRES GARCIA":"1102860504","JOSUE HOYOS CARDENAS":"1030246017","JOSUE DAVID MONTES CHICA":"1043313558","JUAN DAVID BARRETO ESPINOSA":"1138676669","JUAN ESTEBAN GONZALEZ ALVAREZ":"1103508213","JUAN JOSE ORTEGA CARRIAZO":"1102878043","JUAN JOSE RICARDO DIAZ":"1103543553","JUAN LUCAS ACEVEDO ACOSTA":"1138677181","JUAN PABLO ORTEGA DIAZ":"1102313645","JUAN SEBASTIAN AMAYA MENESES":"1202213468","JULIAN JOSE SALCEDO VILLA":"1139434087","JULIAN MANUEL GUTIERREZ TUIRAN":"1103512911","JULIETA RUIZ PERALTA":"1104266694","JULIO ALBERTO ACUÑA GOEZ":"1042263697","JUSETH CAROLINA PACHECO TORRES":"1103748574","KATHERYN PEREZ ARRIETA":"1103753551","KEISY AYELEN IBAÑEZ BOLAÑO":"1125230534","KEREN LUCIA MEDINA MERLANO":"1202213662","KEYLER ANDRÉS HERNÁNDEZ VILLEGAS":"1103752312","KRISS MARIA KLARETH TOVAR GUERRA":"1104265781","LAUREN SOFIA PATIÑO SOTO":"1058357747","LEINA MARISSA FONTALVO JIMENEZ":"1103508816","LEYMAR MARIA CLARETH TOVAR GUERRA":"1103751941","LIZETH PAOLA SIERRA MILLAN":"1138674184","LORENA JUDITH VARGAS PERALTA":"1202214233","LUCAS GUEVARA GONZALEZ":"1103515651","LUCAS IVAN AMELL AGUILERA":"1103507961","LUCCIANA MONTES MARULANDA":"1103752763","LUCERO BARBOSA POLANCO":"1103513363","LUCIANA BERTEL MARMOLEJO":"1138677933","LUCIANA VILLALBA PEÑA":"1104265537","LUCIANA VALENTINA VEGA BORJA":"1103749443","LUIS MATEO SALAZAR PEREZ":"1201234938","LUIS SANTIAGO PEREZ ACOSTA":"1104262917","LUZ DE DIOS VERGARA RIVERO":"1103748954","MALIETH ALEJANDRA FERIA MARQUEZ":"1103748317","MARIA ANGELICA ALANDETE HERAZO":"1100397739","MARIA BELEN ARRAZOLA GARCIA":"1048081459","MARIA CAMILA GARCIA ORTEGA":"1138675306","MARIA CAMILA PESTANA MESA":"1138677367","MARIA ELENA HERNANDEZ VERGARA":"1202213870","MARIA JOSE CACERES CORRALES":"1104262947","MARIA PAULA IBAÑEZ BOLAÑO":"1103757256","MARIA SOFIA ALVAREZ SIERRA":"1102850356","MARIA SOFIA GARCIA ORTEGA":"1138675305","MARIANA CONTRERAS RUIZ":"1103516148","MARIANA JIMENEZ TAPIA":"1103748035","MARIANA VERBEL PATERNINA":"1025902842","MARIANA LUCIA TUIRAN GOMEZ":"1103511781","MARIANGEL GOMEZ PINEDA":"1103509583","MARTIN ORTEGA CARDENAS":"1102232626","MATEO CAUSADO DAVILA":"1100626708","MATEO DE AGUAS GALINDEZ":"1103752247","MATHIAS MERCADO OROZCO":"1102868925","MATIAS SALCEDO CALVO":"1103750026","MATIAS ANDRES ALTAMIRANDA RIVERO":"1103513838","MATIAS JOSE BOLAÑO CARABALLO":"1023530668","MAYTE ANDREA ABAD PETANO":"1103750732","MIA DE DIOS PAREDES ARRIETA":"1138678313","MICHELLE DAYANA VILLALBA CONTRERAS":"1104263365","MOISES OTERO PERDOMO":"1103520704","MOISES DAVID MEZA MENDOZA":"1138674273","MOISES DAVID PADILLA URIBE":"1104268355","NEYMAR ESCORCIA VITAL":"1103514224","NICOLE VARGAS CARMONA":"1030243055","NIKOLLE SOFIA HERNANDEZ BOHORQUEZ":"1030245715","NORELLA SOFIA CORDOBA FLOREZ":"1104264968","RACHELL BOHORQUEZ MERCADO":"1103754219","SALMA SALENA REYES MARTINEZ":"1138677262","SALOMÉ BOLIVAR MONCADA":"1052245125","SALOME CHADID GOMEZ":"1104264601","SALOMON OTERO PERDOMO":"1103511714","SAMANTHA SOFIA AGUDELO CANTERO":"1103755533","SAMUEL VERGARA CASAS":"1138677875","SAMUEL ALEJANDRO AMAYA MENESES":"1103512840","SAMUEL BONILLA CONTRERAS":"1102874689","SAMUEL DAVID BENAVIDES POLO":"1202214022","SAMUEL DAVID MONTES MARULANDA":"1202213766","SAMUEL ELIAS RODRIGUEZ PEREZ":"1102869539","SANTIAGO PIZARRO FAJARDO":"1103756663","SANTIAGO SALAZAR SALGADO":"1103751028","SANTIAGO ANDRES MARTINEZ NAIZIR":"1103508084","SANTIAGO ANDRES MONTERO GUERRERO":"1103509334","SANTIAGO ANDRES RIVERA MOSQUERA":"1103507287","SANTIAGO DAVID BLANCO OLIVERA":"1103754928","SANTIAGO DAVID VILLALBA NISPERUZA":"1102872914","SANTIAGO ENRIQUE PACHECO GOMEZ":"1043463150","SANTIAGO ISAAC GUERRA MARTINEZ":"1138674856","SANTIAGO JOSUE FERNANDEZ HOYOS":"1103510317","SARA NADJAR PASO":"1104268067","SARA SOFIA CURE MENDOZA":"1102849604","SARA SOFIA HERNANDEZ MONTES":"1138674419","SARA SOFIA SIERRA DE LIMA":"1103509948","SARA SOFIA VELASQUEZ ORTEGA":"1103512318","SARA VALENTINA CALDERIN RIOS":"1103509750","SARAH SOFIA PADILLA BALLESTERO":"1104264025","SARAH SOFIA VARGAS ROCHA":"1103518629","SARAH SOFIA VERBEL CONTRERAS":"1103748906","SAUL ANDRES PEREZ MARTINEZ":"1103510808","SCARLETT BOHORQUEZ MERCADO ":"1231340085","SEBASTIAN ALFONSO HERNANDEZ MARTINEZ":"1103509444","SEBASTIAN RODRIGUEZ GALLEGO":"1104266203","SIMON ANDRES ARRAZOLA GARCIA":"1103508560","SOFIA GOMEZ GOMEZ":"1104262857","SOFIA ELENA VILLERA REYES":"1103513759","TAHEEL SOFIA BARRIOS GUERRA":"1103514312","THALIANA CONTRERAS BERTEL":"1104262997","THALIANA JARABA RODRIGUEZ":"1104267019","THIAGO VELILLA DIAZ":"1103514744","VALENTINA SALCEDO MARQUEZ":"1103509587","VALERIA GONZALEZ ROMERO":"1103756114","VALERIA SOFIA SOTO SALGADO":"1187464478","VALERY SOFIA SIERRA MILLAN":"1103514320","VICTORIA SOFIA VERGARA PEÑALOZA":"1102849638","XIMENA PEREZ ARRIETA":"1103756595"}
#    if user_message_name in ("AARON ANDRES OVIEDO OVIEDO","ALAN SEBASTIAN GRANADOS GENEY","ALANIS FERNANDEZ ROMERO","ALICIA ISABEL ABUCHAR MONTERROZA","ANA BELEN RODRIGUEZ PEREZ","ANDRES SALIN GUERRA LAZARO","ANNA KAMILA PARRA GARCIA","ANTONELLA GOMEZ GOMEZ","ARIANA SOFIA BENAVIDES POLO","AVIGAIL MARTINEZ COVO","CALEB JOSE BOHORQUEZ MERCADO","CAMILA OSORIO BALLESTERO","CAMILO ANDRES ORTEGA CARRIAZO","CARLOS MARIO PALOMINO PUENTES","DAMIAN JESUS ROMERO BERTEL","DANIEL ANDRES PEREZ OVIEDO","DANIEL DAVID DIAZ TORRES","DANIELA GRAU FERNANDEZ","DARIANA MILLAN MONTES","DAVID ANDRES ORTEGA PEREZ","DILAN ANDRES CASTELLAR MOLINA","DYLAN MOISES BENAVIDES POLO","DYLLAN ALEJANDRO GRANADOS GENEY","ELENA JARABA PEREZ","ELIANA SALOME PATIÑO SOTO","EMANUEL CASAS DUQUE","EMELY SOFIA ALVAREZ MANGONES","EMILIO VILLALBA GARCIA","ESTEBAN JOSE MARTINEZ DIAZ","ESTEFANY BARRAGAN PARRA","ESTHER SOFIA MARTINEZ HERRERA","EVANYELITH ROLLERO BARRETO","EVELYN MARTINEZ ROYO","FATIMA LEMUS SALAZAR","GABRIEL TEJADA REALES","GABRIEL JOSE ARGUMEDO NAVARRO","GABRIEL JOSE CRUZ GARRIDO","GENESIS SOFIA COGOLLO OLMO","GERALDINE RIOS PEREZ","ISAAC DANIEL OBREGON BARRAGAN","ISAAC DAVID OLIVERA ARROYO","ISAAC DAVID VERGARA BARRETO","ISABEL SOFIA HERNANDEZ VERGARA","ISABELA SIERRA RICARDO","ISABELLA BUELVAS SINCELEJO","ISABELLA MONTES GARRIDO","ISABELLA RICARDO PACHECO","ISABELLA ROMERO GOMEZ","ISABELLA VERGARA CARMONA","ISAIAS DANIEL OLIVERA ARROYO","ISAIAS KALED ALVAREZ GUZMAN","JAILIS DIAZ GONZALEZ","JASMED GONZALEZ JASSAN","JAVIER ANDRES BUELVAS SANCHEZ","JERONIMO DIAZ GOMEZ","JESUS ANDRES SAEZ LARIOS","JESUS DAVID BARBOSA POLANCO","JESUS DAVID LUGO SANCHEZ","JOHN RAFAEL BRANGO VELASQUEZ","JONATHAN DAVID DIAZ RIVERA","JORGE ISAAC PALOMINO PUENTES","JOSHUA DAVID TORRES GARCIA","JOSUE HOYOS CARDENAS","JOSUE DAVID MONTES CHICA","JUAN DAVID BARRETO ESPINOSA","JUAN ESTEBAN GONZALEZ ALVAREZ","JUAN JOSE ORTEGA CARRIAZO","JUAN JOSE RICARDO DIAZ","JUAN LUCAS ACEVEDO ACOSTA","JUAN PABLO ORTEGA DIAZ","JUAN SEBASTIAN AMAYA MENESES","JULIAN JOSE SALCEDO VILLA","JULIAN MANUEL GUTIERREZ TUIRAN","JULIETA RUIZ PERALTA","JULIO ALBERTO ACUÑA GOEZ","JUSETH CAROLINA PACHECO TORRES","KATHERYN PEREZ ARRIETA","KEISY AYELEN IBAÑEZ BOLAÑO","KEREN LUCIA MEDINA MERLANO","KEYLER ANDRÉS HERNÁNDEZ VILLEGAS","KRISS MARIA KLARETH TOVAR GUERRA","LAUREN SOFIA PATIÑO SOTO","LEINA MARISSA FONTALVO JIMENEZ","LEYMAR MARIA CLARETH TOVAR GUERRA","LIZETH PAOLA SIERRA MILLAN","LORENA JUDITH VARGAS PERALTA","LUCAS GUEVARA GONZALEZ","LUCAS IVAN AMELL AGUILERA","LUCCIANA MONTES MARULANDA","LUCERO BARBOSA POLANCO","LUCIANA BERTEL MARMOLEJO","LUCIANA VILLALBA PEÑA","LUCIANA VALENTINA VEGA BORJA","LUIS MATEO SALAZAR PEREZ","LUIS SANTIAGO PEREZ ACOSTA","LUZ DE DIOS VERGARA RIVERO","MALIETH ALEJANDRA FERIA MARQUEZ","MARIA ANGELICA ALANDETE HERAZO","MARIA BELEN ARRAZOLA GARCIA","MARIA CAMILA GARCIA ORTEGA","MARIA CAMILA PESTANA MESA","MARIA ELENA HERNANDEZ VERGARA","MARIA JOSE CACERES CORRALES","MARIA PAULA IBAÑEZ BOLAÑO","MARIA SOFIA ALVAREZ SIERRA","MARIA SOFIA GARCIA ORTEGA","MARIANA CONTRERAS RUIZ","MARIANA JIMENEZ TAPIA","MARIANA VERBEL PATERNINA","MARIANA LUCIA TUIRAN GOMEZ","MARIANGEL GOMEZ PINEDA","MARTIN ORTEGA CARDENAS","MATEO CAUSADO DAVILA","MATEO DE AGUAS GALINDEZ","MATHIAS MERCADO OROZCO","MATIAS SALCEDO CALVO","MATIAS ANDRES ALTAMIRANDA RIVERO","MATIAS JOSE BOLAÑO CARABALLO","MAYTE ANDREA ABAD PETANO","MIA DE DIOS PAREDES ARRIETA","MICHELLE DAYANA VILLALBA CONTRERAS","MOISES OTERO PERDOMO","MOISES DAVID MEZA MENDOZA","MOISES DAVID PADILLA URIBE","NEYMAR ESCORCIA VITAL","NICOLE VARGAS CARMONA","NIKOLLE SOFIA HERNANDEZ BOHORQUEZ","NORELLA SOFIA CORDOBA FLOREZ","RACHELL BOHORQUEZ MERCADO","SALMA SALENA REYES MARTINEZ","SALOMÉ BOLIVAR MONCADA","SALOME CHADID GOMEZ","SALOMON OTERO PERDOMO","SAMANTHA SOFIA AGUDELO CANTERO","SAMUEL VERGARA CASAS","SAMUEL ALEJANDRO AMAYA MENESES","SAMUEL BONILLA CONTRERAS","SAMUEL DAVID BENAVIDES POLO","SAMUEL DAVID MONTES MARULANDA","SAMUEL ELIAS RODRIGUEZ PEREZ","SANTIAGO PIZARRO FAJARDO","SANTIAGO SALAZAR SALGADO","SANTIAGO ANDRES MARTINEZ NAIZIR","SANTIAGO ANDRES MONTERO GUERRERO","SANTIAGO ANDRES RIVERA MOSQUERA","SANTIAGO DAVID BLANCO OLIVERA","SANTIAGO DAVID VILLALBA NISPERUZA","SANTIAGO ENRIQUE PACHECO GOMEZ","SANTIAGO ISAAC GUERRA MARTINEZ","SANTIAGO JOSUE FERNANDEZ HOYOS","SARA NADJAR PASO","SARA SOFIA CURE MENDOZA","SARA SOFIA HERNANDEZ MONTES","SARA SOFIA SIERRA DE LIMA","SARA SOFIA VELASQUEZ ORTEGA","SARA VALENTINA CALDERIN RIOS","SARAH SOFIA PADILLA BALLESTERO","SARAH SOFIA VARGAS ROCHA","SARAH SOFIA VERBEL CONTRERAS","SAUL ANDRES PEREZ MARTINEZ","SCARLETT BOHORQUEZ MERCADO ","SEBASTIAN ALFONSO HERNANDEZ MARTINEZ","SEBASTIAN RODRIGUEZ GALLEGO","SIMON ANDRES ARRAZOLA GARCIA","SOFIA GOMEZ GOMEZ","SOFIA ELENA VILLERA REYES","TAHEEL SOFIA BARRIOS GUERRA","THALIANA CONTRERAS BERTEL","THALIANA JARABA RODRIGUEZ","THIAGO VELILLA DIAZ","VALENTINA SALCEDO MARQUEZ","VALERIA GONZALEZ ROMERO","VALERIA SOFIA SOTO SALGADO","VALERY SOFIA SIERRA MILLAN","VICTORIA SOFIA VERGARA PEÑALOZA","XIMENA PEREZ ARRIETA"):
#        return  intent_consulta_nuip[user_message_name]

#Consulta NAME ESTUDIANTE
#    intent_consulta_name = ["AARON ANDRES OVIEDO OVIEDO","ALAN SEBASTIAN GRANADOS GENEY","ALANIS FERNANDEZ ROMERO","ALICIA ISABEL ABUCHAR MONTERROZA","ANA BELEN RODRIGUEZ PEREZ","ANDRES SALIN GUERRA LAZARO","ANNA KAMILA PARRA GARCIA","ANTONELLA GOMEZ GOMEZ","ARIANA SOFIA BENAVIDES POLO","AVIGAIL MARTINEZ COVO","CALEB JOSE BOHORQUEZ MERCADO","CAMILA OSORIO BALLESTERO","CAMILO ANDRES ORTEGA CARRIAZO","CARLOS MARIO PALOMINO PUENTES","DAMIAN JESUS ROMERO BERTEL","DANIEL ANDRES PEREZ OVIEDO","DANIEL DAVID DIAZ TORRES","DANIELA GRAU FERNANDEZ","DARIANA MILLAN MONTES","DAVID ANDRES ORTEGA PEREZ","DILAN ANDRES CASTELLAR MOLINA","DYLAN MOISES BENAVIDES POLO","DYLLAN ALEJANDRO GRANADOS GENEY","ELENA JARABA PEREZ","ELIANA SALOME PATIÑO SOTO","EMANUEL CASAS DUQUE","EMELY SOFIA ALVAREZ MANGONES","EMILIO VILLALBA GARCIA","ESTEBAN JOSE MARTINEZ DIAZ","ESTEFANY BARRAGAN PARRA","ESTHER SOFIA MARTINEZ HERRERA","EVANYELITH ROLLERO BARRETO","EVELYN MARTINEZ ROYO","FATIMA LEMUS SALAZAR","GABRIEL TEJADA REALES","GABRIEL JOSE ARGUMEDO NAVARRO","GABRIEL JOSE CRUZ GARRIDO","GENESIS SOFIA COGOLLO OLMO","GERALDINE RIOS PEREZ","ISAAC DANIEL OBREGON BARRAGAN","ISAAC DAVID OLIVERA ARROYO","ISAAC DAVID VERGARA BARRETO","ISABEL SOFIA HERNANDEZ VERGARA","ISABELA SIERRA RICARDO","ISABELLA BUELVAS SINCELEJO","ISABELLA MONTES GARRIDO","ISABELLA RICARDO PACHECO","ISABELLA ROMERO GOMEZ","ISABELLA VERGARA CARMONA","ISAIAS DANIEL OLIVERA ARROYO","ISAIAS KALED ALVAREZ GUZMAN","JAILIS DIAZ GONZALEZ","JASMED GONZALEZ JASSAN","JAVIER ANDRES BUELVAS SANCHEZ","JERONIMO DIAZ GOMEZ","JESUS ANDRES SAEZ LARIOS","JESUS DAVID BARBOSA POLANCO","JESUS DAVID LUGO SANCHEZ","JOHN RAFAEL BRANGO VELASQUEZ","JONATHAN DAVID DIAZ RIVERA","JORGE ISAAC PALOMINO PUENTES","JOSHUA DAVID TORRES GARCIA","JOSUE HOYOS CARDENAS","JOSUE DAVID MONTES CHICA","JUAN DAVID BARRETO ESPINOSA","JUAN ESTEBAN GONZALEZ ALVAREZ","JUAN JOSE ORTEGA CARRIAZO","JUAN JOSE RICARDO DIAZ","JUAN LUCAS ACEVEDO ACOSTA","JUAN PABLO ORTEGA DIAZ","JUAN SEBASTIAN AMAYA MENESES","JULIAN JOSE SALCEDO VILLA","JULIAN MANUEL GUTIERREZ TUIRAN","JULIETA RUIZ PERALTA","JULIO ALBERTO ACUÑA GOEZ","JUSETH CAROLINA PACHECO TORRES","KATHERYN PEREZ ARRIETA","KEISY AYELEN IBAÑEZ BOLAÑO","KEREN LUCIA MEDINA MERLANO","KEYLER ANDRÉS HERNÁNDEZ VILLEGAS","KRISS MARIA KLARETH TOVAR GUERRA","LAUREN SOFIA PATIÑO SOTO","LEINA MARISSA FONTALVO JIMENEZ","LEYMAR MARIA CLARETH TOVAR GUERRA","LIZETH PAOLA SIERRA MILLAN","LORENA JUDITH VARGAS PERALTA","LUCAS GUEVARA GONZALEZ","LUCAS IVAN AMELL AGUILERA","LUCCIANA MONTES MARULANDA","LUCERO BARBOSA POLANCO","LUCIANA BERTEL MARMOLEJO","LUCIANA VILLALBA PEÑA","LUCIANA VALENTINA VEGA BORJA","LUIS MATEO SALAZAR PEREZ","LUIS SANTIAGO PEREZ ACOSTA","LUZ DE DIOS VERGARA RIVERO","MALIETH ALEJANDRA FERIA MARQUEZ","MARIA ANGELICA ALANDETE HERAZO","MARIA BELEN ARRAZOLA GARCIA","MARIA CAMILA GARCIA ORTEGA","MARIA CAMILA PESTANA MESA","MARIA ELENA HERNANDEZ VERGARA","MARIA JOSE CACERES CORRALES","MARIA PAULA IBAÑEZ BOLAÑO","MARIA SOFIA ALVAREZ SIERRA","MARIA SOFIA GARCIA ORTEGA","MARIANA CONTRERAS RUIZ","MARIANA JIMENEZ TAPIA","MARIANA VERBEL PATERNINA","MARIANA LUCIA TUIRAN GOMEZ","MARIANGEL GOMEZ PINEDA","MARTIN ORTEGA CARDENAS","MATEO CAUSADO DAVILA","MATEO DE AGUAS GALINDEZ","MATHIAS MERCADO OROZCO","MATIAS SALCEDO CALVO","MATIAS ANDRES ALTAMIRANDA RIVERO","MATIAS JOSE BOLAÑO CARABALLO","MAYTE ANDREA ABAD PETANO","MIA DE DIOS PAREDES ARRIETA","MICHELLE DAYANA VILLALBA CONTRERAS","MOISES OTERO PERDOMO","MOISES DAVID MEZA MENDOZA","MOISES DAVID PADILLA URIBE","NEYMAR ESCORCIA VITAL","NICOLE VARGAS CARMONA","NIKOLLE SOFIA HERNANDEZ BOHORQUEZ","NORELLA SOFIA CORDOBA FLOREZ","RACHELL BOHORQUEZ MERCADO","SALMA SALENA REYES MARTINEZ","SALOMÉ BOLIVAR MONCADA","SALOME CHADID GOMEZ","SALOMON OTERO PERDOMO","SAMANTHA SOFIA AGUDELO CANTERO","SAMUEL VERGARA CASAS","SAMUEL ALEJANDRO AMAYA MENESES","SAMUEL BONILLA CONTRERAS","SAMUEL DAVID BENAVIDES POLO","SAMUEL DAVID MONTES MARULANDA","SAMUEL ELIAS RODRIGUEZ PEREZ","SANTIAGO PIZARRO FAJARDO","SANTIAGO SALAZAR SALGADO","SANTIAGO ANDRES MARTINEZ NAIZIR","SANTIAGO ANDRES MONTERO GUERRERO","SANTIAGO ANDRES RIVERA MOSQUERA","SANTIAGO DAVID BLANCO OLIVERA","SANTIAGO DAVID VILLALBA NISPERUZA","SANTIAGO ENRIQUE PACHECO GOMEZ","SANTIAGO ISAAC GUERRA MARTINEZ","SANTIAGO JOSUE FERNANDEZ HOYOS","SARA NADJAR PASO","SARA SOFIA CURE MENDOZA","SARA SOFIA HERNANDEZ MONTES","SARA SOFIA SIERRA DE LIMA","SARA SOFIA VELASQUEZ ORTEGA","SARA VALENTINA CALDERIN RIOS","SARAH SOFIA PADILLA BALLESTERO","SARAH SOFIA VARGAS ROCHA","SARAH SOFIA VERBEL CONTRERAS","SAUL ANDRES PEREZ MARTINEZ","SCARLETT BOHORQUEZ MERCADO ","SEBASTIAN ALFONSO HERNANDEZ MARTINEZ","SEBASTIAN RODRIGUEZ GALLEGO","SIMON ANDRES ARRAZOLA GARCIA","SOFIA GOMEZ GOMEZ","SOFIA ELENA VILLERA REYES","TAHEEL SOFIA BARRIOS GUERRA","THALIANA CONTRERAS BERTEL","THALIANA JARABA RODRIGUEZ","THIAGO VELILLA DIAZ","VALENTINA SALCEDO MARQUEZ","VALERIA GONZALEZ ROMERO","VALERIA SOFIA SOTO SALGADO","VALERY SOFIA SIERRA MILLAN","VICTORIA SOFIA VERGARA PEÑALOZA","XIMENA PEREZ ARRIETA"]
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

#Emojis
    intent_emoji = ("👏👏","excelente","⭐️⭐️","👍👍")
    for emoji in intent_emoji:
        aleatorio_emocion_emoji = choice(["Maravilloso 🌺","Genial 🌻","Me gusta 🌷"])
        if re.search(emoji, user_message) is not None:
            return aleatorio_emocion_emoji

#Agradecimiento
    if user_message in ("muchas gracias","thanks you","gracias teacher"):
        aleatorio_gracias = choice(["🧡💚💙❤️","🟠🟢🔵🔴","Wonderfull 💫","Genial 👌🏽","Me gusta 👍🏽","Maravilloso 🌺","🌼","🌻","💐"])
        return aleatorio_gracias

# Medios de pago
    if user_message in ("medios de pago", "medio de pago"):
        medio_de_pago = """\n
Hola 🌺,\n\n Para conocer los medios de pago vaya a /mediodepago\n"""
        return medio_de_pago

# Pago por pse
    if user_message in ("pago por internet", "pago por pse", "pse","pagar por pse"):
        pago_pse = """\n\n
    🏦 Para pagar por internet puede usar este : \n
    [link de pago por PSE](https://www.mipagoamigo.com/MPA_WebSite/ServicePayments/StartPayment?id=4510&searchedCategoryId=&searchedAgreementName=ACADEMIA%20DE%20LAS%20AMERICAS)"""
        return pago_pse

#Evidencia pago    
    if user_message in ("👍*","👍**"):
        mensaje_pago_recibido=("*Muchas gracias!*\n\n📬 Al *_correo_* se le envía el recibo de caja ")
        
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
    
            return  "por favor ingrese a este link: \n\n   /cuenta"

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

# Genera horario
    if user_message in ("horario primero", "horario 1"):  # solicitud del usuario
        link_horario = "https://telegra.ph/First-Class-Schedule-01-27\n\n  La hora de entrada: 6:20 am\nLa hora de salida: 1:10 pm"
        return link_horario

# Lista de estudiantes que se le entrega el kit
    if user_message in ("kitsi","kit si"):  # solicitud del usuario
        list_student = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=1350193451&single=true&output=csv')  # variable con tabla de datos se trae de googlesheet. Hoja compartida como archivo CSV.
        genera_lista()
        # apertura del archivo para impresión
        f = open("list_student_text_3.txt", "r", encoding="utf-8")
        return "Estudiantes que pagaron el kit.\n\n"+"*Grado | Estudiante | Entrega?*\n"+ f.read()  # imprime

# Lista de estudiantes pendientes por pagar el kit
    if user_message in ("kitno", "kit no"):  # solicitud del usuario
        list_student = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/e/2PACX-1vQyGXMDTSbh_vXeYVpkFF91ARGNYMKvYM27LfuFn35SJ78ja7ARPIhlQ9GU_hUOz596HIfQLo9L45_u/pub?gid=925366367&single=true&output=csv')  # variable con tabla de datos se trae de googlesheet. Hoja compartida como archivo CSV.
        genera_lista()
        # apertura del archivo para impresión
        f = open("list_student_text_3.txt", "r", encoding="utf-8")
        return "Formulario para registrar:  \n"+"[link](https://docs.google.com/spreadsheets/d/11P7-Eq_MGWGSjqirMawN3pS0t6Jsc5W4fb6UfGUeqQI/edit#gid=1350193451)\n"+"Estudiantes que pagaron el kit.\n\n" + "Grado | Estudiante\n"+ f.read()  # imprime

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
🌱 Próximamente sede campestre.

[Link](www.academia.edu.co)"""  # imprime
#Estado de cuenta
    if user_message in ["1001368730091","566823099","740479597","774961259","752044425","594244247","1001278091682","734477373","611306758","1001264500088","510276625","560957978","790584346","587492183","633478750","662072738","710900500","698079942","732978397","723545874","1001338979168","1001266243352","1001445422887","563619371","1001470298709","545054499","1001211791436","581778935","1001221364964","756678131","439651001","676845958","1001274258420","612122202","1001167380937","637490155","672121967","422965172","640252592","599226510","1001302901969","528328293","776155007","1001267993107","477108352","1001410910756","1001283899591","757466026","1001495905419","599089927","748250659","623339134","1001440528243","748183480","568864068","1001196292071","501580454","1001207414865","752083719","545183138","1076512291","451366432","1001189318617"]:
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

#Default 
    aleatorio = ""#choice(["/help 💬","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","🟠🟢🔵🔴",""])
    
    return aleatorio