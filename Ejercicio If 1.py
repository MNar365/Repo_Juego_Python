var1=int(input())
if var1>21:
    print("Tienes mas de 21 años")
else:
    print("Tienes 21 años o menos")

var2=int(input())
var3=int(input())
var4=int(input())
if ((var1<var2) and (var3<var2)):
    print (var2)
elif ((var2<var1)and (var3<var1)):
    print(var1)
else:
    print(var3)

