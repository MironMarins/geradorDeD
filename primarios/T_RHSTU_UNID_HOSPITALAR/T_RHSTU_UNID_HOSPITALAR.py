import datetime as dt
import csv
import aleatorioUnidHospitalar
hoje = dt.date.today()
listaEstados=[]
listaUnidadesHospitalares=[]

def T_RHSTU_UNID_HOSPITALAR(id_unid_hospital,nm_unid_hospitalar,nm_razao_social_unid_hosp,dt_fundacao,nr_logradouro,ds_complemento_numero,ds_ponto_referencia,dt_inicio,dt_termino,dt_cadastro,nm_usuario):
    unid_hospitalar = {}
    unid_hospitalar['ID_UNID_HOSPITAL'] = id_unid_hospital #PK
    unid_hospitalar['NM_UNID_HOSPITAR'] = nm_unid_hospitalar 
    unid_hospitalar['NM_RAZAO_SOCIAL_UNID_HOSP'] = nm_razao_social_unid_hosp
    unid_hospitalar['DT_FUNDACAO'] = dt_fundacao
    unid_hospitalar['NR_LOGRADOURO'] = nr_logradouro
    unid_hospitalar['DS_COMPLEMENTO_NUMERO'] = ds_complemento_numero
    unid_hospitalar['DS_PONTO_REFERENCIA'] = ds_ponto_referencia
    unid_hospitalar['DT_INICIO'] = dt_inicio
    unid_hospitalar['DT_TERMINO'] = dt_termino
    unid_hospitalar['DT_CADASTRO'] = dt_cadastro
    unid_hospitalar['NM_USUARIO'] = nm_usuario
    return unid_hospitalar 
i=0
while i< len(aleatorioUnidHospitalar.siglas):
            nmUnidHospital = "Hospital Somos Todos Um" + "(" + aleatorioUnidHospitalar.siglas[i] + ")"
            nmRazaoSocialUnidHosp = "Somos Todos Um S.A."
            dtFundacao = aleatorioUnidHospitalar.dataFundacao(aleatorioUnidHospitalar.idades())
            nrLogradouro = aleatorioUnidHospitalar.geraNrLogradouro()
            dsComplementoNumero = "None"
            dsPontoReferencia = "proximo ao " + aleatorioUnidHospitalar.pontosDeReferencia[i]
            dtInicio = str((int(dtFundacao[:4])+1)) + dtFundacao[4:]
            dtTermino = "None"
            dataCadastro = hoje
            usuarioNomeCompleto = "Miron"
            i+=1
            idUnidHospital = i


            unidHospitalar = T_RHSTU_UNID_HOSPITALAR(id_unid_hospital=idUnidHospital,nm_unid_hospitalar=nmUnidHospital,nm_razao_social_unid_hosp=nmRazaoSocialUnidHosp,dt_fundacao=dtFundacao,nr_logradouro=nrLogradouro,ds_complemento_numero=dsComplementoNumero,ds_ponto_referencia=dsPontoReferencia,dt_inicio=dtInicio,dt_termino=dtTermino,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            listaUnidadesHospitalares.append(unidHospitalar)
            
with open('primarios\\T_RHSTU_UNID_HOSPITALAR\\T_RHSTU_UNID_HOSPITALAR.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=listaUnidadesHospitalares[0].keys())
        csv_writer.writeheader()
        for line in listaUnidadesHospitalares:
            csv_writer.writerow(line)





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