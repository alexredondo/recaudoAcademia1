import datetime
import requests
import json
import csv

#Muestra la fecha de ejecución
fechaEjecucion = datetime.datetime.now()

print("\n_____________________________________________________________________")
print("\n\n\nFecha del estado de cuenta: "+str(fechaEjecucion)+"\n")
print ("Centro Educativo Academia de las Américas\n\n")
print ("ESTADO DE CUENTA\n\n")


#filtro por estudiante
#id_est = int(input("Nuip del Estudiante:"))
#id_est = 1138678313

#Obtener el archivo en csv, compartido en drive
recaudo = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSqcAIkMJVJi5ehJB9TtTaRktBfj9eTLXizEZQAUQThOXmLx-k8k4w686ZpP0fEbwzIkKryYc4SW3Dt/pub?gid=1830933640&single=true&output=csv')

url_content = recaudo.content

csv_file =open('downloaded.csv','wb')
csv_file.write(url_content)

with open('downloaded.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    data= {"recaudos": []}
    for row in reader:
        data["recaudos"].append({"ID": row[0], "Estudiante":row[1], "Fecha":row[2], "Pago":row[3], "Valor":row[4], "Concepto":row[5]})
        
with open('recaudo.json','w') as f:
   json.dump(data,f, indent=4)

with open ('recaudo.json','r') as f:
    recaudo_json =json.load(f)

registros = recaudo_json["recaudos"][0]

clave = registros.keys()
valor = registros.values()
cantidad_datos = registros.items()

for clave, valor in cantidad_datos:


        print (clave + ": " + valor)

#for i in [1,2]:

 #   print (i)
 #   reg = recaudo_json["recaudos"][i]
#    print (reg)

for i in range(len(recaudo_json["recaudos"])):

    if recaudo_json["recaudos"][i]["ID"]==1103517925:

        print ("Done")
    print (recaudo_json["recaudos"][i]["Estudiante"])
print (recaudo_json["recaudos"][0]["Estudiante"])
print (recaudo_json["recaudos"][0].values())
print (len(recaudo_json["recaudos"]))

#print ("\n\n========= Totales ==========\n")
#print ("Total Costos Educativos: $ {:,}".format(totalValor))
#print ("Pagado: $ {:,}".format(totalPago))

#pendiente = totalValor - totalPago

#print("Pendiente por pagar:$ {:,}\n\n\n".format(pendiente))
print("\n_____________________________________________________________________")

