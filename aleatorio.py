import random
repetidas = []
repetidasTel = []
repetidasCPF = []
repetidasRG = []
def nomes():
    nomes = ("Roberto","Maricio", "Silvio", "Wagner", "Silvia", "Joana", "Marina","Nubia")
    pos = random.randint(0, (len(nomes)-1))
    return nomes[pos]

def sobrenomes(): 
    sobrenomes = (" da Silva", "Oliveira", "Machado", "dos Santos", "Fraga", "Moura", "Menezes")
    pos = random.randint(0, (len(sobrenomes)-1))
    return sobrenomes[pos]
def estadoCivil(idade):
    estadoCivil = ("solteiro","namorando","casado")
    
    if idade <= 12:
        pos = 0
    elif idade > 12 and idade >= 18:
        pos = random.randint(0,1)
    else:
        pos = random.randint(0,(len(estadoCivil)-1))
    return estadoCivil[pos]
def sexoBiologico():
    sexoBiologico = ("M","F","I")
    pos = random.randint(0, (len(sexoBiologico)-1))
    return sexoBiologico[pos]

def tipoSanguineo():
    tipoSanguineo = ("A+","A-","O+","O-","AB+","AB-","B+","B-")
    pos = random.randint(0, (len(tipoSanguineo)-1))
    return tipoSanguineo[pos]

def ids():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 8:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    while repetidas.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidas.append(num)
    
    return num
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
    
    return num

def Tel():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 8:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    while repetidasTel.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidasTel.append(num)

def Ddd():
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    ddd = ""
    while i < 2:
        pos = random.randint(0, (len(numeros)-1))
        ddd = ddd + str(pos)
        i = i + 1
        return ddd

#------------------------------------------------------------------------------------------------------------------
# escolher aleatoriamente idades
def idadeInfanto():
    idade = random.randint(1,17)
    return idade

def idadeAdulto():
    idade = random.randint(18,59)
    return idade

def idadeIdoso():
    idade = random.randint(60,107)
    return idade

idadeInfanto = idadeInfanto()
idadeAdulto = idadeAdulto()
idadeIdoso = idadeIdoso()

geracao = [idadeInfanto,idadeAdulto,idadeIdoso]



# pega uma idade para definir o ano de nascimento 
def idades():
    pos = random.randint(0, (len(geracao)-1))
        
    return geracao[pos]





def dataNascimento(idade):
    anoNascimento = 2023 - idade
    anoNascimento = str(anoNascimento)
    data = anoNascimento + "-"
    mes = random.randint(1,12)
    mes = str(mes)
    data = data + mes + "-"
    dia = random.randint(1,30)
    dia = str(dia)
    data = data + dia
     
    return data



def dataInscricao(idade):
    
    dataNascimento = 2023 - idade
    anoInscricao = random.randint(1900, 2023)
    while anoInscricao < dataNascimento:
        idade = random.randint(1,30)
        anoInscricao = 2023 - idade
    anoInscricao = str(anoInscricao)
    data = anoInscricao + "-"
    mes = random.randint(1,12)
    mes = str(mes)
    data = data + mes + "-"
    dia = random.randint(1,30)
    dia = str(dia)
    data = data + dia 
      
    return data



def Altura(novaidade):
    if novaidade <= 3:
        altura =  random.uniform(0.2,0.8)
        altura = round(altura,2)
    elif novaidade > 3 and novaidade <= 8:
        altura = random.uniform(0.5, 1.20)
        altura = round(altura,2)
    elif novaidade > 8 and novaidade <=14:
        altura = random.uniform(0.8, 1.7)
        altura = round(altura,2)
    elif novaidade > 14:
        altura = random.uniform(1.2,2.3)
        altura = round(altura,2)
    return altura

def Peso(novaidade):
    if novaidade <= 3:
        peso =  random.uniform(0, 5)
        peso = round(peso,1)
    elif novaidade > 3 and novaidade <= 8:
        peso = random.uniform(10, 30)
        peso = round(peso,1)
    elif novaidade > 8 and novaidade <=14:
        peso = random.uniform(30, 80)
        peso = round(peso,1)
    elif novaidade > 14:
        peso = random.uniform(50, 120)
        peso = round(peso,1)
    return peso



#-------------------------------------------------------------------------------------------------------------------------------------

def escolaridadePaciente(idade):
    escolaridade = ("nulo","Analfabeto","5º Ano Incompleto","5º Ano Completo","6º ao 9º Ano do Fundamental","Fundamental Completo","Médio Incompleto","Médio Completo","Superior Incompleto","Superior Completo","Mestrado","Doutorado")
    if idade <= 7:
        pos = 0
    elif idade > 7 and idade <= 17:      
        pos = random.randint(1, 7)
    elif idade > 17 and idade <=25:
        pos = random.randint(1,10)
    else:
        pos = random.randint(1,(len(escolaridade)-1))
    
    return escolaridade[pos]


