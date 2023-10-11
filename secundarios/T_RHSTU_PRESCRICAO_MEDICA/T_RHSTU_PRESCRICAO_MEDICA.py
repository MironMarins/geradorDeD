import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaPrescricaoMedicas=[]
repeticao = 2

def T_RHSTU_PRESCRICAO_MEDICA(id_prescricao_medica,id_unid_hospital,id_consulta,id_medicamento,ds_posologia,ds_via,ds_observacao_uso,qt_medicamento,dt_cadastro,nm_usuario):
    prescricao_medica = {}
    prescricao_medica['ID_PRESCRICAO_MEDICA'] = id_prescricao_medica #P
    prescricao_medica['ID_UNID_HOSPITAL'] = id_unid_hospital #F
    prescricao_medica['ID_CONSULTA'] = id_consulta #F
    prescricao_medica['ID_MEDICAMENTO'] = id_medicamento #F
    prescricao_medica['DS_POSOLOGIA'] = ds_posologia
    prescricao_medica['DS_VIA'] = ds_via
    prescricao_medica['DS_OBSERVACAO_USO'] = ds_observacao_uso
    prescricao_medica['QT_MEDICAMENTO'] = qt_medicamento
    prescricao_medica['NM_USUARIO'] = nm_usuario
    prescricao_medica['DT_CADASTRO'] = dt_cadastro
    
    return prescricao_medica 

for i in range(repeticao):
            idPrescricaoMedica = #P
            idUnidHospital = #F
            idConsulta = #F
            idMedicamento = #F
            dsPosologia = 
            dsVia =
            dsObservacaoUso =
            qtMedicamento =
            dtCadastro =
            nmUsuario =



            prescricaoMedica = T_RHSTU_PRESCRICAO_MEDICA(id_prescricao_medica=,id_unid_hospital=,id_consulta=,id_medicamento=,ds_posologia=,ds_via=,ds_observacao_uso=,qt_medicamento=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaPrescricaoMedicas.append(prescricaoMedica)
            


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