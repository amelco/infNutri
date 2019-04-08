import sqlite3


class conectar(object):
    """docstring for conectar"""

    def __init__(self, nomeDB):
        self.nomeDB = nomeDB
        self.con = sqlite3.connect(nomeDB)
        self.c = self.con.cursor()

    def selectPaes(self):
        """Seleciona todos os paes e retorna uma lista de tuples"""
        res = []
        for r in self.c.execute("SELECT * FROM paes"):
            # print(r)
            res.append({"nome": r[1], "peso": r[2]})
        return res

    def desconectar(self):
        self.c.close()
