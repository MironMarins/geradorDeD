import csv
import random
repetidasRG = []
repetidasCPF = []
dicCPF = {}
dicRG = {}
ListaDicRg = []


def Cpf():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 11:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    
    while repetidasCPF.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 11:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidasCPF.append(num)
    repetidasCPF.sort()
    return num
def Rg():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 11:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    while repetidasRG.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 11:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidasRG.append(num)
    repetidasRG.sort()
    
    return num
for i in range(0,10):
    identidade = Rg()




for i in range(len(repetidasRG)):
    dicRG['rg'] = repetidasRG
ListaDicRg.append(dicRG)
    


print(ListaDicRg)


# Criando arquivo
with open('rg.csv', 'w', newline='', encoding='utf-8') as file_csv:
        # Criando objeto de Escrita do CSV
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaDicRg[0].keys())

        # Escrevendo headers (Nome das colunas do CSV)
        csv_writer.writeheader()

        # Percorrendo o dicionario de dados
        for line in ListaDicRg:
            # Escrevendo linha por linha
            csv_writer.writerow(line)

