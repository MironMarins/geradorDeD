import aleatorioFuncionario

#presidente = 27
#diretor = 27*3 = 81
#gerente = 81*5 = 405
#coordenador =  7*405 = 2835
#funcionario =  2835 * 15 = 42525 medicos
#funcionario =  8 * 27 = 216 motoristas

hierarquiaHosp = [
]

def presiDic(numero,nome):
    presidente ={}
    presidente['numero'] = numero
    presidente['nome'] = nome
    return presidente
def dretorDic(numero,nome):
    diretor ={}
    diretor['numero'] = numero
    diretor['nome']= nome
    return diretor
def gerenteDic(numero,nome):
    gerente ={}
    gerente['numero'] = numero
    gerente['nome']= nome
    return gerente

def CoordenadorDic(numero,nome):
    coordenador ={}
    coordenador['numero'] = numero
    coordenador['nome']= nome
    return coordenador

