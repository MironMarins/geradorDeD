import oracledb
import aleatorio
import aleatorioEstado
import aleatorioCidade
import T_RHSTU_ESTADO

listaEstados=T_RHSTU_ESTADO.listaEstados
listaCidades=[]
print(listaEstados)


def T_RHSTU_CIDADE(id_cidade,id_estado,nm_cidade,cd_ibge,nr_ddd,dt_cadastro,nm_usuario):
    cidade = {}
    
    cidade['ID_CIDADE'] = id_cidade #PK
    cidade['ID_ESTADO'] = id_estado #FK
    cidade['NM_CIDADE'] = nm_cidade
    cidade['CD_IBGE'] = cd_ibge
    cidade['NR_DDD'] = nr_ddd
    cidade['DT_CADASTRO'] = dt_cadastro
    cidade['NM_USUARIO'] = nm_usuario
    
    
    return cidade 
contador = 0
for i in range(T_RHSTU_ESTADO.repeticao):
            idCidade = aleatorioEstado.idEstado() #PK
            idEstado = listaEstados[contador]['ID_ESTADO'] #FK
            nmCidade = "Sumé"
            cdIBGE = aleatorio.ids()
            nrDDD = aleatorioCidade.DDD()
            dataCadastro = aleatorioEstado.hoje
            usuarioNomeCompleto = listaEstados[contador]['NM_USUARIO']

            contador=contador+1
            cidade = T_RHSTU_CIDADE(id_cidade=idCidade,id_estado=idEstado,nm_cidade=nmCidade,cd_ibge=cdIBGE,nr_ddd=nrDDD,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            listaCidades.append(cidade)
            print(listaCidades)


try:
    with oracledb.connect(user='rm551801',password='040591',dsn="oracle.fiap.com.br/orcl") as conexao:
        with conexao.cursor() as cur:
             ins = '''INSERT INTO T_RHSTU_CIDADE(ID_CIDADE,ID_ESTADO,NM_CIDADE,CD_IBGE,NR_DDD,DT_CADASTRO,NM_USUARIO) 
             VALUES(:ID_CIDADE,:ID_ESTADO,:NM_CIDADE,:CD_IBGE,:NR_DDD,TO_DATE(:DT_CADASTRO,'YYYY-MM-DD'),:NM_USUARIO)'''        
             for info in listaCidades:
                    cur.execute(ins, info)
                    conexao.commit()
                    
            
            
except oracledb.DatabaseError as erro:
                print("deu erro CIDADE!")
                print(erro)