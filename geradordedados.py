import random
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd


# Inicializa o Faker
fake = Faker('pt_BR')

# Função para gerar datas de nascimento realistas
def generate_birth_date():
    end_date = datetime(2005, 12, 31)
    start_date = datetime(1950, 1, 1)
    random_date = fake.date_of_birth(minimum_age=18, maximum_age=70)
    return random_date

# Função para gerar CPF válidos (necessário instalar a biblioteca "validate-docbr")
from validate_docbr import CPF
def generate_cpf():
    cpf = CPF()
    return cpf.generate()

# Geração de dados para pacientes
def generate_patient_data(num_patients):
    patients = []
    for _ in range(num_patients):
        patient = {
            'nm_paciente': fake.name(),
            'dt_nascimento': generate_birth_date(),
            'nr_cpf': generate_cpf(),
            'id_cidade': random.randint(1, 280)
        }
        patients.append(patient)
    return patients

# Geração de dados para contatos
def generate_contact_data(num_contacts):
    contact_types = ['Pai', 'Mãe', 'Esposa', 'Primo', 'Prima', 'Outros contatos']
    contacts = []
    for _ in range(num_contacts):
        contact = {
            'id_tipo_contato': random.randint(1, 6),
            'ds_contato': fake.phone_number(),
        }
        contacts.append(contact)
    return contacts

# Lista de hospitais fictícios
hospitais_ficticios = [
    {
        'nm_unid_hospitalar': 'Hospital Central',
        'nm_razao_social_unid_hosp': 'Hospital Central Ltda.',
        'id_logradouro': 1
    },
    {
        'nm_unid_hospitalar': 'Hospital da Cidade',
        'nm_razao_social_unid_hosp': 'Hospital da Cidade S.A.',
        'id_logradouro': 2
    },
    {
        'nm_unid_hospitalar': 'Hospital São Lucas',
        'nm_razao_social_unid_hosp': 'Hospital São Lucas Eireli',
        'id_logradouro': 3
    },
    {
        'nm_unid_hospitalar': 'Hospital Santa Clara',
        'nm_razao_social_unid_hosp': 'Hospital Santa Clara Ltda.',
        'id_logradouro': 4
    },
    {
        'nm_unid_hospitalar': 'Hospital Nossa Senhora',
        'nm_razao_social_unid_hosp': 'Hospital Nossa Senhora S.A.',
        'id_logradouro': 5
    },
    {
        'nm_unid_hospitalar': 'Hospital Santo Antônio',
        'nm_razao_social_unid_hosp': 'Hospital Santo Antônio Eireli',
        'id_logradouro': 6
    },
    {
        'nm_unid_hospitalar': 'Hospital Santa Rita',
        'nm_razao_social_unid_hosp': 'Hospital Santa Rita Ltda.',
        'id_logradouro': 7
    },
    {
        'nm_unid_hospitalar': 'Hospital São José',
        'nm_razao_social_unid_hosp': 'Hospital São José S.A.',
        'id_logradouro': 8
    },
    {
        'nm_unid_hospitalar': 'Hospital São Francisco',
        'nm_razao_social_unid_hosp': 'Hospital São Francisco Eireli',
        'id_logradouro': 9
    },
    {
        'nm_unid_hospitalar': 'Hospital Santo Agostinho',
        'nm_razao_social_unid_hosp': 'Hospital Santo Agostinho Ltda.',
        'id_logradouro': 10
    },
    {
        'nm_unid_hospitalar': 'Hospital Santa Maria',
        'nm_razao_social_unid_hosp': 'Hospital Santa Maria S.A.',
        'id_logradouro': 11
    },
    {
        'nm_unid_hospitalar': 'Hospital Nossa Senhora de Fátima',
        'nm_razao_social_unid_hosp': 'Hospital Nossa Senhora de Fátima Eireli',
        'id_logradouro': 12
    },
    {
        'nm_unid_hospitalar': 'Hospital São Pedro',
        'nm_razao_social_unid_hosp': 'Hospital São Pedro Ltda.',
        'id_logradouro': 13
    },
    {
        'nm_unid_hospitalar': 'Hospital Santa Isabel',
        'nm_razao_social_unid_hosp': 'Hospital Santa Isabel S.A.',
        'id_logradouro': 14
    },
    {
        'nm_unid_hospitalar': 'Hospital São João',
        'nm_razao_social_unid_hosp': 'Hospital São João Eireli',
        'id_logradouro': 15
    },
    {
        'nm_unid_hospitalar': 'Hospital Santo André',
        'nm_razao_social_unid_hosp': 'Hospital Santo André Ltda.',
        'id_logradouro': 16
    },
    {
        'nm_unid_hospitalar': 'Hospital Santa Cruz',
        'nm_razao_social_unid_hosp': 'Hospital Santa Cruz S.A.',
        'id_logradouro': 17
    },
    {
        'nm_unid_hospitalar': 'Hospital São Luiz',
        'nm_razao_social_unid_hosp': 'Hospital São Luiz Eireli',
        'id_logradouro': 18
    },
    {
        'nm_unid_hospitalar': 'Hospital Santo Expedito',
        'nm_razao_social_unid_hosp': 'Hospital Santo Expedito Ltda.',
        'id_logradouro': 19
    },
    {
        'nm_unid_hospitalar': 'Hospital São Vicente',
        'nm_razao_social_unid_hosp': 'Hospital São Vicente S.A.',
        'id_logradouro': 20
    },
]

# Geração de dados para unidades hospitalares
def generate_hospital_data(num_hospitals):
    hospitals = []
    for i in range(num_hospitals):
        hospital = random.choice(hospitais_ficticios)
        hospital_data = {
            'nm_unid_hospitalar': hospital['nm_unid_hospitalar'],
            'nm_razao_social_unid_hosp': hospital['nm_razao_social_unid_hosp'],
            'id_logradouro': hospital['id_logradouro']
        }
        hospitals.append(hospital_data)
    return hospitals

# Geração de dados para funcionários
def generate_employee_data(num_employees):
    employees = []
    for _ in range(num_employees):
        employee = {
            'nm_funcionario': fake.name(),
            'id_superior': None if random.random() < 0.9 else random.randint(1, 5000)
        }
        employees.append(employee)
    return employees

# Dicionário de descrições e medicamentos correspondentes
descricao_medicamento = {
    'Para alívio de dor de cabeça': 'Paracetamol',
    'Para redução de febre': 'Ibuprofeno',
    'Antibiótico para infecções respiratórias': 'Amoxicilina',
    'Analgésico para dores musculares': 'Diclofenaco',
    'Anti-inflamatório para articulações': 'Ibuprofeno',
    'Para alergias sazonais': 'Cetirizina',
    'Anticoagulante para problemas cardíacos': 'Varfarina',
    'Suplemento vitamínico': 'Vitamina C',
    'Para tratamento de hipertensão': 'Losartana',
    'Antidepressivo': 'Fluoxetina',
}

# Geração de dados para medicamentos
def generate_medication_data(num_medications):
    medications = []
    for i in range(num_medications):
        # Selecionar aleatoriamente uma descrição fictícia
        descricao = random.choice(list(descricao_medicamento.keys()))
        # Obter o medicamento real correspondente
        medicamento_real = descricao_medicamento[descricao]
        medication = {
            'nm_medicamento': medicamento_real,
            'ds_medicamento': descricao,
        }
        medications.append(medication)
    return medications

# Função para gerar CEP personalizado
def generate_custom_zipcode():
    # Gera um CEP personalizado, no formato "XXXXX-XXX"
    return fake.random_int(min=10000, max=99999).__str__() + '-' + fake.random_int(min=100, max=999).__str__()

# Geração de dados para endereços
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

# Geração de dados para consultas
def generate_consultation_data(num_consultations, num_patients, num_employees, num_hospitals):
    consultations = []
    for id_consulta in range(1, num_consultations + 1):
        consultation = {
            'id_paciente': random.randint(1, num_patients),
            'id_func': random.randint(1, num_employees),
            'id_unid_hospital': random.randint(1, num_hospitals),
            'dt_consulta': fake.date_time_between(start_date='-1y', end_date='+1y'),
        }
        consultations.append(consultation)
    return consultations

# Geração de dados para telefones
def generate_phone_data(num_phones):
    phones = []
    for _ in range(num_phones):
        phone = {
            'nr_telefone': fake.phone_number(),
        }
        phones.append(phone)
    return phones

# Geração de dados para e-mails
def generate_email_data(num_emails):
    emails = []
    for _ in range(num_emails):
        email = {
            'ds_email': fake.email(),
        }
        emails.append(email)
    return emails

# Geração de dados para planos de saúde
# Lista de nomes de planos de saúde reais
planos_de_saude_reais = [
    'Unimed',
    'SulAmérica',
    'Bradesco Saúde',
    'Amil',
    'Hapvida',
    'Golden Cross',
    'NotreDame Intermédica',
    'Porto Seguro Saúde',
    'SulAmérica Saúde',
    'Cassi'
]

# Geração de dados para planos de saúde
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

# Geração de dados para formas de pagamento
def generate_payment_data():
    payment_methods = ['Gratuito', 'Plano de saúde', 'Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix']
    payment_data = []
    for id_forma_pagto, nm_forma_pagto in enumerate(payment_methods):
        payment = {
            'id_forma_pagto': id_forma_pagto + 1,
            'nm_forma_pagto': nm_forma_pagto,
        }
        payment_data.append(payment)
    return payment_data

# Geração de dados para Estados Brasileiros
def generate_state_data():
    state_data = [
        {"id_estado": 1, "sg_estado": "AC", "nm_estado": "Acre"},
        {"id_estado": 2, "sg_estado": "AL", "nm_estado": "Alagoas"},
        {"id_estado": 3, "sg_estado": "AP", "nm_estado": "Amapá"},
        {"id_estado": 4, "sg_estado": "AM", "nm_estado": "Amazonas"},
        {"id_estado": 5, "sg_estado": "BA", "nm_estado": "Bahia"},
        {"id_estado": 6, "sg_estado": "CE", "nm_estado": "Ceará"},
        {"id_estado": 7, "sg_estado": "DF", "nm_estado": "Distrito Federal"},
        {"id_estado": 8, "sg_estado": "ES", "nm_estado": "Espírito Santo"},
        {"id_estado": 9, "sg_estado": "GO", "nm_estado": "Goiás"},
        {"id_estado": 10, "sg_estado": "MA", "nm_estado": "Maranhão"},
        {"id_estado": 11, "sg_estado": "MT", "nm_estado": "Mato Grosso"},
        {"id_estado": 12, "sg_estado": "MS", "nm_estado": "Mato Grosso do Sul"},
        {"id_estado": 13, "sg_estado": "MG", "nm_estado": "Minas Gerais"},
        {"id_estado": 14, "sg_estado": "PA", "nm_estado": "Pará"},
        {"id_estado": 15, "sg_estado": "PB", "nm_estado": "Paraíba"},
        {"id_estado": 16, "sg_estado": "PR", "nm_estado": "Paraná"},
        {"id_estado": 17, "sg_estado": "PE", "nm_estado": "Pernambuco"},
        {"id_estado": 18, "sg_estado": "PI", "nm_estado": "Piauí"},
        {"id_estado": 19, "sg_estado": "RJ", "nm_estado": "Rio de Janeiro"},
        {"id_estado": 20, "sg_estado": "RN", "nm_estado": "Rio Grande do Norte"},
        {"id_estado": 21, "sg_estado": "RS", "nm_estado": "Rio Grande do Sul"},
        {"id_estado": 22, "sg_estado": "RO", "nm_estado": "Rondônia"},
        {"id_estado": 23, "sg_estado": "RR", "nm_estado": "Roraima"},
        {"id_estado": 24, "sg_estado": "SC", "nm_estado": "Santa Catarina"},
        {"id_estado": 25, "sg_estado": "SP", "nm_estado": "São Paulo"},
        {"id_estado": 26, "sg_estado": "SE", "nm_estado": "Sergipe"},
        {"id_estado": 27, "sg_estado": "TO", "nm_estado": "Tocantins"},
    ]

    return state_data


# Geração de dados para Cidades
def generate_city_data(num_states, cities_per_state):
    city_data = []
    for id_estado in range(1, num_states + 1):
        for _ in range(cities_per_state):
            city = {
                'nm_cidade': fake.city(),
                'id_estado': id_estado,
            }
            city_data.append(city)
    return city_data

# Geração de dados para Bairros
def generate_neighborhood_data(num_cities, neighborhoods_per_city):
    neighborhood_data = []
    for id_cidade in range(1, num_cities + 1):
        for _ in range(neighborhoods_per_city):
            neighborhood = {
                'nm_bairro': fake.street_name(),
                'id_cidade': id_cidade,
            }
            neighborhood_data.append(neighborhood)
    return neighborhood_data

# Quantidade de dados a serem gerados
num_patients = 100000
num_contacts = num_patients
num_hospitals = 28
num_employees = 50000
num_medications = 100000
num_consultations = num_patients
num_phones = num_patients
num_emails = num_patients
num_plans = 10

# Gere os dados
patients = generate_patient_data(num_patients)
contacts = generate_contact_data(num_contacts)
hospitals = generate_hospital_data(num_hospitals)
employees = generate_employee_data(num_employees)
medications = generate_medication_data(num_medications)
consultations = generate_consultation_data(num_consultations, num_patients, num_employees, num_hospitals)
phones = generate_phone_data(num_phones)
emails = generate_email_data(num_emails)
health_plans = generate_health_plan_data(num_plans)
patients_health_plans = generate_patient_health_plan_data(num_patients, num_plans)
payment_data = generate_payment_data()
state_data = generate_state_data()
city_data = generate_city_data(27, 10)
neighborhood_data = generate_neighborhood_data(270, 2)
address_data = generate_address_data(540, 2)

# Escreva os dados em arquivos CSV
def write_csv(filename, data):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, sep=';')

write_csv('estados.csv', state_data)
write_csv('cidades.csv', city_data)
write_csv('bairros.csv', neighborhood_data)
write_csv('enderecos.csv', address_data)
write_csv('pacientes.csv', patients)
write_csv('tipos_contato.csv', contacts)
write_csv('unidades_hospitalares.csv', hospitals)
write_csv('funcionarios.csv', employees)
write_csv('medicamentos.csv', medications)
write_csv('consultas.csv', consultations)
write_csv('telefones.csv', phones)
write_csv('emails.csv', emails)
write_csv('planos_saude.csv', health_plans)
write_csv('pacientes_planos.csv', patients_health_plans)
write_csv('formas_pagamento.csv', payment_data)
