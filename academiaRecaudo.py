import pandas as pd
import datetime

#Muestra la fecha de ejecución
fechaEjecucion = datetime.datetime.now()

print("\n_____________________________________________________________________")
print("\n\n\nFecha del estado de cuenta: "+str(fechaEjecucion)+"\n")
print ("Centro Educativo Academia de las Américas\n\n")
print ("ESTADO DE CUENTA\n\n")


#filtro por estudiante
id_est = int(input("Nuip del Estudiante:"))
#id_est = 1138678313

#Obtener el archivo en csv, compartido en drive
recaudoPD = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vSqcAIkMJVJi5ehJB9TtTaRktBfj9eTLXizEZQAUQThOXmLx-k8k4w686ZpP0fEbwzIkKryYc4SW3Dt/pub?gid=1830933640&single=true&output=csv')

filtro = recaudoPD["ID"] == id_est
my_filtro = recaudoPD[filtro]
print (my_filtro.sort_values("Fecha"))

#my_filtro = pd.to_numeric(my_filtro.Pago)
#my_filtro = pd.to_numeric(my_filtro.Valor)
totalPago = my_filtro.Pago.sum(axis=0)
totalValor = my_filtro.Valor.sum(axis=0)

print ("\n\n========= Totales ==========\n")
print ("Total Costos Educativos: $ {:,}".format(totalValor))
print ("Pagado: $ {:,}".format(totalPago))

pendiente = totalValor - totalPago

print("Pendiente por pagar:$ {:,}\n\n\n".format(pendiente))
print("\n_____________________________________________________________________")

#print(recaudoPD.dtypes)
#print(recaudoResumen.info())
#print(recaudoResumen.head())
#print(recaudoResumen.tail())


