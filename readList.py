def readList(list):
    """Read a string of format '{1 2 3 4 5}' and returns
    a integer list [1, 2, 3, 4, 5]"""
    stlst = list[1:-1]
    stlst = stlst.split(" ")
    intlst = [int(x) for x in stlst]
    return intlst


lst = "{1 2 3 4 5 6}"
print(readList(lst))
