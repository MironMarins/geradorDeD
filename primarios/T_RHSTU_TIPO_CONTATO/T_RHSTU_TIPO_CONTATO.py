import datetime as dt
import csv
import aleatorioTipoContato
hoje = dt.date.today()
ListatiposContatos=[]
repeticao = 2

def T_RHSTU_TIPO_CONTATO(id_tipo_contato,nm_tipo_contato,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    tipo_contato = {}
    tipo_contato['ID_UNID_TIPO_CONTATO'] = id_tipo_contato #P
    tipo_contato['NM_UNID_TIPO_CONTATO'] = nm_tipo_contato
    tipo_contato['DT_INICIO'] = dt_inicio
    tipo_contato['DT_FIM'] = dt_fim
    tipo_contato['DT_CADASTRO'] = dt_cadastro
    tipo_contato['NM_USUARIO'] = nm_usuario
    return tipo_contato 
i=0
while i < len(aleatorioTipoContato.tiposDeContatos):
            
            nmTipoContato = aleatorioTipoContato.tiposDeContatos[i]
            dtInicio = aleatorioTipoContato.dataFundacao(aleatorioTipoContato.idades())
            dtFim = "None"
            dataCadastro = hoje
            usuarioNome = "Miron"
            i=i+1
            idTipoContato = i #P

            tipoContato = T_RHSTU_TIPO_CONTATO(id_tipo_contato=idTipoContato,nm_tipo_contato=nmTipoContato,dt_inicio=dtInicio,dt_fim=dtFim,dt_cadastro=dataCadastro,nm_usuario=usuarioNome)
            ListatiposContatos.append(tipoContato)
            
with open('primarios\\T_RHSTU_TIPO_CONTATO\\T_RHSTU_TIPO_CONTATO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListatiposContatos[0].keys())
        csv_writer.writeheader()
        for line in ListatiposContatos:
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