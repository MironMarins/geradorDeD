import oracledb

conn = oracledb.connect(user='rm551801',password='040591', dsn="oracle.fiap.com.br/orcl")
print("Database version: ", conn.version)
#CRIAR CURSOR
cur = conn.cursor()
#cur.execute('SELECT * FROM TB_PSH_PATAKI_PRODUTO')
#CHECAR IMFORMAÇÕES
#rows = cur.fetchall()
#for reg in rows:
  #print(reg)
#INSERIR
#cur.execute("INSERT INTO TB_PSH_PATAKI_PRODUTO(ID_PRODUTO,DS_PROD,VL_UNITARIO,DS_UNIDADE) VALUES (:ID_PROD,:DS_PROD,:VL_UNIT,:DS_UNID)", {'ID_PROD':99999,'DS_PROD':'ração do toto','VL_UNIT':100,'DS_UNID':'u'})