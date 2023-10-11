import oracledb
import aleatorio
import aleatorioEstado
PlanosDeSaude=[]
repeticao = 2

def T_RHSTU_PLANO_SAUDE(id_plano_saude,ds_razao_social,nm_fantasia_plano_saude,ds_plano_saude,
                        nr_cnpj,nm_contato,ds_telefone,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    planoSaude = {}
    planoSaude['ID_PLANO_SAUDE'] = id_plano_saude #P
    planoSaude['DS_RAZAO_SOCIAL'] = ds_razao_social
    planoSaude['NM_FANTASIA_PLANO_SAUDE'] = nm_fantasia_plano_saude #F
    planoSaude['DS_PLANO_SAUDE'] = ds_plano_saude
    planoSaude['NR_CNPJ'] = nr_cnpj
    planoSaude['NM_CONTATO'] = nm_contato
    planoSaude['DS_TELEFONE'] = ds_telefone
    planoSaude['DT_INICIO'] = dt_inicio
    planoSaude['DT_FIM'] = dt_fim
    planoSaude['DT_CADASTRO'] = dt_cadastro
    planoSaude['NM_USUARIO'] = nm_usuario
    return planoSaude 

for i in range(repeticao):
            
            idPlanoSaude =
            dsRazaoSocial =
            nmFantasiaPlanoSaude =
            dsPlanoSaude =
            nrCNPJ =
            nmContato =
            dsTelefone =
            dtInicio =
            dtFim =
            dtCadastro =
            nmUsuario =


            PlanoDeSaude = T_RHSTU_PLANO_SAUDE(id_plano_saude=,ds_razao_social=,nm_fantasia_plano_saude=,ds_plano_saude=,nr_cnpj=,nm_contato=,ds_telefone=,dt_inicio=,dt_fim=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            PlanosDeSaude.append(PlanoDeSaude)
            


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