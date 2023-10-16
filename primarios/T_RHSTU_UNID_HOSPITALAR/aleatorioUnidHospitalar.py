from faker import Faker
import random
fake = Faker('pt_BR')
siglas = ("AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO")
pontosDeReferencia =("Palácio Rio Branco","Praia de Ponta Verde","Fortaleza de São José de Macapá","Teatro Amazonas","Pelourinho","Praia de Iracema","Palácio do Planalto","Convento da Penha","Parque Flamboyant",
                     "Centro Histórico de São Luís","Chapada dos Guimarães","Parque das Nações Indígenas","Praça da Liberdade","Mercado Ver-o-Peso","Praia de Tambaú","Jardim Botânico","Centro Histórico de Olinda",
                     "Ponte Estaiada","Maracanã","Forte dos Reis Magos","Mercado Público","Complexo da Estrada de Ferro Madeira-Mamoré","Praça das Águas","Ponte Hercílio Luz","Avenida Paulista","Orla de Atalaia","Praia da Graciosa")
cidade =("Rio Branco","Maceió","Macapá","Manaus","Salvador","Fortaleza","Brasília","Vitória","Goiânia","São Luís","Cuiabá","Campo Grande","Belo Horizonte","João Pessoa","Curitiba","Recife","Teresina","Rio de Janeiro",
         "Natal","Porto Alegre","Porto Velho","Boa Vista","Florianópolis","São Paulo","Aracaju","Palmas")





def idades():
    pos = random.randint(1, 80)
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




def generate_custom_zipcode():
    # Gera um CEP personalizado, no formato "XXXXX-XXX"
    return fake.random_int(min=10000, max=99999).__str__() + '-' + fake.random_int(min=100, max=999).__str__()

def geraNrLogradouro():
    pos = random.randint(27, 1500)    
    return pos

def generate_address_data(num_neighborhoods, addresses_per_neighborhood):
    address_data = []
    for id_bairro in range(1, num_neighborhoods + 1):
        for _ in range(addresses_per_neighborhood):
            address = {
                'nm_endereco': fake.street_address(),
                'id_bairro': id_bairro,
                'nr_cep': generate_custom_zipcode(),  # Use a função personalizada para gerar CEPs
            }
            address_data.append(address)
    return address_data

def rua():
     rua = fake.street_address()
     return rua
nome = rua()
print(nome)

