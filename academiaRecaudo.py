import pandas as pd
import datetime

#Muestra la fecha de ejecución
fechaEjecucion = datetime.datetime.now()
print("Fecha de Ejecución: "+str(fechaEjecucion))

#Obtener el archivo en csv, compartido en drive
recaudoPD = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vSqcAIkMJVJi5ehJB9TtTaRktBfj9eTLXizEZQAUQThOXmLx-k8k4w686ZpP0fEbwzIkKryYc4SW3Dt/pub?gid=1830933640&single=true&output=csv')

#filtro por estudiante
#id_est = int(input())
id_est = 1138678313
filtro = recaudoPD["ID"] == id_est
my_filtro = recaudoPD[filtro]
print (my_filtro.sort_values("Fecha"))

#my_filtro = pd.to_numeric(my_filtro.Pago)
#my_filtro = pd.to_numeric(my_filtro.Valor)
totalPago = my_filtro.Pago.sum(axis=0)
totalValor = my_filtro.Valor.sum(axis=0)

print ("_____ Totales _____")
print ("Pagado: $"+str(totalPago))
print ("Conceptos: $"+str(totalValor))
pendiente = totalPago + totalValor
print("Pendiente por pagar: $"+str(pendiente))

print(recaudoPD.dtypes)
#print(recaudoResumen.info())
#print(recaudoResumen.head())
#print(recaudoResumen.tail())


