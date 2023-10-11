import oracledb
import aleatorio
Medicos=[]


def T_RHSTU_MEDICO(id_func,nr_crm,ds_especialidade,st_func,dt_cadastro,nm_usuario):
    medico = {}
    medico['ID_FUNC'] = id_func #PF
    medico['NR_CRM'] = nr_crm
    medico['DS_ESPECIALIDAE'] = ds_especialidade
    medico['DT_CADASTRO'] = dt_cadastro
    medico['NM_USUARIO'] = nm_usuario
    return medico 




for i in range(2):
            idFunc = #PF
            nrCRM =
            dsEspecialidade =
            dtCadastro =
            nmUsuario =




 

            medico = T_RHSTU_MEDICO(id_func=,nr_crm=,ds_especialidade=,dt_cadastro=,nm_usuario=)
            Medicos.append(medico)
            print(Medicos)


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