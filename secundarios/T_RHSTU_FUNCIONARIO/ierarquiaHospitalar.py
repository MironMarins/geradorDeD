import aleatorioFuncionario



hierarquiaHosp = []






def presiDic(numero,nome,subalterno):
    presidente ={}
    presidente['numero'] = numero
    presidente['nome'] = nome
    presidente['cargo'] = "presidente"
    presidente['subalterno'] = subalterno
    return presidente
#listaPresidente.append(presiDic(1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),))
def dretorDic(numero,nome,subalterno):
    diretor ={}
    diretor['numero'] = numero
    diretor['nome']= nome
    diretor['cargo']= "diretor"
    diretor['subalterno'] = subalterno
    return diretor
def gerenteDic(numero,nome,subalterno):
    gerente ={}
    gerente['numero'] = numero
    gerente['nome']= nome
    gerente['cargo'] = "gerente"
    gerente['subalterno'] = subalterno
    return gerente

def CoordenadorDic(numero,nome,subalterno):
    coordenador ={}
    coordenador['numero'] = numero
    coordenador['nome']= nome
    coordenador['cargo'] = "coordenador"
    coordenador['subalterno'] = subalterno

    return coordenador
#listaCoodenador.append(CoordenadorDic(1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),"medico"))
def funcionarioDic(numero,nome,cargo):

    funcionario ={}
    funcionario['numero'] = numero
    funcionario['nome']= nome
    funcionario['cargo']=cargo
    
    return funcionario

c=0
print(c)
#for p in range(1,28):
    #hierarquiaHosp.append(presiDic(p,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
    #for d in range(0,2):
        #hierarquiaHosp.append(dretorDic(d,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
        #for g in range(0,2):
            #hierarquiaHosp.append(gerenteDic(g,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
            


#for f in range(1,3):
    #listafunc.append(funcionarioDic(f,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),"motorista"))
#primeira lista de funcionarios

listafunc=[]
for f in range(0,18):
        listafunc.append(funcionarioDic(f+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),"medico"))
#primeira lista coordenadores 
listaCoodenador=[]

for k in range(0,7):
    listaCoodenador.append(CoordenadorDic(k+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listafunc)) 
    listafunc=[]
    for f in range(0,18):
        listafunc.append(funcionarioDic(f+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),"medico"))
#primeira lista de gerente
listaGerente=[]
for g in range(0,5):
     listaGerente.append(gerenteDic(g+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listaCoodenador))
     listaCoodenador=[]
     for k2 in range(0,7):
        listaCoodenador.append(CoordenadorDic(k2+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listafunc))
        listafunc=[]
        for f in range(0,18):
            listafunc.append(funcionarioDic(f+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),"medico"))  
#primeira lista de diretores
listaDiretor =[]
for d in range(0,3):
    listaDiretor.append(dretorDic(d+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listaGerente))
    listaGerente=[]
    for g in range(0,5):
        listaGerente.append(gerenteDic(g+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listaCoodenador))
        listaCoodenador=[]
        for k2 in range(0,7):
            listaCoodenador.append(CoordenadorDic(k2+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listafunc))
            listafunc=[]
            for f in range(0,18):
                listafunc.append(funcionarioDic(f+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),"medico"))
#primeira lista de presidentes
listaPresidente=[]
for p in range(0,27):
    listaPresidente.append(presiDic(p+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listaDiretor))
    listaDiretor=[]
    for d in range(0,3):
        listaDiretor.append(dretorDic(d+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listaGerente))
        listaGerente=[]
        for g in range(0,5):
            listaGerente.append(gerenteDic(g+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listaCoodenador))
            listaCoodenador=[]
            for k2 in range(0,7):
                listaCoodenador.append(CoordenadorDic(k2+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),listafunc))
                listafunc=[]
                for f in range(0,18):
                    listafunc.append(funcionarioDic(f+1,aleatorioFuncionario.nomes()+ " "+ aleatorioFuncionario.sobrenomes(),"medico"))


#presidente = 27
#diretor = 27*3 = 81
#gerente = 81*5 = 405
#coordenador =  7*405 = 2835
#funcionario =  2835 * 18 = 51030 funcionarios
                 
#print("=-"*10)
#print(listafunc)
#print("=-"*10)
#print(listaCoodenador)
#print("=-"*10)
#print(listaGerente)
#print("=-"*10)
#print(listaDiretor)
#print("=-"*10)
#print(listaPresidente)
#print("-="*20, "informacao")
print(len(listaPresidente))

resultDiretor=len(listaPresidente[0]['subalterno'])
novalistaDiretor = listaPresidente[0]['subalterno']
print(resultDiretor)
resultgerente=len(novalistaDiretor[0]['subalterno'])
novalistaGerente=novalistaDiretor[0]['subalterno']
print(resultgerente)
resultCoordendor=len(novalistaGerente[0]['subalterno'])
novalistaCoordenador=novalistaGerente[0]['subalterno']
print(resultCoordendor)
resultFunc = len(novalistaCoordenador[0]['subalterno'])
novalistaFunc = novalistaCoordenador[0]['subalterno']
print(resultFunc)
#print(novalistaDiretor)
