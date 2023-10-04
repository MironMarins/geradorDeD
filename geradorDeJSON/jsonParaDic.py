'''import json

with open('geradorDeJSON\SP.json') as Cidades_SaoPaul:
    dados = json.loads(Cidades_SaoPaul)

print(dados[features])'''

https://github.com/chandez/Estados-Cidades-IBGE/commit/4cb009e429ad4174c46c425c3f5c05c596d244db

#pegar nome de estado

import json

with open("json\estados.json") as meu_json:
    dados = json.load(meu_json)

print(dados['data'][2]['Nome'])