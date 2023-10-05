import oracledb
import aleatorio
import aleatorioEstado
listaEstados=[]
repeticao = 2

def T_RHSTU_ENDERECO_UNIDHOSP(id_end_unidhosp,id_unid_hospital,id_logradouro,nr_logradouro,ds_ponto_referencia,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    endereco_unidhosp = {}
    endereco_unidhosp['ID_END_UNIDHOSP'] = id_end_unidhosp #PK
    endereco_unidhosp['ID_UNID_HOSPITAL'] = id_unid_hospital #FK T_RHSTU_UNID_HOSPITALAR
    endereco_unidhosp['ID_LOGRADOURO'] = id_logradouro #FK T_RHSTU_LOGRADOURO
    endereco_unidhosp['NR_LOGRADOURO'] = nr_logradouro
    endereco_unidhosp['DS_PONTO_REFERENCIA'] = ds_ponto_referencia
    endereco_unidhosp['DT_INICIO'] = dt_inicio
    endereco_unidhosp['DT_FIM'] = dt_fim
    endereco_unidhosp['DT_CADASTRO'] = dt_cadastro
    endereco_unidhosp['NM_USUARIO'] = nm_usuario
    return logradouro 

for i in range(repeticao):
            idEndUnidhosp = #PK
            idUnidHospital = #FK T_RHSTU_UNID_HOSPITALAR
            idLogradouro = #FK T_RHSTU_LOGRADOURO
            nrLogradouro =
            dsPontoReferencia = 
            dtInicio = 
            dtFim = 
            dataCadastro = aleatorioEstado.hoje
            usuarioNome = aleatorio.nomes()
            usuarioSobreNome = aleatorio.sobrenomes()
            usuarioNomeCompleto = usuarioNome + usuarioSobreNome


            enderecoUnidhosp = T_RHSTU_ENDERECO_UNIDHOSP(id_end_unidhosp=,id_unid_hospital=,id_logradouro=,nr_logradouro=,ds_ponto_referencia=,dt_inicio=,dt_fim=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            listaEstados.append(enderecoUnidhosp)
            


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