import connect

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


def calcQtd(qe, pr, pi):
    """qe, pr and pi devem ser listas"""
    return [a / b * c for a, b, c in zip(qe, pr, pi)]


nomeDB = "paes.db"

# conectando ao DB
test = connect.conectar(nomeDB)

# Selecionando o pao
paes = test.selectPaes()
pao = paes[0]['nome']

# Selecionando o peso (quantidade dos elementos de uma lista de
#   ingredientes de um pão específico)
query = "SELECT idEle, pesoEle FROM ElemIngr \
         WHERE idIng IN (\
         SELECT idIng FROM ingPao WHERE idPao IN (\
         SELECT id FROM paes WHERE nome == '" + pao + "')\
         )"
qtdEle = test.execute(query)
for ele in qtdEle:
    print(ele)
    qe = ele[1]


# Selecionando o peso referência dos ingredientes de um pao especifico
query = "SELECT id, peso_ref FROM ingredientes \
         WHERE id IN (\
         SELECT idIng FROM ingPao WHERE idPao IN (\
         SELECT id FROM paes WHERE nome == '" + pao + "')\
         )"
pesoRef = test.execute(query)
for peso in pesoRef:
    print(peso)
    pr = peso[1]



# desconectando do DB
test.desconectar()
