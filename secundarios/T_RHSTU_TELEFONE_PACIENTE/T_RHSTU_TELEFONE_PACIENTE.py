import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaTelefonesPaciente=[]
repeticao = 2

def T_RHSTU_PACIENTE_TELEFONE_PACIENTE(id_paciente,id_telefone,nr_ddi,nr_ddd,nr_telefone,tp_telepone,st_telefone,dt_cadastro,nm_usuario):
    telefonePaciente = {}
    telefonePaciente['ID_PACIENTE'] = id_paciente #PF
    telefonePaciente['ID_TELEFONE'] = id_telefone #P
    telefonePaciente['NR_DDI'] = nr_ddi 
    telefonePaciente['NR_DDD'] = nr_ddd
    telefonePaciente['NR_TELEFONE'] = nr_telefone
    telefonePaciente['TP_TELEFONE'] = tp_telepone
    telefonePaciente['ST_TELEFONE'] = st_telefone
    telefonePaciente['DT_CADASTRO'] = dt_cadastro
    telefonePaciente['NM_USUARIO'] = nm_usuario
    return telefonePaciente 

for i in range(repeticao):
            idPaciente = #PF
            idTelefone = #P
            nrDDI =
            nrDDD =
            nrTelefone =
            tpTelepone =
            stTelefone =
            dtCadastro =
            nmUsuario =
            



            TelefonePaciente = T_RHSTU_PACIENTE_TELEFONE_PACIENTE(id_paciente=,id_telefone=,nr_ddi=,nr_ddd=,nr_telefone=,tp_telepone=,st_telefone=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaTelefonesPaciente.append(TelefonePaciente)
            


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