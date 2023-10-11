import random
import datetime as dt

hoje = dt.date.today()

def idEstado():
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    ddd = ""
    while i < 2:
        pos = random.randint(0, (len(numeros)-1))
        ddd = ddd + str(pos)
        i = i + 1
    return ddd
result = idEstado()
print(result)

def estados():
    estados = ("Acre","Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal","Espírito Santo","Goiás","Maranhão",
               "Mato Grosso","Mato Grosso do Sul","Minas Gerais","Pará","Paraíba","Paraná","Pernambuco","Piauí","Rio de Janeiro",
               "Rio Grande do Norte","Rio Grande do Sul","Rondônia","Roraima","Santa Catarina","São Paulo","Sergipe","Tocantins")
    pos = random.randint(0, (len(estados)-1))
    return estados[pos]
def dicestados():
    estados={}
    estados['Acre']
    estados['Alagoas']
    estados['Amapá']
    estados['Amazonas']
    estados['Bahia']
    estados['Ceará']
    estados['Distrito Federal']
    estados['Espírito Santo']
    estados['Goiás']
    estados['Maranhão']
    estados['Mato Grosso']
    estados['Mato Grosso do Sul']
    estados['Minas Gerais']
    estados['"Pará']
    estados['Paraíba']
    estados['Pernambuco']
    estados['Piauí']
    estados['Rio de Janeiro']
    estados['Rio Grande do Norte']
    estados['']


def siglas(estado):
    estado = estado
    if estado == "Acre":
        sigla = "AC"
    elif estado == "Alagoas":
        sigla = "AL"
    elif estado== "Amapá":
        sigla ="AP"
    elif estado == "Amazonas":
        sigla = "AM"
    elif estado == "Bahia":
        sigla = "BA"
    elif estado == "Ceará":
        sigla = "CE"
    elif estado == "Distrito Federal":
        sigla = "DF"
    elif estado == "Espírito Santo":
        sigla = "ES"
    elif estado == "Goiás":
        sigla = "GO"
    elif estado == "Maranhão":
        sigla = "MA"
    elif estado == "Mato Grosso":
        sigla = "MT"
    elif estado == "Mato Grosso do Sul":
        sigla = "MS"
    elif estado == "Minas Gerais":
        sigla = "MG"
    elif estado == "Pará ":
        sigla = "PA"
    elif estado == "Paraíba":
        sigla = "PB"
    elif estado == "Paraná":
        sigla = "PR"
    elif estado == "Pernambuco":
        sigla = "PE"
    elif estado == "Piauí":
        sigla = "PI"
    elif estado == "Rio de Janeiro":
        sigla = "RJ"
    elif estado == "Rio Grande do Norte":
        sigla = "RN"
    elif estado == "Rio Grande do Sul":
        sigla = "RS"
    elif estado == "Rondônia":
        sigla = "RO"
    elif estado == "Roraima":
        sigla = "RR"
    elif estado == "Santa Catarina":
        sigla = "SC"
    elif estado == "São Paulo":
        sigla = "SP"
    elif estado == "Sergipe":
        sigla = "SE"
    elif estado == "Tocantins":
        sigla = "TO"
    
    return sigla

