import random

def randTelefones():
    tiposDeTalefones=("celular","empresa","firma")
    pos = random.randint(0, (len(tiposDeTalefones)-1))
    return tiposDeTalefones[pos]

planos_de_saude_reais = ['Alice','Unimed','SulAmérica','Bradesco Saúde','Amil','Hapvida','NotreDame Intermédica','Porto Seguro Saúde','SulAmérica Saúde','Cassi']


cnpjReais = ("35612503000100","02812468000106","02866602000151","92693118000160","29309127000179",
             "63554067000198","44649812000138","61198164000160","02866602000151","33719485000127")
def descricaoPS():
    descriçãoPS =("Plano de saude empresarial","Plano classico","Plano Familia","Plano Individual")
    pos = random.randint(0, (len(descriçãoPS)-1))
    return descriçãoPS[pos]
def generate_health_plan_data(num_plans):
    health_plans = []
    for _ in range(num_plans):
        health_plan = {
            'nm_plano_saude': random.choice(planos_de_saude_reais),
        }
        health_plans.append(health_plan)
    return health_plans

# Geração de associações entre pacientes e planos de saúde
def generate_patient_health_plan_data(num_patients, num_plans):
    patients_health_plans = []
    for id_paciente in range(1, num_patients + 1):
        patient_health_plan = {
            'id_paciente': id_paciente,
            'id_plano_saude': random.randint(1, num_plans),
        }
        patients_health_plans.append(patient_health_plan)
    return patients_health_plans

def idades():
    pos = random.randint(1, 15)
    return pos

def dataFundacao(idade):
        anoNascimento = 2023 - idade
        anoNascimento = str(anoNascimento)
        data = anoNascimento + "-"
        mes = random.randint(1,12)
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            mes = str(mes)
            data = data + mes + "-"
            dia = random.randint(1,31)
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            mes = str(mes)
            data = data + mes + "-"
            dia = random.randint(1,30)
        elif mes == 2:
             mes = str(mes)
             data = data + mes + "-"
             dia = random.randint(1,28)
        dia = random.randint(1,30)
        dia = str(dia)
        data = data + dia
        return data

def nomesMasculinos():
    nomesMasculinos = ("João","Pedro","Antônio","Luís","Gabriel","Rafael","Felipe","Daniel","André","Carlos","Marcos","Eduardo","Lucas","Marcelo","Rodrigo","Mateus","Alexandre","Roberto","Thiago","Gustavo","Leonardo","Bruno","João Pedro","Raul","Miguel","Fernando","Paulo","Francisco","Matheus","Vinícius","Guilherme","Diego","Rafael","Fabio","Otávio","William","Renato","Emanuel","Davi","Flávio","José","César","Márcio","Leandro","Alan","Vitor","Augusto","Juan","Ângelo","Hugo")
    pos = random.randint(0, (len(nomesMasculinos)-1))
    return nomesMasculinos[pos]

def nomesFemininos():
    nomesFemininos =("Maria","Ana","Laura","Sofia","Isabella","Helena","Valentina","Luísa","Giovanna","Alice","Clara","Camila","Beatriz","Julia","Manuela","Mariana","Gabriela","Rafaela","Carolina","Joana","Amanda","Letícia","Vitória","Emanuela","Bruna","Renata","Isadora","Lívia","Eloísa","Thais","Roberta","Júlia","Marta","Andrea","Vanessa","Bárbara","Flávia","Natália","Bianca","Fernanda","Raquel","Daniela","Patrícia","Juliana","Débora","Larissa","Verônica","Renata","Adriana","Cláudia")
    pos = random.randint(0, (len(nomesFemininos)-1))
    return nomesFemininos[pos]
def sobrenomes(): 
    sobrenomes = ("da Silva", "Oliveira", "Machado", "dos Santos", "Fraga", "Moura", "Menezes","Pereira","Oliveira","Souza","Costa","Rodrigues","Martins","Ferreira","Alves","Lima","Araújo","Barbosa","Gomes","Vieira","Barbosa","Ribeiro","Fernandes","Carvalho","Mendes","Dantas","Cardoso","Dias","Cunha","Rocha",
                  "Castro","Nunes","Moreira","Torres","Lopes","Pinto","Monteiro","Fonseca","Amaral","Xavier","Guedes","Magalhães","Andrade","Abreu","Tavares","Santos","Reis","Coelho","Guimarães","Mota","Machado","Azevedo","Correia","Teixeira","Medeiros","Mello","Nascimento","Aguiar","Sá","Freitas","Rios","Marques",
                  "Caldeira","Cardoso","Viana","Vasconcelos","Bessa","Simões","Moraes","Peixoto","Sampaio","Pinheiro","Brito","Soares","Barros","Pires","Guerra","Veloso","Azevedo","Rangel","Cordeiro","Abreu","Peçanha","Britto","Santana","Nogueira","Dantas","Galvão","Guimarães","Paiva","Lima","Siqueira","Vasconcelos","Goulart",
                  "Franco","Couto","Lobato","Duarte","Pacheco","Brites","Bastos","Pinho","Lacerda","Rios","Brandão")
    pos = random.randint(0, (len(sobrenomes)-1))
    return sobrenomes[pos]
masc = nomesMasculinos()
fem = nomesFemininos()

def nomes():
    nome1 = nomesMasculinos()
    nome2 = nomesFemininos()
    pos = random.randint(1,2)
    #print(pos)
    if pos == 2:
        nome = nome1
    elif pos == 1:
        nome = nome2
    return nome