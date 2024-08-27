# P1
# dictionary = {}
# numar = input('Introduceti un numar intre 1-20:')
# while not numar.isdigit() or (int(numar) > 21 or int(numar) <= 0):
#     print('Numarul introdus nu este valid. Introduceti un numar pana la 20 si mai mare decat 20:')
#     numar = input()
#
# for i in range(int(numar)):
#     dictionary[i+1] = (i+1)**2
#
# print(dictionary)

# P2
# def sumaTuplu():
#     tuplu_string = input("Introduceti numerele ce vor face parte din tuplu,separate prin virgula:")
#     tuplu = tuplu_string.split(',')
#     tuplu = [int(numar) for numar in tuplu]
#     print(sum(tuplu))
#
#
# sumaTuplu()


# P3
# def separateLists(listaUtilizator: [str], numarSeparare: int) -> ([int], [int]):
#     listaUtilizatorNumere = [int(item) for item in listaUtilizator.split(',')]
#     lista1 = listaUtilizatorNumere[:numarSeparare]
#     lista2 = listaUtilizatorNumere[numarSeparare:]
#     return lista1, lista2
#
#
# listaUtilizator = input("Introduceti numerele din lista:")
# numarSeparare = input("Cate numere va avea prima lista?")
# rez_lista1, rez_lista2 = separateLists(listaUtilizator, int(numarSeparare))
# print(rez_lista1, rez_lista2)


# P4
# vocale = ["a", "e", "i", "o", "u"]
# sir_caractere = input("Introduceti sirul de caractere:")
# len_vocale_filtrate = len(set(filter(lambda x: x in vocale, sir_caractere)))
# print(len_vocale_filtrate)

# P5 - nu inteleg cerinta!!
# n1, n2, n3 = input("Introduceti numerele:\n"), input(), input()
# if int(n1) == int(n2) == int(n3):
#     print(int(n1), int(n2), int(n3))
# else:
#     print(int(n1) / int(n2) / int(n3))

# P6
# sir_numere = [1, 2, 3, 4, 5, 6, 7]
# sir_final = []
# for i in range(len(sir_numere)):
#     if sir_numere[i] % 2 == 0:
#         sir_final.append(sir_numere[i])
#         sir_final.append(sir_numere[i] * 2)
#     else:
#         sir_final.append(sir_numere[i])
# print(sir_final)
