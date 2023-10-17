import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaEmailsPaciente=[]
repeticao = 2

def T_RHSTU_PACIENTE_EMAIL_PACIENTE(id_paciente,id_email,ds_email,tp_email,st_email,dt_cadastro,nm_usuario):
    emailPaciente = {}
    emailPaciente['ID_PACIENTE'] = id_paciente #F
    emailPaciente['ID_TELEFONE'] = id_email #P
    emailPaciente['DS_EMAIL'] = ds_email
    emailPaciente['TP_EMAIL'] = tp_email
    emailPaciente['ST_EMAIL'] = st_email
    emailPaciente['DT_CADASTRO'] = dt_cadastro
    emailPaciente['NM_USUARIO'] = nm_usuario
    return emailPaciente 

for i in range(repeticao):
            idPaciente = #F
            idEmail = #P
            dsEmail =
            tpEmail =
            stEmail =
            dtCadastro = 
            nmUsuario =
            



            EmailPaciente = T_RHSTU_PACIENTE_EMAIL_PACIENTE(id_paciente=idPaciente,id_email=idEmail,ds_email=dsEmail,tp_email=tpEmail,st_email=stEmail,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaEmailsPaciente.append(EmailPaciente)
            


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