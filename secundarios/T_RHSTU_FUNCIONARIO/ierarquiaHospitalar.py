import aleatorioFuncionario

#presidente = 27
#diretor = 27*3 = 81
#gerente = 81*5 = 405
#coordenador =  7*405 = 2835
#funcionario =  2835 * 15 = 42525 medicos
#funcionario =  8 * 27 = 216 motoristas

hierarquiaHosp = []
listaPresidente =[]
listaDiretor =[]
listaGerente=[]
listaCoodenador=[]
listafunc=[]

def presiDic(numero,nome,subalterno):
    presidente ={}
    presidente['numero'] = numero
    presidente['nome'] = nome
    presidente['cargo'] = "presidente"
    presidente['subalterno'] = subalterno
    return presidente
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

def funcionarioDic(numero,nome,subalterno):
    funcionario ={}
    funcionario['numero'] = numero
    funcionario['nome']= nome
    funcionario['cargo']="funcionario"
    funcionario['subalterno'] = subalterno
    return funcionario
c=0
print(c)
for p in range(1,28):
    hierarquiaHosp.append(presiDic(p,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
    for d in range(0,2):
        hierarquiaHosp.append(dretorDic(d,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
        for g in range(0,2):
            hierarquiaHosp.append(gerenteDic(g,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
            for c in range(0,2):
                hierarquiaHosp.append(CoordenadorDic(c,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
                for f in range(0,2):
                    hierarquiaHosp.append(funcionarioDic(f,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
                for f in range(3,5):
                    hierarquiaHosp.append(funcionarioDic(f,aleatorioFuncionario.nomes(),aleatorioFuncionario.nomes()))
                
                    

print(hierarquiaHosp)

