import aleatorioEstado
import datetime as dt
import csv
hoje = dt.date.today()
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

for i in range(0,len(aleatorioEstado.estados)):
            idEstado = i #PK
            nmEstado = aleatorioEstado.estados[i]
            print(nmEstado)
            sgEstado = aleatorioEstado.siglas(nmEstado)
            print(sgEstado)
            dataCadastro = hoje
            usuarioNomeCompleto = "Miron"
            if i == 1:
                    print("1")
            elif i == 100: 
                    print("100")
            elif i == 1000: 
                    print("1000")
            elif i == 10000: 
                    print("10000")
            elif i == 100000: 
                    print("100000")
            elif i == 1000000: 
                    print("1000000")
            elif i == 2500000: 
                    print("2500000")
            elif i == 5000000: 
                    print("5000000")
            elif i == 7500000: 
                    print("7500000")
            elif i == 9000000: 
                    print("9000000")


            estado = T_RHSTU_ESTADO(id_estado=idEstado,sg_estado=sgEstado,nm_estado=nmEstado,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            listaEstados.append(estado)
            
print(listaEstados)
with open('primarios\\T_RHSTU_ESTADO\\T_RHSTU_ESTADO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        # Criando objeto de Escrita do CSV
        csv_writer = csv.DictWriter(file_csv, fieldnames=listaEstados[0].keys())

        # Escrevendo headers (Nome das colunas do CSV)
        csv_writer.writeheader()

        # Percorrendo o dicionario de dados
        for line in listaEstados:
            # Escrevendo linha por linha
            csv_writer.writerow(line)

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