import pandas as pd
import codecs

import csv
#dicRG = pd.read_csv('medicine_dataset2.csv', header=None, index_col=0).to_dict()
#print(dicRG)

 #retornar uma lista de listas
#with open('medicine_dataset2.csv',"r") as csvfile:
    #reader = csv.reader(csvfile)
    #lista = list(reader)

#print(lista[3])

#df = pd.read_csv('rgteste.csv')
#inform = df[2]
#print(inform)

listaRemedios =[]
   
listaDicRemedios =[]   
with open('medicine_dataset2.csv',mode ="r",encoding="utf-8") as inp:
    reader = csv.reader(inp, delimiter=',')
    for i, linha in enumerate(reader):
        print(i)
        if i !=0 or i > 100002:
            listaRemedios.append(linha[1])
        
        if i >= 100002:
            break
         
        
def dicRemedios(valor):   
    dicRemedios ={}
    dicRemedios['remedio'] = valor
    return dicRemedios

for i in range(len(listaRemedios)):
    listaDicRemedios.append(dicRemedios(listaRemedios[i]))

print(listaDicRemedios)

with open('remedios.csv', 'w', newline='', encoding='utf-8') as file_csv:
        # Criando objeto de Escrita do CSV
        csv_writer = csv.DictWriter(file_csv, fieldnames=listaDicRemedios[0].keys())

        # Escrevendo headers (Nome das colunas do CSV)
        csv_writer.writeheader()

        # Percorrendo o dicionario de dados
        for line in listaDicRemedios:
            # Escrevendo linha por linha
            csv_writer.writerow(line)

def geradorDeCSV(caminho,listaDic):            
    with open(caminho, 'w', newline='', encoding='utf-8') as file_csv:
            csv_writer = csv.DictWriter(file_csv, fieldnames=listaDic[0].keys())
            csv_writer.writeheader()
            for line in listaDic:
                csv_writer.writerow(line)
    