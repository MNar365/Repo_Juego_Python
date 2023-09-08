
#Ejercicio 1
print("Comienza el ejercicio 1")
corr=int(input("Dicta el valor de corriente"))
res=int(input("Dicta el valor de resistencia"))
volt=str(corr*res)
print("El voltaje es igual a " + volt)

#Ejercicio 2
print("Comienza el ejercicio 2")
cost=int(input("Cuanto costaba un vuelo el año pasado?"))
dif=str(8000-cost)
por=str(1-(cost/8000))
print("La diferencia es "+ dif)
print("El cambio porcentual es " + por)

#Ejercicio 3
print("Comienza el ejercicio 3")
num=int(input("Escribe un numero"))
if((num%2)==0):
    print("Tu numero es par")
else:
    print("Tu numero es impar")

#Ejercicio 4
print("Comienza el ejercicio 4")
libros=["Biblia","Coran","Principito","El diario de Greg","Programacion en Pyhton","Algoritmos avanzados","Algebra de Baldor"]
libros.insert(0,"El señor de los anillos")
libros.insert(0,"Pulgarcito")
libros.insert(0,"Jurassic Park")
libros.insert(0,"Frankenstein")
libros.pop
libros.pop
libros.pop
libros.pop
libros.insert(0,"El diario de Greg")
libros.insert(0,"Programacion en Python")
print(libros)

#Ejercicio 5
print("Comienza el ejercicio 5")
apo_0=int(input("Introduce el apotema del pentagono"))
lad_0=int(input("Introduce el lado del pentagono"))
per_0=(lad_0*5)
apo_1=int(input("Introduce el apotema del hexagono"))
lad_1=int(input("Introduce el lado del hexagono"))
per_1=(lad_1*5)
a_pen=(apo_0*per_0)
a_hex=(apo_1*per_1)
if (a_pen < a_hex):
    print("El area del hexagono es mayor")
elif (a_pen > a_hex):
    print("El area del pentagono es mayor")
else:
    print("Las areas son iguales")

'''#6
.pop
.insert

#7
La instruccion .len

#8
Un string es una cadena de caracters, puede ser una palabra, una cadena de numeros o cualquier otra union de 1 o mas caracteres

#9
int=numeros enteros que pueden ser usados en aritmetica o algebra
float=numeros con decimales que pueden ser usados en aritmetica o algebra
string=una cadena de uno o mas caracteres, no puede ser usado en matematica a menos que sea con otros strings para concatenarse
boolean=son los resultados de operaciones booleanas, pueden ser verdadero o falso

#10
una variable es un contenedor en el que se puede guardar un dato de cualquier tipo

#11
or requiere que solo uno de sus resultados sean verdaderos para obtener el resultado de verdader
and requiere que todos sus resultados sean veradero para obtener el resultado de verdadero
not invierte el resultado de toda funcion booleana a la que se aplica, si el resultado es true not lo convierte a false y viceversa
'''

#12
print("Comienza el challenge 12")
arista_1=int(input("Introduce cuanto mide el lado del triangulo"))
alt_tri=(((arista_1^2)-((.5*arista_1)^2))^.5)
area_tri=str((alt_tri*arista_1)/2)
print("El area del triangulo es " + area_tri)

#13
print("Comienza el challenge 13")
texto_0=str(input("Escribe un texto"))
cont_0=(texto_0.len)
if (cont_0>500):
    print("Error, tu texto es mas largo que 500 caracteres.")
else:
    print("Tu texto tiene " + cont_0 " caracteres")

