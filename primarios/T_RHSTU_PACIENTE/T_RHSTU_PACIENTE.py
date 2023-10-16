#import oracledb
import aleatorioPaciente as aleatorio
import csv
import datetime as dt
hoje = dt.date.today()



listaPacientes=[]
with open('primarios\\T_RHSTU_PACIENTE\\cpf.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaCpf = list(reader)

with open('primarios\\T_RHSTU_PACIENTE\\rg.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaRg = list(reader)

def T_RHSTU_PACIENTE(id_paciente,nm_paciente,nr_cpf,nm_rg,dt_nascimento,fl_sexo_biologico,
                     ds_escolaridade,ds_estado_civil,nm_grupo_sanguineo,nr_altura,nr_peso,
                     dt_cadastro,nm_usuario):
    paciente = {}
    paciente['ID_PACIENTE'] = id_paciente 
    paciente['NM_PACIENTE'] = nm_paciente
    paciente['NR_CPF'] = nr_cpf
    paciente['NM_RG'] = nm_rg
    paciente['DT_NASCIMENTO'] = dt_nascimento
    paciente['FL_SEXO_BIOLOGICO'] = fl_sexo_biologico
    paciente['DS_ESCOLARIDADE'] = ds_escolaridade
    paciente['DS_ESTADO_CIVIL'] = ds_estado_civil
    paciente['NM_GRUPO_SANGUINEO'] = nm_grupo_sanguineo
    paciente['NR_ALTURA'] = nr_altura
    paciente['NR_PESO'] = nr_peso
    paciente['DT_CADASTRO'] = dt_cadastro
    paciente['NM_USUARIO'] = nm_usuario
    return paciente 




for i in range(9000001):
            idPaciente = i
            nome = aleatorio.nomes()

            sobrenome = aleatorio.sobrenomes()
            nomeInteiro = nome +" "+sobrenome
            cpf = listaCpf[i]
            rg = listaRg[i]
            idade = aleatorio.idades()
            dataNascimento = aleatorio.dataNascimento(idade=idade)
            sexoBiologico =  aleatorio.sexoBiologico()
            escolaridade = aleatorio.escolaridadePaciente()
            estadoCivil = aleatorio.estadoCivil(idade=idade)
            grupoSanguineo = aleatorio.tipoSanguineo()
            altura = aleatorio.Altura(novaidade=idade)
            peso = aleatorio.Peso()
            dataCadastro = hoje
            usuarioNomeCompleto = "Miron"
            if i == 1:
                    print("1")
            elif i == 100: 
                    print("100")
            elif i == 1000: 
                    print("1000")
            elif i == 10000: 
                    print("10000")
            elif i == 100000: 
                    print("100000")
            elif i == 1000000: 
                    print("1000000")
            elif i == 2500000: 
                    print("2500000")
            
            paciente = T_RHSTU_PACIENTE(id_paciente=idPaciente,nm_paciente=nomeInteiro,nr_cpf=cpf,nm_rg=rg,dt_nascimento=dataNascimento,
                                    fl_sexo_biologico=sexoBiologico,ds_escolaridade=escolaridade,ds_estado_civil=estadoCivil,
                                    nm_grupo_sanguineo=grupoSanguineo,nr_altura=altura,nr_peso=peso,dt_cadastro=dataCadastro,
                                                            nm_usuario=usuarioNomeCompleto)
            listaPacientes.append(paciente)
            
with open('primarios\\T_RHSTU_PACIENTE\\T_RHSTU_PACIENTE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        # Criando objeto de Escrita do CSV
        csv_writer = csv.DictWriter(file_csv, fieldnames=listaPacientes[0].keys())

        # Escrevendo headers (Nome das colunas do CSV)
        csv_writer.writeheader()

        # Percorrendo o dicionario de dados
        for line in listaPacientes:
            # Escrevendo linha por linha
            csv_writer.writerow(line)            
            
            #print(listaPacientes)


#try:
    #with oracledb.connect(user='rm551801',password='040591',dsn="oracle.fiap.com.br/orcl") as conexao:
        #with conexao.cursor() as cur:
             #ins = '''INSERT INTO T_RHSTU_PACIENTE(ID_PACIENTE,NM_PACIENTE,NR_CPF,NM_RG,DT_NASCIMENTO,FL_SEXO_BIOLOGICO,DS_ESCOLARIDADE,DS_ESTADO_CIVIL,NM_GRUPO_SANGUINEO,NR_ALTURA,NR_PESO,DT_CADASTRO,NM_USUARIO) 
             #VALUES(:ID_PACIENTE,:NM_PACIENTE,:NR_CPF,:NM_RG,TO_DATE(:DT_NASCIMENTO, 'YYYY-MM-DD'),:FL_SEXO_BIOLOGICO,:DS_ESCOLARIDADE,:DS_ESTADO_CIVIL,
             #:NM_GRUPO_SANGUINEO,:NR_ALTURA,:NR_PESO,TO_DATE(:DT_CADASTRO,'YYYY-MM-DD'),:NM_USUARIO)'''        
             #for info in listaPacientes:
                    #cur.execute(ins, info)
                    #conexao.commit()
                    
            
            
#except oracledb.DatabaseError as erro:
                #print("deu erro!")
                #print(erro)