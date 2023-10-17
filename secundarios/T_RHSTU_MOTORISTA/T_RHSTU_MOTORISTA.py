import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
ListaMotoristas=[]


def T_RHSTU_MOTORISTA(id_func,nr_crm,nm_categoria_cnh,dt_validade_cnh,dt_cadastro,nm_usuario):
    motorista = {}
    motorista['ID_FUNC'] = id_func #PF
    motorista['NR_CRM'] = nr_crm
    motorista['NM_CATEGORIA_CNH'] = nm_categoria_cnh
    motorista['DT_VALIDADE_CNH'] = dt_validade_cnh
    motorista['DT_CADASTRO'] = dt_cadastro
    motorista['NM_USUARIO'] = nm_usuario
    return motorista 




for i in range(2):
            idFunc = #PF
            nrCRM =
            nmCategoriaCNH =
            dtValidadeCNH =
            dtCadastro =
            nmUsuario =




 

            motorista = T_RHSTU_MOTORISTA(id_func=idFunc,nr_crm=nrCRM,nm_categoria_cnh=nmCategoriaCNH,dt_validade_cnh=dtValidadeCNH,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaMotoristas.append(motorista)
            print(ListaMotoristas)


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