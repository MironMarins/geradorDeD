import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
listaBairros=[]
repeticao = 2

def T_RHSTU_BAIRRO(id_bairro,id_cidade,nm_bairro,nm_zona_bairro,dt_cadastro,nm_usuario):
    bairro = {}
    bairro['ID_BAIRRO'] = id_bairro #PK
    bairro['ID_CIDADE'] = id_cidade #FK T_RHSTU_CIDADE
    bairro['NM_BAIRRO'] = nm_bairro
    bairro['NM_ZONA_BAIRRO'] = nm_zona_bairro
    bairro['DT_CADASTRO'] = dt_cadastro
    bairro['NM_USUARIO'] = nm_usuario
    return bairro 

for i in range(repeticao):
            idBairro =  #PK
            idCidade =  #FK T_RHSTU_CIDADE
            nmBairro = 
            nmZonaBairro = 
            dataCadastro = aleatorioEstado.hoje
            usuarioNome = aleatorio.nomes()
            usuarioSobreNome = aleatorio.sobrenomes()
            usuarioNomeCompleto = usuarioNome + usuarioSobreNome


            bairro = T_RHSTU_BAIRRO(id_estado=idEstado,sg_estado=sgEstado,nm_estado=nmEstado,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            listaBairros.append(bairro)
            


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