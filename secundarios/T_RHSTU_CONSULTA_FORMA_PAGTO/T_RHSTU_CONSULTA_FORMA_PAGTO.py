import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaConsultaFormasDePagamento=[]
repeticao = 2

def T_RHSTU_CONSULTA_FORMA_PAGTO(id_consulta_forma_pagto,id_unid_hospital,id_consulta,id_paciente_ps,
                                 id_forma_pagto,dt_pagto_consulta,st_pagto_consulta,dt_cadastro,nm_usuario):
    consultaFormaPagto = {}
    consultaFormaPagto['ID_CONSULTA_FORMA_PAGTO'] = id_consulta_forma_pagto #P
    consultaFormaPagto['ID_UNID_HOSPITAL'] = id_unid_hospital #F
    consultaFormaPagto['ID_CONSULTA'] = id_consulta #F
    consultaFormaPagto['ID_PACIENTE_PS'] = id_paciente_ps #F
    consultaFormaPagto['ID_FORMA_PAGTO'] = id_forma_pagto #F
    consultaFormaPagto['DT_PAGTO_CONSULTA'] = dt_pagto_consulta 
    consultaFormaPagto['ST_PAGTO_CONSULTA'] = st_pagto_consulta
    consultaFormaPagto['DT_CADASTRO'] = dt_cadastro
    consultaFormaPagto['NM_USUARIO'] = nm_usuario
    return consultaFormaPagto 

for i in range(repeticao):
            idConsultaFormaPagto= #P
            idUnidHospital= #F
            idConsulta = #F
            idPacientePs = #F
            idFormaPagto = #F
            dtPagtoConsulta =
            stPagtoConsulta =
            dtCadastro =
            nmUsuario =



            ConsultaFormaDePagamento = T_RHSTU_CONSULTA_FORMA_PAGTO(id_consulta_forma_pagto=,id_unid_hospital=,id_consulta=,id_paciente_ps=,id_forma_pagto=,dt_pagto_consulta=,st_pagto_consulta=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaConsultaFormasDePagamento.append(ConsultaFormaDePagamento)
            


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