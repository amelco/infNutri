import sqlite3
from math import floor


def readList(list):
    """Read a string of format '{1 2 3 4 5}' and returns
    an float list [1, 2, 3, 4, 5]"""
    stlst = list[2:-1]
    stlst = stlst.split(" ")
    fltlst = [float(x) for x in stlst]
    return fltlst


def getInsert(file, tabela):
    """Lê valores separados por vírgula de um arquivo e monta o
    INSERT INTO statement
    Se a linha começar com #, é considerada comentário e não é lida"""
    r = "INSERT INTO " + tabela + " values (1,'"
    r2 = []
    f = open(file, "r")
    n = 2
    for line in f.read().split('\n'):
        # sai do loop caso linha seja vazia (EOF)
        if line == "":
            r = r[:-len(str(n)) - 5]
            break
        # pula linha que comece com '#'
        if line[0] == "#":
            continue
        if tabela == "elementos":
            r += line + "'), (" + str(n) + ",'"
            n += 1
        elif tabela == "ingredientes" or "paes":
            ls = line.split(",")
            elem = readList(ls[2])

            # cria tabela de intermediação
            if tabela == "ingredientes":
                tabIntermed = "ElemIngr"
            if tabela == "paes":
                tabIntermed = "IngPao"

            qtdelem = readList(ls[3])
            r += ls[0] + "'," + ls[1] + "), (" + str(n) + ",'"
            n += 1
            id = n - 2
            values = "("
            for i in range(0, len(elem)):
                values += str(floor(elem[i])) + "," + str(id) + ","\
                                              + str(qtdelem[i]) + "), ("
            values = values[:-3]
            insertValues = "INSERT INTO " + tabIntermed + " values "\
                                          + values
            r2.append(insertValues)
        # print(r)
    r2.append(r)
    return r2


dbName = "paes.db"

# creating tables
with sqlite3.connect(dbName) as conn:
    c = conn.cursor()
    querys = [
        'CREATE TABLE elementos (\
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            nome TEXT NOT NULL\
        )',
        'CREATE TABLE ingredientes (\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            nome TEXT NOT NULL,\
            peso_ref INTEGER NOT NULL\
        )',
        'CREATE TABLE paes (\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            nome TEXT NOT NULL,\
            peso INTEGER NOT NULL\
        )',
        'CREATE TABLE ElemIngr (\
            idEle INTEGER NOT NULL,\
            idIng INTEGER NOT NULL,\
            pesoEle INTEGER NOT NULL\
        )',

        'CREATE TABLE IngPao (\
        idIng INTEGER NOT NULL,\
        idPao INTEGER NOT NULL,\
        pesoIng REAL NOT NULL\
        )'
    ]
    for query in querys:
        c.execute(query)

# populating tables
with sqlite3.connect(dbName) as conn:
    c = conn.cursor()
    querys = [
        getInsert("elementos.csv", "elementos"),
        getInsert("ingredientes.csv", "ingredientes"),
        getInsert("paes.csv", "paes")
    ]
    for query in querys:
        for q in query:
            # print(q)
            c.execute(q)
