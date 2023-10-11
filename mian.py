import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import tabelas

listaPacientes=[]



conn = oracledb.connect(user='rm551801',password='040591', dsn="oracle.fiap.com.br/orcl")
print("Database version: ", conn.version)
#CRIAR CURSOR
cur = conn.cursor()
cur.execute('SELECT * FROM TB_PSH_PATAKI_PRODUTO')
#CHECAR IMFORMAÇÕES

try:
    with oracledb.connect(user='rm551801',password='040591',
                           dsn="oracle.fiap.com.br/orcl") as conexao:
       with conexao.cursor() as cur:
           ins = '''INSERT INTO T_RHSTU_PACIENTE(ID_PACIENTE,NM_PACIENTE,NR_CPF,NM_RG,DT_NASCIMENTO,FL_SEXO_BILOGICO,DS_ESCOLARIDADE,DS_ESTADO_CIVIL,NM_GRUPO_SANGUINEO,NR_ALTURA,NR_PESO,DT_CADASTRO,NM_USUARIO) 
            VALUES (SEQ_ID.NEXTVAL,:NM_PACIENTE,:NR_CPF,:NM_RG,:DT_NASCIMENTO,:FL_SEXO_BILOGICO,:DS_ESCOLARIDADE,:DS_ESTADO_CIVIL,:
            NM_GRUPO_SANGUINEO,: NR_ALTURA,:NR_PESO,:DT_CADASTRO,:NM_USUARIO)'''        

except oracledb.DatabaseError as erro:
                print("deu erro!")

print("[1] manual")
print("[2] automatico")
opcao = int(input())
if opcao == 1:
    print("escolha sua tabela")
    print("[1] paciente")
    opcao = int(input())
    if opcao == 1:
        print("escreva as informações pedidas")
        #idPaciente = aleatorio.ids()
        nome = str(input("nome: "))
        sobrenome = str(input("sobrenome: "))
        nomeInteiro = nome + sobrenome
        cpf = str(input("cpf: "))
        rg = str(input("rg: "))
        idade = int(input("idade: "))
        dataNascimento = str(input("data de nascimento(dd/mm/aaaa): "))
        sexoBiologico = str(input("sexoBiologico [M](masculino) [F](feminino) [I] (indefinido): "))
        escolaridade = str(input("escolaridade: "))
        estadoCivil = str(input("estadoCivil: "))
        grupoSanguineo = str(input("Tipo de sangue: " ))
        altura = int(input("altura (cm):"))
        peso = int(input("altura (mg): "))
        dataCadastro = str(input("dataCadastro (dd/mm/aaaa): "))
        usuarioNome = str(input("nome completo do usuario: ")) 
elif opcao == 2:
    print("escolha sua tabela")
    print("[1] paciente")
    opcao = int(input())
    if opcao == 1:
        for i in range(100):
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

            #cur.execute("INSERT INTO T_RHSTU_PACIENTE(ID_PACIENTE,NM_PACIENTE,NR_CPF,NM_RG,DT_NASCIMENTO,FL_SEXO_BILOGICO,DS_ESCOLARIDADE,DS_ESTADO_CIVIL,NM_GRUPO_SANGUINEO,NR_ALTURA,NR_PESO,DT_CADASTRO,NM_USUARIO) 
            # VALUES (:ID_PACIENTE,:NM_PACIENTE,:NR_CPF,:NM_RG,:DT_NASCIMENTO,:FL_SEXO_BILOGICO,:DS_ESCOLARIDADE,:DS_ESTADO_CIVIL,:
            # NM_GRUPO_SANGUINEO,: NR_ALTURA,:NR_PESO,:DT_CADASTRO,:NM_USUARIO)", {ID_PACIENTE,NM_PACIENTE,NR_CPF,NM_RG,DT_NASCIMENTO,FL_SEXO_BILOGICO,DS_ESCOLARIDADE,DS_ESTADO_CIVIL,NM_GRUPO_SANGUINEO,NR_ALTURA,NR_PESO,DT_CADASTRO,NM_USUARIO)
            #'FL_SEXO_BILOGICO':sexoBiologico,'DS_ESCOLARIDADE':escolaridade,'DS_ESTADO_CIVIL':estadoCivil,'NM_GRUPO_SANGUINEO':grupoSanguineo,
            #'NR_ALTURA':altura,'NR_PESO':peso,'DT_CADASTRO':dataCadastro,'NM_USUARIO':usuarioNomeCompleto})        
            
            paciente = tabelas.T_RHSTU_PACIENTE(id_paciente=idPaciente,nm_paciente=nomeInteiro,nr_cpf=cpf,nm_rg=rg,dt_nascimento=dataNascimento,
                                                fl_sexo_biologico=sexoBiologico,ds_escolaridade=escolaridade,ds_estado_civil=estadoCivil,
                                                nm_grupo_sanguineo=grupoSanguineo,nr_altura=altura,nr_peso=peso,dt_cadastro=dataCadastro,
                                                nm_usuario=usuarioNomeCompleto)
            listaPacientes.append(paciente)
            print(listaPacientes)
            




            print("-=" * 20)

        
        
        
        for k, v in paciente.items():
            print(f'{k}={v}' )

        
        try:
                with oracledb.connect(user='rm551801',password='040591',
                           dsn="oracle.fiap.com.br/orcl") as conexao:
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
