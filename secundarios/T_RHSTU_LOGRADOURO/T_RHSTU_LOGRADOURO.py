import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaLogradouros=[]
repeticao = 2

def T_RHSTU_LOGRADOURO(id_logradouro,id_bairro,nm_logradouro,nr_cep,dt_cadastro,nm_usuario):
    logradouro = {}
    logradouro['ID_LOGRADOURO'] = id_logradouro #PK
    logradouro['ID_BAIRRO'] = id_bairro #FK T_RHSTU_BAIRRO
    logradouro['NM_LOGRADOURO'] = nm_logradouro
    logradouro['NR_CEP'] = nr_cep
    logradouro['DT_CADASTRO'] = dt_cadastro
    logradouro['NM_USUARIO'] = nm_usuario
    return logradouro 

for i in range(repeticao):
            idLogradouro = #PK
            idBairro =  #FK T_RHSTU_BAIRRO
            nmLogradouro = 
            nrCEP = 
            dataCadastro = aleatorioEstado.hoje
            usuarioNome = aleatorio.nomes()
            usuarioSobreNome = aleatorio.sobrenomes()
            usuarioNomeCompleto = usuarioNome + usuarioSobreNome


            logradouro = T_RHSTU_LOGRADOURO(id_logradouro=idEstado,id_bairro=,nm_logradouro=,nr_cep=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaLogradouros.append(logradouro)
            


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