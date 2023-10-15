import csv
import aleatorioFormaPagamento
import datetime as dt
hoje = dt.date.today()
ListaFormasDePagamento=[]
repeticao = 2

def T_RHSTU_FORMA_PAGAMENTO(id_forma_pagto,nm_forma_pagto,ds_forma_pagto,st_forma_pagto,dt_cadastro,nm_usuario):
    formaPagamento = {}
    formaPagamento['ID_FORMA_PAGTO'] = id_forma_pagto #P
    formaPagamento['NM_FORMA_PAGTO'] = nm_forma_pagto 
    formaPagamento['DS_FORMA_PAGTO'] = ds_forma_pagto
    formaPagamento['ST_FORMA_PAGTO'] = st_forma_pagto
    formaPagamento['DT_CADASTRO'] = dt_cadastro
    formaPagamento['NM_USUARIO'] = nm_usuario
    return formaPagamento 
i=0
while i < len(aleatorioFormaPagamento.formaDePagamento):
            
            nmFormaPagto = aleatorioFormaPagamento.formaDePagamento[i]
            dsFormaPagto = aleatorioFormaPagamento.descricao[i]
            stFormaPagto = "A" #tivo #ou "I"nativo 
            dtCadastro = hoje
            nmUsuario = "Miron"
            i=i+1
            idFormaPagto = i


            FormaDePagamento = T_RHSTU_FORMA_PAGAMENTO(id_forma_pagto=idFormaPagto,nm_forma_pagto=nmFormaPagto,ds_forma_pagto=dsFormaPagto,st_forma_pagto=stFormaPagto,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaFormasDePagamento.append(FormaDePagamento)
            
with open('primarios\\T_RHSTU_FORMA_PAGAMENTO\\T_RHSTU_FORMA_PAGAMENTO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        # Criando objeto de Escrita do CSV
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaFormasDePagamento[0].keys())

        # Escrevendo headers (Nome das colunas do CSV)
        csv_writer.writeheader()

        # Percorrendo o dicionario de dados
        for line in ListaFormasDePagamento:
            # Escrevendo linha por linha
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