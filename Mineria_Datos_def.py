import pandas as pd
print("Bienvenido, por favor, indique el nombre del archivo, recuerde que el formato debe ser CSV (en ingles)")


def cargar(activo):
    carga = pd.read_csv(activo + ".csv", parse_dates=True, sep=",")
    acc=input("¿Quiere exportar el archivo?, solo responda: si o no. ")
    carga["Date"] = pd.to_datetime(carga["Date"])
    #carga[["Date", "High", "Low", "Close"]].round(decimals=2)

    carga= carga[["Date", "High", "Low", "Close", "Adj Close", "Open"]] #Nos quedamos con las columnas que necesitamos
    carga["resultado"]=(carga["Close"]-carga["Open"])/100
    if acc == "si":
        carga.to_excel(activo+"_export.xlsx", index=False)
    else:
        print(carga)
    return carga

contador = range(int(input("Por favor, ¿que cantidad de activos desea cargar?")))

for n in contador:
    activo = input("Por favor, introduzca el nombre del activo que desea cargar, sin la extension")
    activoLoad = cargar(activo) #Cargamos el CSV original
    tipoDato=input("¿Desea comprobar que tipos de datos hay en el Data Set?, Solo responda: ¿si o no? ")
    if tipoDato=="si":
        print(activoLoad.dtypes)


#Añadir una columna que construya la diferencia entre el precio de cierre y el de apertura

