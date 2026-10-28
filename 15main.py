import math 
n1=float(input("digite o  A: "))
n2=float(input("digite o B: "))
n3=float(input("digite o C: "))
if (n1==0):
    print("A equação não é do segundo grau")
else:
    d=(n2**2)-4*n1*n3
    raiz=math.sqrt(d)
    x1= (-n2+raiz)/2*n1
    x2= (-n2-raiz)/2*n1
    if d > 0:
        print("Possui duas raizes, {} ,{}" .format(x1, x2))
    elif d == 0:
        print("Possui uma raiz , {}" .format(x1))
    else:
        print("Não possui raizes ")
         
 
    