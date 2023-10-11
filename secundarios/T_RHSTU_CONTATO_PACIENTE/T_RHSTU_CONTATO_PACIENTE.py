import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaContatoPacientes=[]
repeticao = 2

def T_RHSTU_CONTATO_PACIENTE(id_paciente,id_contato,id_tipo_contato,nm_contato,nr_ddi,nr_ddd,nr_telefone,dt_cadastro,nm_usuario):
    contato_paciente = {}
    
    contato_paciente['ID_PACIENTE'] = id_paciente #PF
    contato_paciente['ID_CONTATO'] = id_contato #P
    contato_paciente['ID_TIPO_CONTATO'] = id_tipo_contato#F
    contato_paciente['NM_CONTATO'] = nm_contato
    contato_paciente['NR_DDI'] = nr_ddi
    contato_paciente['NR_DDD'] = nr_ddd
    contato_paciente['NR_TELEFONE'] = nr_telefone
    contato_paciente['DT_CADASTRO'] = dt_cadastro
    contato_paciente['NM_USUARIO'] = nm_usuario
    return contato_paciente

for i in range(repeticao):
            idPaciente = #PF
            idContato = #P
            IdTipoContato = #F
            nmContato = 
            nrDDI = aleatorioEstado.hoje 
            nrDDD =
            nrTelefone =
            dtCadastro =
            usuarioNome = aleatorio.nomes()
            usuarioSobreNome = aleatorio.sobrenomes()
            usuarioNomeCompleto = usuarioNome + usuarioSobreNome


            ContatoPaciente = T_RHSTU_CONTATO_PACIENTE(id_paciente=,id_contato=,id_tipo_contato=,nm_contato=,nr_ddd=,nr_ddi=,nr_telefone=,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            ListaContatoPacientes.append(ContatoPaciente)
            


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