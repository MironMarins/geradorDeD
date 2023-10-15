import pandas as pd

import csv
#dicRG = pd.read_csv('rgteste.csv', header=None, index_col=0, squeeze=True).to_dict()
#print(dicRG)

# retornar uma lista de listas
with open('primarios\\T_RHSTU_PACIENTE\\rg.csv',"r") as csvfile:
    reader = csv.reader(csvfile)
    lista = list(reader)

print(lista[3])

#df = pd.read_csv('rgteste.csv')
#inform = df[2]
#print(inform)

