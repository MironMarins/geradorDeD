import oracledb
import aleatorio
import aleatorioEstado
listaEstados=[]
repeticao = 2

def T_RHSTU_ESTADO(id_estado,sg_estado,nm_estado,dt_cadastro,nm_usuario):
    paciente = {}
    paciente['ID_ESTADO'] = id_estado #PK
    paciente['SG_ESTADO'] = sg_estado
    paciente['NM_ESTADO'] = nm_estado
    paciente['DT_CADASTRO'] = dt_cadastro
    paciente['NM_USUARIO'] = nm_usuario
    return paciente 

for i in range(repeticao):
            idEstado = aleatorioEstado.idEstado() #PK
            nmEstado = aleatorioEstado.estados()
            sgEstado = aleatorioEstado.siglas(nmEstado)
            dataCadastro = aleatorioEstado.hoje
            usuarioNome = aleatorio.nomes()
            usuarioSobreNome = aleatorio.sobrenomes()
            usuarioNomeCompleto = usuarioNome + usuarioSobreNome


            estado = T_RHSTU_ESTADO(id_estado=idEstado,sg_estado=sgEstado,nm_estado=nmEstado,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            listaEstados.append(estado)
            


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