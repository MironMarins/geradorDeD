import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
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

for i in range(repeticao):
            idFormaPagto =
            nmFormaPagto =
            dsFormaPagto =
            stFormaPagto =
            dtCadastro =
            nmUsuario =



            FormaDePagamento = T_RHSTU_FORMA_PAGAMENTO(id_forma_pagto=,nm_forma_pagto=,ds_forma_pagto=,st_forma_pagto=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaFormasDePagamento.append(FormaDePagamento)
            


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