import pandas as pd
import json

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi",):
        return "Hey"
    if user_message in ("hola", ):
        return "Que tal"

    if user_message in ("estado de cuenta","Estado de cuenta"):

        return "nuip"

    if user_message in ("1138678313"):
        id_est = int(input_text)
        recaudoPD = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vSqcAIkMJVJi5ehJB9TtTaRktBfj9eTLXizEZQAUQThOXmLx-k8k4w686ZpP0fEbwzIkKryYc4SW3Dt/pub?gid=1830933640&single=true&output=csv')
        filtro = recaudoPD["ID"] == id_est
        my_filtro = recaudoPD[filtro]
        print(my_filtro.sort_values("Fecha"))
        return "este es mi *texto*",{parse_mode : "Markdown"}
    #my_filtro.to_json()



    return "No tengo respuesta"

