import oracledb
import aleatorio
import aleatorioEstado
tiposContatos=[]
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

for i in range(repeticao):
            idTipoContato = #P
            nmTipoContato =
            dtInicio = 
            dtFim = 
            dataCadastro = aleatorioEstado.hoje
            usuarioNome = aleatorio.nomes()
            usuarioSobreNome = aleatorio.sobrenomes()
            usuarioNomeCompleto = usuarioNome + usuarioSobreNome


            tipoContato = T_RHSTU_TIPO_CONTATO(id_tipo_contato=,nm_tipo_contato=,dt_inicio=,dt_fim=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            tiposContatos.append(tipoContato)
            


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