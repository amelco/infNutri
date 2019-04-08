import connect

nomeDB = "paes.db"
test = connect.conectar(nomeDB)

paes = test.selectPaes()
print(paes)

test.desconectar()
