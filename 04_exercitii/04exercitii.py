
def processList(element):
    return element+1


lista = [1, 2, 3]
newMAp = map(processList, lista)
print(newMAp)
print(list(newMAp))

