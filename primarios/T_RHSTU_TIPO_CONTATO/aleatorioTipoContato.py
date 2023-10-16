from faker import Faker
import random
fake = Faker('pt_BR')

tiposDeContatos = ['Pai', 'Mãe', 'Esposa', 'Primo', 'Prima', 'Outros contatos']

telefone = fake.phone_number()
   
def idades():
    pos = random.randint(0, 10)
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