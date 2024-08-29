def generate_dict(key_no: int):
    dictionar_nou ={}
    for i in range(1, key_no+1):
        dictionar_nou[i] = sum(range(1, i+1))
    return dictionar_nou


nr_chei = input("Introduceti nr de chei:\n");

while (int(nr_chei) > 15):
    nr_chei = input("Nr de chei nu poate fi mai mare decat 15!\n Introduceti un nou nr de chei:\n")

print(generate_dict(int(nr_chei)))