import random
import csv

def descricao():
    descricaoRemedio =["Tratamento de doenças cardíacas.","Alívio de enxaquecas.","Redução da pressão arterial.","Controle de diabetes.","Prevenção de infecções.","Tratamento de alergias sazonais.","Alívio de dores de cabeça.",
                   "Redução de febre.","Tratamento de problemas de tireoide.","Alívio de dores nas costas.","Tratamento de acne.","Supressão de tosse.","Controle de ansiedade.","Alívio de náusea.","Tratamento de artrite.",
                   "Promoção da saúde óssea.","Redução da inflamação.","Prevenção de coágulos sanguíneos.","Tratamento de insônia.","Alívio de dores musculares.","Controle de asma.","Tratamento de problemas de pele.","Redução de colesterol."
                   ,"Prevenção de enjoo de movimento.","Alívio de cólicas menstruais.","Tratamento de infecções do trato urinário.","Controle de pressão intraocular.","Alívio de dores nas articulações.","Tratamento de alergias alimentares.",
                   "Promoção de perda de peso.","Prevenção de osteoporose.","Tratamento de queimaduras solares.","Alívio de ressacas.","Controle de doenças autoimunes.","Tratamento de infecções respiratórias.","Redução de alergias a animais de estimação.",
                   "Prevenção de enxaquecas crônicas.","Tratamento de depressão.","Alívio de dores de dente.","Controle de doença de Crohn.","Tratamento de infecções oculares.","Promoção da saúde cardiovascular.","Redução de sintomas de gripe.",
                   "Prevenção de alergias sazonais.","Tratamento de psoríase.","Alívio de dores na garganta.","Controle de hipertensão.","Tratamento de infecções fúngicas.","Redução de sintomas de alergias sazonais.","Prevenção de enxaquecas por tensão."]
    pos = random.randint(0,len(descricaoRemedio)-1)
    
    return descricaoRemedio[pos]


def CodBarras():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 13:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    return num


def geradorDeCSV(caminho,listaDic):            
    with open(caminho, 'w', newline='', encoding='utf-8') as file_csv:
            csv_writer = csv.DictWriter(file_csv, fieldnames=listaDic[0].keys())
            csv_writer.writeheader()
            for line in listaDic:
                csv_writer.writerow(line)