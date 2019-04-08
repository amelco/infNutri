import sqlite3
from math import floor


def readList(list):
    """Read a string of format '{1 2 3 4 5}' and returns
    an float list [1, 2, 3, 4, 5]"""
    stlst = list[2:-1]
    stlst = stlst.split(" ")
    fltlst = [float(x) for x in stlst]
    return fltlst


def getInsert(file, tabela, tipo):
    """Lê valores separados por vírgula de um arquivo e monta o
    INSERT INTO statement
    Se a linha começar com #, é considerada comentário e não é lida"""
    r = "INSERT INTO " + tabela + " values (1,'"
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
        if tipo == 1:
            r += line + "'), (" + str(n) + ",'"
            n += 1
        elif tipo == 2 or 3:
            ls = line.split(",")
            # r += ls[0] + "'," + ls[1] + "), (" + str(n) + ",'"
            n += 1
            elem = readList(ls[2])

            # cria tabela de intermediação
            if tipo == 2:
                qtdelem = readList(ls[3])
                r += ls[0] + "'," + ls[1] + "), (" + str(n) + ",'"
                tabIntermed = "ElemIngr"
                criaTabela(tabIntermed, "idEle int, idIng int, pesoEle int")
                # values = getValues(elem, n - 2)
                id = n - 2
                values = "("
                for i in range(0, len(elem)):
                    values += str(floor(elem[i])) + "," + str(id) + ","\
                                                  + str(qtdelem[i]) + "), ("
                values = values[:-3]
                insertValues = "INSERT INTO " + tabIntermed + " values "\
                                              + values
            if tipo == 3:
                qtdelem = readList(ls[3])
                r += ls[0] + "'," + ls[1] + "), (" + str(n) + ",'"
                tabIntermed = "IngPao"
                criaTabela(tabIntermed, "idIng int, idPao int, pesoIng int")
                # values = getValues(elem, n - 2)
                id = n - 2
                values = "("
                for i in range(0, len(elem)):
                    values += str(floor(elem[i])) + "," + str(id) + ","\
                                                  + str(qtdelem[i]) + "), ("
                values = values[:-3]
                insertValues = "INSERT INTO " + tabIntermed + " values "\
                                              + values
            print(insertValues)
            c.execute(insertValues)
    return r


def getValues(lista, id):
    r = "("
    for item in lista:
        r += str(floor(item)) + "," + str(id) + "), ("
    return r[:-3]


def criaTabela(nome, colunas):
    dropTable = "DROP TABLE IF EXISTS " + nome
    c.execute(dropTable)
    createTable = "CREATE TABLE " + nome + "(" + colunas + ")"
    c.execute(createTable)


def preencheTabela(nome, file, tipo):
    insertValues = getInsert(file, nome, tipo)
    print(insertValues)
    c.execute(insertValues)
    conn.commit()


def verTabela(nome):
    # visualiza a tabela
    pesq = "SELECT * FROM " + nome
    res = conn.execute(pesq)
    for r in res:
        print(r)


def listarTudo():
    """Lista todas as tabelas e suas colunas"""
    ex = "SELECT m.name as tableName, \
               p.name as columnName \
        FROM sqlite_master m \
        left outer join pragma_table_info((m.name)) p \
             on m.name <> p.name \
        order by tableName, columnName;"
    res = c.execute(ex)
    for r in res:
        print(r)


def createDB():
    criaTabela(tblEle, eleCol)
    criaTabela(tblIng, ingCol)
    criaTabela(tblPao, paoCol)
    preencheTabela(tblEle, eleFil, 1)
    preencheTabela(tblIng, ingFil, 2)
    preencheTabela(tblPao, paoFil, 3)


name = "paes.db"

tblEle = "elementos"
eleCol = "id int PRIMARY KEY,\
          nome char(100) NOT NULL"
eleFil = "elementos.csv"

tblIng = "ingredientes"
ingCol = "id int PRIMARY KEY, nome char(100), peso_ref int"
ingFil = "ingredientes.csv"

tblPao = "paes"
paoCol = "id int PRIMARY KEY, nome char(100), peso int"
paoFil = "paes.csv"

conn = sqlite3.connect(name)    # tabela física (em arquivo)
# conn = sqlite3.connect(":memory:")   # tabela na memória (volátil)
c = conn.cursor()
createDB()
listarTudo()
# verTabela(tblEle)
# verTabela(tblIng)
# verTabela(tblPao)
verTabela("ElemIngr")
verTabela("IngPao")
conn.close()
