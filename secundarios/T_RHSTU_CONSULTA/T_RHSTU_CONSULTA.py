import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaConsultas=[]
repeticao = 2

def T_RHSTU_CONSULTA(id_unid_hospital,id_consulta,id_paciente,id_func,dt_hr_consulta,nr_consultorio,dt_cadastro,nm_usuario):
    consulta = {}
    consulta['ID_UNID_HOSPITAL'] = id_unid_hospital #PF
    consulta['ID_CONSULTA'] = id_consulta #P
    consulta['ID_PACIENTE'] = id_paciente #F
    consulta['ID_FUNC'] = id_func #F
    consulta['DT_HR_CONSULTA'] = dt_hr_consulta
    consulta['NR_CONSULTORIO'] = nr_consultorio
    consulta['DT_CADASTRO'] = dt_cadastro
    consulta['NM_USUARIO'] = nm_usuario
    return consulta 

for i in range(repeticao):
            idUnidHospital = #PK
            idConsulta = #P
            idPaciente = #F
            idFunc = #F
            dtHrConsulta =
            nrConsultorio =
            dtCadastro =
            nmUsuario =



            consulta = T_RHSTU_CONSULTA(id_unid_hospital=,id_consulta=,id_paciente=,id_func=,dt_hr_consulta=,nr_consultorio=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaConsultas.append(consulta)
            


try:
    with oracledb.connect(user='rm551801',password='040591',dsn="oracle.fiap.com.br/orcl") as conexao:
        with conexao.cursor() as cur:
             ins = '''INSERT INTO T_RHSTU_ESTADO(ID_ESTADO,SG_ESTADO,NM_ESTADO,DT_CADASTRO,NM_USUARIO) 
             VALUES(:ID_ESTADO,:SG_ESTADO,:NM_ESTADO,TO_DATE(:DT_CADASTRO,'YYYY-MM-DD'),:NM_USUARIO)'''        
             for info in listaEstados:
                    cur.execute(ins, info)
                    conexao.commit()
                    
            
            
except oracledb.DatabaseError as erro:
                print("deu erro ESTADO!")
                print(erro)