from collections import OrderedDict
from operator import itemgetter

"""
1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de

caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.

In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de

caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru

preluat automat de la tastatura.
"""

# text = input("Introduceti textul:")
# isString = True
# for letter in text:
#     if letter in '0123456789':
#         isString = False
#         break
# if isString:
#     print('Sirul de caractere a fost gasit de catre Raluca')


"""
 Creati un program in care utilizatorul sa introduca un numar. Validati daca acest

numar este par sau impar si afisati un raspuns in acest sens.
"""
# text = input("Introduceti textul:")
# par = False
# if text.isnumeric():
#     par = int(text) % 2 == 0
# else:
#     print("Nu e numar")
#
# print("Numar Par") if par else print("Numar Impar")

"""
Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este

bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact

la 4 (fara rest)
"""

# text = input("Introduceti anul:")
# if(text.isnumeric() and len(text)==4 and text[0]!=0):
#     numText = int(text)
#     anBisect = True
#     if numText % 4 != 0:
#         anBisect = False
#     elif numText % 100 != 0:
#         anBisect = True
#     elif numText % 400 != 0:
#         anBisect = False
#     print("An bisect!") if anBisect else print("Nu este an bisect!")

"""
Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul

este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic

decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul

este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si

afisati numarul pozitiv.
"""

# text = float(input("Introduceti un numar:"))
#
# if text == 0:
#     print('Numarul este 0')
# elif text < 0:
#     positiveNumber = text * -1
#     print(int(positiveNumber))
# else:
#     print('Numarul mai mic decat 10') if text < 10 else print('Numarul este mai mare decat 10')

"""
Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea

de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare

acest sir de caractere:
"""
# text = input("1 – Afisare lista de cumparaturi\n2 – Adaugare element\n3 – Stergere elemen\n4 – Sterere lista de cumparaturi\n5 - Cautare in lista de cumparaturi\n")
#
# match text:
#     case '1':
#         print('Afisare lista de cumparaturi')
#     case '2':
#         print('Adaugare element')
#     case '3':
#         print('Stergere elemen')
#     case '4':
#         print('Sterere lista de cumparaturi')
#     case '5':
#         print('Cautare in lista de cumparaturi')
#     case _:
#         print('Alegerea nu exista. Reincercati')

"""
Avand doua liste, afisati o lista a elementelor comune ambelor liste
"""
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = []
#
# for element in a:
#     if (element in b) and (element not in result):
#         result.append(element)
# print(result)

"""
Avand o lista de utilizatori si filme vizionate, listati 

Cel mai vizionat film - Fight Club in cazul de mai sus

Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus

Extra
Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...

Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan"""

listaUtilizatori = [
    {
        'nume': 'George',
        'filme': ['Shrek', 'Bond', 'Fight Club']
    },
    {
        'nume': 'Cristian',
        'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
    },

    {
        'nume': 'Stefan',
        'filme': ['Fight Club', 'Slumdog Milionare']
    }
]

movieStatistics = {}
userStatistics = {}


def topFilms():
    global movieStatistics
    for utilizator in listaUtilizatori:
        for film in utilizator['filme']:
            if film in movieStatistics:
                movieStatistics[film] += 1
            else:
                movieStatistics[film] = 1


def sort_dict_by_value_reverse(dictionary: dict, direction: str):
    sortDesc = True if direction == 'desc' else False
    sorted_dictionary = sorted(dictionary.items(), key=itemgetter(1), reverse = sortDesc)
    return OrderedDict(sorted_dictionary)

def topUsers():
    global userStatistics
    for utilizator in listaUtilizatori:
        if not utilizator['nume'] in userStatistics:
            userStatistics[utilizator['nume']] = len(utilizator['filme'])

#Rezolvare
topFilms()
sortedMovieStatistics = sort_dict_by_value_reverse(movieStatistics, 'desc')
topUsers()
sortedUsersByMovies = sort_dict_by_value_reverse(userStatistics, 'desc')

# Afisare statistici
print('Cel mai vizionat films:\n' + list(sortedMovieStatistics)[0])
print('Cel mai activ utilizator:\n' + list(sortedUsersByMovies)[0])
print('Top filme dupa vizionari:')
print(list(sortedMovieStatistics))
print('Top utilizatori:')
print(list(sortedUsersByMovies))


