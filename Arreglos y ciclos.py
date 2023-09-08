frase=str(input(print("Menciona una frase")))
frase_reves= frase.reverse()
if (frase==frase_reves):
    print("Tu frase es un palindromo")
else:
    print("Tu frase no es un palindromo")

lista = []

for i in range(5):
    lista.appendi(i+1)

print(lista)

lista_1 = [1,2,3,4,5,6,7,8,9,10]

lista_1.pop()

for i in range(5):
    lista_1.remove(i+1)

for i in range(3):
    lista_1.insert(0,3)

print(lista_1)



