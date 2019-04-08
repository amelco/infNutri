import connect

nomeDB = "paes.db"

"""
Para a composição da tabela nutricional, são necessários:
1. quantidade da composição de cada elemento dos ingredientes da receita (qe)
2. peso de referencia de cada ingrediente (pr)
3. peso de cada ingrediente utilizado na receita (pi)

A quantidade (peso) de cada elemento é, então, calculada como:
        qe / pr * pi

qe se localiza na tabela: ElemIngr.pesoEle
pr se localiza na tabela: ingredientes.peso_ref
pi se localiza na tabela: ingPao.pesoIng
"""

# conectando ao DB
test = connect.conectar(nomeDB)

# Selecionando os paes
paes = test.selectPaes()

# visualizando resultados
print(paes)
print(paes[0]['nome'])
print(paes[1]['nome'])

# Selecionando o peso (quantidade dos elementos de uma lista de
#   ingredientes de um pão específico)
query = "SELECT idEle, pesoEle FROM ElemIngr \
         WHERE idIng IN (\
         SELECT idIng FROM ingPao WHERE idPao == 2\
         )"
# query = "SELECT * FROM ingPao WHERE idPao == 2"

print(test.execute(query))

# desconectando do DB
test.desconectar()
