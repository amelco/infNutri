import connect

nomeDB = "paes.db"
test = connect.conectar(nomeDB)

paes = test.selectPaes()
print(paes)
print(paes[0]['nome'])
print(paes[1]['nome'])

test.desconectar()
