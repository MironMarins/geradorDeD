import aleatorioPlanoSaude
import csv
import datetime as dt
hoje = dt.date.today()
ListaPlanosDeSaude=[]


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
i=0
while i < len(aleatorioPlanoSaude.planos_de_saude_reais):
       
            dsRazaoSocial = aleatorioPlanoSaude.planos_de_saude_reais[i]
            nmFantasiaPlanoSaude = aleatorioPlanoSaude.planos_de_saude_reais[i]
            dsPlanoSaude = aleatorioPlanoSaude.descricaoPS()
            nrCNPJ = aleatorioPlanoSaude.cnpjReais[i]
            nmContato = aleatorioPlanoSaude.nomes()
            dsTelefone = aleatorioPlanoSaude.randTelefones()
            dtInicio = aleatorioPlanoSaude.dataFundacao(aleatorioPlanoSaude.idades())
            dtFim = "None"
            dtCadastro = hoje
            nmUsuario = "Miron"
            i=i+1
            idPlanoSaude = i

            PlanoDeSaude = T_RHSTU_PLANO_SAUDE(id_plano_saude=idPlanoSaude,ds_razao_social=dsRazaoSocial,nm_fantasia_plano_saude=nmFantasiaPlanoSaude,ds_plano_saude=dsPlanoSaude,nr_cnpj=nrCNPJ,nm_contato=nmContato,ds_telefone=dsTelefone,dt_inicio=dtInicio,dt_fim=dtFim,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaPlanosDeSaude.append(PlanoDeSaude)
            
with open('primarios\\T_RHSTU_PLANO_SAUDE\\T_RHSTU_PLANO_SAUDE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        # Criando objeto de Escrita do CSV
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaPlanosDeSaude[0].keys())

        # Escrevendo headers (Nome das colunas do CSV)
        csv_writer.writeheader()

        # Percorrendo o dicionario de dados
        for line in ListaPlanosDeSaude:
            # Escrevendo linha por linha
            csv_writer.writerow(line)

#try:
    #with oracledb.connect(user='rm551801',password='040591',dsn="oracle.fiap.com.br/orcl") as conexao:
        #with conexao.cursor() as cur:
             #ins = '''INSERT INTO T_RHSTU_ESTADO(ID_ESTADO,SG_ESTADO,NM_ESTADO,DT_CADASTRO,NM_USUARIO) 
             #VALUES(:ID_ESTADO,:SG_ESTADO,:NM_ESTADO,TO_DATE(:DT_CADASTRO,'YYYY-MM-DD'),:NM_USUARIO)'''        
             #for info in listaEstados:
                    #cur.execute(ins, info)
                    #conexao.commit()
                    
            
            
#except oracledb.DatabaseError as erro:
                #print("deu erro ESTADO!")
                #print(erro)