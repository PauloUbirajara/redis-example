# Considerando o banco criado
# 1) Buscar todos os funcionários/dependentes
# Scan percorre as chaves a partir de um registro que serve como ponteiro para o próximo e finaliza quando o resultado obtido é 0
scan 0 count 25 match funcionario:*
scan 0 count 25 match dependente:*


# 2) Obter o dependente e o seu funcionário
hgetall dependente:1
hgetall <funcionario_id obtido da query anterior>


# 3) Apagar o dependente com id 2
# HDEL apaga um ou mais atributos de uma tabela hash
# DEL apaga o valor de uma chave
hdel dependente:2 funcionario_id
del dependente:2


# 4) Alterar o parâmetro de um funcionário
# Nesse caso, caso já houver algum registro prévio, ele só altera os existentes
hset funcionario:5 nome Gerinaldo complemento "Complemento para teste"

# Isso faz com que altere o tipo do valor e, como passa de tabela hash para string, não pode mais ser usado o HGET
set funcionario:5 Valor aleatório


# 5) Definir um novo funcionário
hset funcionario:26 id 1 nome Alan logradouro Casa numero 123 complemento 456 bairro Bairro cidade Fortaleza uf CE cep 123456 data_nascimento ?

# Caso precisar de alguma operação para mostrar as outras estruturas não relacionadas ao banco

# Chave valor individual
set nome Renato
get nome
exists nome

# Lista
rpush vetor 1
rpush vetor 2
rpush vetor 3 4
lpush vetor -2 1
lrange vetor 0 -1

# Set/Conjunto (Lista sem repetições)
sadd letras A B B C
sscan letras 0