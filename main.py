import connect

nomeDB = "paes.db"
test = connect.conectar(nomeDB)

paes = test.selectPaes()
print(paes)
print(paes[0]['nome'])
print(paes[1]['nome'])

test.desconectar()

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
