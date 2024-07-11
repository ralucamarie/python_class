dictionar = {}
print(type(dictionar))
dictionar = {
    'cheie1': 12,
    'cheie2': 333,
    'cheie3': 100,
    40: 'valoare'
}
print(dictionar['cheie2'])
# cu eroare daca nu exista
# print(dictionar['cheie4'])
# nu da eroare,  returneaza none si poate primi si vloare in caz ca val nu exista
# print(dictionar.get('cheie4', "Nu exista!"))
# dictionar['cheie4'] = 'valoare noua'
dictionar.update({
    'cheie4': 'val noua',
    'cheie5': 'val noua second'
})
print(dictionar.keys())
print(dictionar)

