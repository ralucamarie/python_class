import sys
from datetime import datetime

# introducere cnp de la tastatura
cnp = input("Introduceti CNP-ul\n")


# functie validare daca sunt 13 cifre si sunt numere toate
def characterValidation():
    return cnp.isnumeric() and len(cnp) == 13


def sexValidation():
    return sex <= 9 and sex != 0


def yearValidation():
    currentYear = datetime.today().year
    # sexul este deja un int din 1 cifra deci poate avea valori intre 0-9. Anul poate fi un int dintr-o cifra sau doua,
    # mai mare sau egal cu 0, mai mic sau egal cu 99, cu exceptia in care
    # sexul este 5 sau 6, caz in care anul maxim, poate fi anul curent.
    if sex == 0:
        return False
    elif sex in [5, 6]:
        return 0 <= an <= currentYear % 100
    else:
        return True


def leapYear():
    anIntreg = 0
    if sex in [1, 2, 7, 8, 9]:
        anIntreg = int('19' + str(an))
    elif sex in [3, 4]:
        anIntreg = int('18' + str(an))
    elif sex in [5, 6]:
        anIntreg = int('20' + str(an))

    if anIntreg % 4 != 0:
        return False
    elif anIntreg % 100 != 0:
        return True
    elif anIntreg % 400 != 0:
        return False
    else:
        return True


def dayAndMonthValidation():
    longMonths = [1, 3, 5, 7, 8, 10, 12]
    shortMonths = [4, 6, 9, 11]
    valid = True

    if 0 in [luna, zi] or luna > 12 or zi > 31:
        valid = False
    elif luna == 2:
        valid = (leapYear() and zi <= 29) or (not leapYear() and zi <= 28)
    elif luna in longMonths:
        valid = (zi <= 31)
    elif luna in shortMonths:
        valid = (zi <= 30)
    return valid


def countyValidation():
    invalid = not (46 < judet < 51)
    return (0 < judet <= 52) and invalid


def codeValidation():
    return 0 < nnn <= 999


def controlValidation():
    controlSequence = list('279146358279')
    listCnp = list(cnp)
    listCnp.pop()
    checkSum = 0
    for index, el in enumerate(listCnp):
        checkSum += int(el) * int(controlSequence[index])
    return control == 1 if checkSum % 11 == 10 else control == (checkSum % 11)


def cnpValidation():
    if not sexValidation():
        print('Sex Validation failed')
    if not yearValidation():
        print('Year Validation failed')
    if not dayAndMonthValidation():
        print('Day and Month Validation failed')
    if not countyValidation():
        print('County Validation failed')
    if not codeValidation():
        print('Code Validation failed')
    if not controlValidation():
        print('Control Validation failed')
    return (sexValidation()
            and yearValidation()
            and dayAndMonthValidation()
            and countyValidation()
            and codeValidation()
            and controlValidation())


# APP
# verificare numar si tip caractere
if not characterValidation():
    print("Numarul sau tipul caracterelor introduse, nu sunt valide")
    sys.exit()

# separare coduri din CNP S AA LL ZZ JJ NNN C - functie pentru fiecare
sex = int(cnp[0])
an = int(cnp[1:3])
luna = int(cnp[3:5])
zi = int(cnp[5:7])
judet = int(cnp[7:9])
nnn = int(cnp[9:12])
control = int(cnp[-1])

# returnare rezultat
print('CNP Valid!') if cnpValidation() else print('CNP invalid')
