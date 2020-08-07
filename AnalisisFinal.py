import pandas as pd
import requests
import json

cantidad=int(input("Introduzca el numero de acciones para analizar: "))

for n in range(0,cantidad):
    simbolo = input("Introduzca el ticket: ")
    # bs= requests.get("https://financialmodelingprep.com/api/v3/cash-flow-statement/"+simbolo+"?apikey=9ac35ab14518cc23649921416cd19b11")
    simb = requests.get("https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/" + simbolo + "?apikey=9ac35ab14518cc23649921416cd19b11")
    simb = simb.json()
    simb = simb["financials"]
    simb = pd.DataFrame.from_dict(simb)
    #simb=simb[["date","Total current liabilities","Total current assets","Total liabilities","Total assets"]]
    simb = simb[["date","Total current liabilities", "Total current assets", "Total liabilities", "Total assets"]]
    #simb=simb["Total current assets"].astype("float")
    #simb=simb["Total current liabilities"].astype("float")
    #simb["Caja Neta"]= simb["Total current assets"]-simb["Total current liabilities"]
    simb.to_excel(simbolo + "_export_Financial.xlsx", index=False)
    print(simb)