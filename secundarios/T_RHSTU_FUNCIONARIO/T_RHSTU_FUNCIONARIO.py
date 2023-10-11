import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
ListaFuncionarios=[]


def T_RHSTU_FUNCIONARIO(id_func,id_superior,nm_func,nr_cpf,nr_rg,dt_nascimento,vl_salario,
                     st_func,dt_cadastro,nm_usuario):
    funcionario = {}
    funcionario['ID_FUNC'] = id_func #PK
    funcionario['ID_SUPERIOR'] = id_superior #FK
    funcionario['NM_FUNC'] = nm_func
    funcionario['DT_NASCIMENTO'] = dt_nascimento
    funcionario['VL_SALARIO'] = vl_salario
    funcionario['NR_RG'] = nr_rg
    funcionario['NR_CPF'] = nr_cpf
    funcionario['ST_FUNC'] = st_func
    funcionario['DT_CADASTRO'] = dt_cadastro
    funcionario['NM_USUARIO'] = nm_usuario
    return funcionario 




for i in range(2):
            idFunc = #PK
            idSuperior = #FK
            nmFunc = 
            dtNascimento = 
            vlSalario =
            nrRG =
            nrCPF =
            stFunc =
            dtCadastro =
            nmUsuario =




 

            funcionario = T_RHSTU_FUNCIONARIO(id_func=,id_superior=,nm_func=,dt_nascimento=,vl_salario=,nr_rg=,nr_cpf=,st_func=,dt_cadastro=,nm_usuario=)
            ListaFuncionarios.append(funcionario)
            print(Funcionarios)


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