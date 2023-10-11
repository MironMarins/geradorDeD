import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaPacientePlanosDeSaude=[]
repeticao = 2

def T_RHSTU_PACIENTE_PLANO_SAUDE(id_paciente_ps,id_paciente,id_plano_saude,nr_carteira_ps,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    pacientePlanoSaude = {}
    pacientePlanoSaude['ID_PACIENTE_PS'] = id_paciente_ps #P
    pacientePlanoSaude['ID_PACIENTE'] = id_paciente #F
    pacientePlanoSaude['ID_PLANO_SAUDE'] = id_plano_saude #F
    pacientePlanoSaude['NR_CARTEIRA_PS'] = nr_carteira_ps
    pacientePlanoSaude['DT_INICIO'] = dt_inicio
    pacientePlanoSaude['DT_FIM'] = dt_fim
    pacientePlanoSaude['DT_CADASTRO'] = dt_cadastro
    pacientePlanoSaude['NM_USUARIO'] = nm_usuario
    return pacientePlanoSaude 

for i in range(repeticao):
            idPacientePs = #P
            idPaciente = #F
            idPlanoSaude = #F
            nrCarteiraPs =
            dtInicio = 
            dtFim =
            dtCadastro =
            nmUsuario =



            PacientePlanoDeSaude = T_RHSTU_PACIENTE_PLANO_SAUDE(id_paciente_ps=,id_paciente=,id_plano_saude=,nr_carteira_ps=,dt_inicio=,dt_fim=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaPacientePlanosDeSaude.append(PacientePlanoDeSaude)
            


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