import csv
import aleatorioMedicamento 
import datetime as dt
hoje = dt.date.today()
ListaMedicamentos=[]

with open('primarios\\T_RHSTU_MEDICAMENTO\\remedios.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaNomeRemedios = list(reader)


def T_RHSTU_MEDICAMENTO(id_medicamento,nm_medicamento,ds_detalhada_medicamento,nr_codigo_barras,dt_cadastro,nm_usuario):
    medicamento = {}
    medicamento['ID_MEDICAMENTO'] = id_medicamento #P
    medicamento['NM_MEDICAMENTO'] = nm_medicamento 
    medicamento['DS_DETALHADA_MEDICAMENTO'] = ds_detalhada_medicamento 
    medicamento['NR_CODIGO_BARRAS'] = nr_codigo_barras 
    medicamento['DT_CADASTRO'] = dt_cadastro
    medicamento['NM_USUARIO'] = nm_usuario
    return medicamento 

i=0
while i < len(listaNomeRemedios):
            idMedicamento = i 
            nmMedicamento = listaNomeRemedios[i][0]
            dsDetalhadaMedicamento = aleatorioMedicamento.descricao()
            nrCodigoBarras = aleatorioMedicamento.CodBarras()
            dtCadastro = hoje
            nmUsuario = "Miron"
            i+=1
            

            medicamento = T_RHSTU_MEDICAMENTO(id_medicamento=idMedicamento,nm_medicamento=nmMedicamento,ds_detalhada_medicamento=dsDetalhadaMedicamento,nr_codigo_barras=nrCodigoBarras,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaMedicamentos.append(medicamento)

            
aleatorioMedicamento.geradorDeCSV('primarios\\T_RHSTU_MEDICAMENTO\\T_RHSTU_MEDICAMENTO.csv',ListaMedicamentos)              

#try:
    #with oracledb.connect(user='rm551801',password='040591',dsn="oracle.fiap.com.br/orcl") as conexao:
        #with conexao.cursor() as cur:
             #ins = '''INSERT INTO T_RHSTU_ESTADO(ID_ESTADO,SG_ESTADO,NM_ESTADO,DT_CADASTRO,NM_USUARIO) 
             #VALUES(:ID_ESTADO,:SG_ESTADO,:NM_ESTADO,TO_DATE(:DT_CADASTRO,'YYYY-MM-DD'),:NM_USUARIO)'''        
             #for info in listaEstados:
                    #cur.execute(ins, info)
                    #conexao.commit()
                    
            
            
#except oracledb.DatabaseError as erro:
                #print("deu erro ESTADO!")
                #print(erro)