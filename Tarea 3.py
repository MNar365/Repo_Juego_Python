enero = 31
febrero = 28
marzo = 30
abril = 31
mayo = 30
junio = 31
julio = 30
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

print(" Escribe un mes, como nota escribe todo en minuscula")
tutu = input("tapea pib@: ")

if tutu == "enero":
    print(enero)

elif tutu == "febrero":
    print(febrero)

elif tutu == "marzo":
    print(marzo)

elif tutu == "abril":
    print(abril)

elif tutu == "mayo":
    print(mayo)

elif tutu == "junio":
    print(junio)

elif tutu == "julio":
    print(julio)

elif tutu == "agosto":
    print(agosto)

elif tutu == "septiembre":
    print(septiembre)

elif tutu == "octubre":
    print(octubre)

elif tutu == "noviembre":
    print(noviembre)

elif tutu == "diciembre":
    print(noviembre)

lunes = 1
martes = 2
miercoles = 3
jueves = 4
viernes = 5
sabado = 6
domingo = 7
sem = input("escribe un dia de la semana en minuscula pibe:  ")

if sem == "lunes":
    print(lunes)
elif sem == "martes":
    print(martes)
elif sem == "miercoles":
    print(miercoles)
elif sem == "jueves":
    print(jueves)
elif sem == "viernes":
    print(viernes)
elif sem == "sabado":
    print(sabado)
elif sem == "domingo":
    print(domingo)

var1=int(input("Escribe un año"))
if ((var1%4)== 0 ):
    print("Tu año es un año bisiesto")
else:
    print("Tu año no es un año bisiesto")


var2=int(input("Ingresa un numero"))
if ((var2>=0) and (var2<100) and ((var2%2)== 0)):
    print("Tu numero es positivo, menor a 100 y par")
elif ((var2>=0) and (var2<100) and ((var2%2)!= 0)):
    print("Tu numero es positivo, menor a 100 e impar")
elif ((var2>=0) and (var2>=100) and ((var2%2)== 0)):
    print("Tu numero es positivo, mayor o igual a 100 y par")
elif((var2>=0) and (var2>=100) and ((var2%2)!= 0)):
    print("Tu numero es positivo, mayor o igual a 100 e impar")
elif ((var2<0) and (var2<100) and ((var2%2)!= 0)):
    print("Tu numero es negativo, menor a 100 e impar")
else:
    print("Tu numero es negativo, menor a 100 y par")

list_0=["Do","Re","Mi","Fa","Sol","La","Si"]
list_0.insert(0,"Si")
list_0.insert(0,"Si")
list_0.insert(3,"Re")
list_0.insert(5,"Do")
list_0.insert(6,"Si")
list_0.insert(7,"La")
list_0.insert(8,"Sol")
list_0.remove("Mi")
list_0.remove("Fa")
list_0.insert(11,"Si")
list_0.insert(13,"La")
list_0.insert(14,"La")
print(list_0)

list_1=["Jose Miguel","Carlos","Manuel","Memo"]
name=str(input("Escribe un nombre"))
if (name=="Jose Miguel" or name=="Carlos" or name=="Manuel" or name=="Memo"):
    print("True")
else:
    print("False")
