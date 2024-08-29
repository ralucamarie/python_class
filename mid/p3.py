def divideList(lista: list, prag: int):
    listSmall = [x for x in lista if x < prag]
    listLarge = [x for x in lista if x >= prag]
    return listSmall, listLarge


listEx = [5, 2, 9, 1, 5, 6]

prag = input("Introduceti pragul:\n")
while (int(prag) > max(listEx) or int(prag) < min(listEx)):
    prag = input(f"Introduceti pragul, un numar intre: {min(listEx)} si {max(listEx)}\n")

print(divideList(listEx, int(prag)))
