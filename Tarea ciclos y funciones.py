#Ejercicio 1
n = int(input("Introduce un numero entero "))
acum = 0
cont = 1
while cont<=n:
    acum = acum + cont
    cont = cont + 12

print (acum)

#Ejercicio 2
var_1 = int(input("Introduce un numero entero "))
cont_1 = 0
acum_1 = 0
prom = float
while var_1 != 0:
    acum_1 = acum_1 + var_1
    cont_1 = cont_1 + 1
    var_1 = int(input("Introduce otro numero entero "))

if var_1 == 0:
    prom = acum_1/cont_1

print(prom)

#Ejercicio 3
lista_1 = []
item = str
var_2 = int(input("Cuantos items tendra la lista? "))
cont_2 = 1
while cont_2<=var_2:
    item = input("Que quieres agregar a la lista? ")
    lista_1.append (item)
    cont_2 = cont_2 + 1
lista_1.sort()
print(lista_1)

#Ejercicio 4
lista_2 = []
var_3 = int(input("Cuantos numeros tendra la lista? "))
cont_3 = 1
while cont_3<=var_3:
    num = int(input("Agrega un numero entero a la lista "))
    if (num%2)==0:
        lista_2.append(num)
    cont_3 = cont_3 + 1
print(lista_2)  

#Ejercicio 6
def divi243(a):
    if (a%243)==0:
        res = True
    else:
        res = False
    return res
a = int(input("Ingresa un numero entero "))
result = divi243(a)
print(result)

#Ejercicio 7
def multiplicarString(a,b):
    a = a*b
    return a
a = str(input("Escribe una palabra "))
b = int(input("Escribe el numero para multiplicar la palabra "))
mult = multiplicarString(a,b)
print(mult)



    




