import redis
from json import load

with open('dataset.json', 'r', encoding='utf8') as f:
    dataset = load(f)

redis = redis.Redis(
     host= 'localhost',
     port= '6379'
)

# Reiniciar os valores do banco
redis.flushdb()

chaves = ['dependente', 'funcionario']
valores = {
    'dependente': [
			"nome",
			"data_nascimento",
			"funcionario_id"
    ],
    'funcionario': [
			"nome",
			"logradouro",
			"numero",
			"complemento",
			"bairro",
			"cidade",
			"uf",
			"cep",
			"data_nascimento"
    ]
}

def setup_tables_from_json():
	for tabela in chaves:
		for registro in dataset[tabela]:
				chave = tabela + ':' + str(registro['id'])

				for atributo in valores[tabela]:
						redis.hset(chave, atributo, registro.get(atributo, ''))

def select_all_from_table(table):
	i = 1

	while True:
		data = redis.hgetall(f'{table}:{i}')

		if not data:
			break

		print(data)

		i += 1

setup_tables_from_json()
# Não tem funções tipo select * from user
select_all_from_table('dependente')
select_all_from_table('funcionario')