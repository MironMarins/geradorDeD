import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
listaPacientes=[]


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




for i in range(2):
            idPaciente = aleatorio.ids()
            nome = aleatorio.nomes()
            sobrenome = aleatorio.sobrenomes()
            nomeInteiro = nome + sobrenome
            cpf = aleatorio.Cpf()
            rg = aleatorio.Rg()
            idade = aleatorio.idades()
            dataNascimento = aleatorio.dataNascimento(idade=idade)
            sexoBiologico =  aleatorio.sexoBiologico()
            escolaridade = aleatorio.escolaridadePaciente(idade=idade)
            estadoCivil = aleatorio.estadoCivil(idade=idade)
            grupoSanguineo = aleatorio.tipoSanguineo()
            altura = aleatorio.Altura(novaidade=idade)
            peso = aleatorio.Peso(novaidade=idade)
            dataCadastro = aleatorio.dataInscricao(idade=idade)
            usuarioNome = aleatorio.nomes()
            usuarioSobreNome = aleatorio.sobrenomes()
            usuarioNomeCompleto = usuarioNome + usuarioSobreNome




 

            paciente = T_RHSTU_PACIENTE(id_paciente=idPaciente,nm_paciente=nomeInteiro,nr_cpf=cpf,nm_rg=rg,dt_nascimento=dataNascimento,
                                    fl_sexo_biologico=sexoBiologico,ds_escolaridade=escolaridade,ds_estado_civil=estadoCivil,
                                    nm_grupo_sanguineo=grupoSanguineo,nr_altura=altura,nr_peso=peso,dt_cadastro=dataCadastro,
                                                            nm_usuario=usuarioNomeCompleto)
            listaPacientes.append(paciente)
            print(listaPacientes)


try:
    with oracledb.connect(user='rm551801',password='040591',dsn="oracle.fiap.com.br/orcl") as conexao:
        with conexao.cursor() as cur:
             ins = '''INSERT INTO T_RHSTU_PACIENTE(ID_PACIENTE,NM_PACIENTE,NR_CPF,NM_RG,DT_NASCIMENTO,FL_SEXO_BIOLOGICO,DS_ESCOLARIDADE,DS_ESTADO_CIVIL,NM_GRUPO_SANGUINEO,NR_ALTURA,NR_PESO,DT_CADASTRO,NM_USUARIO) 
             VALUES(:ID_PACIENTE,:NM_PACIENTE,:NR_CPF,:NM_RG,TO_DATE(:DT_NASCIMENTO, 'YYYY-MM-DD'),:FL_SEXO_BIOLOGICO,:DS_ESCOLARIDADE,:DS_ESTADO_CIVIL,
             :NM_GRUPO_SANGUINEO,:NR_ALTURA,:NR_PESO,TO_DATE(:DT_CADASTRO,'YYYY-MM-DD'),:NM_USUARIO)'''        
             for info in listaPacientes:
                    cur.execute(ins, info)
                    conexao.commit()
                    
            
            
except oracledb.DatabaseError as erro:
                print("deu erro!")
                print(erro)