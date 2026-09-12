#calculadora media faculdade 
n1=float(input("Digite o valor da N1 :"))
institucional=float(input("Digite o valor da Institucional :"))
n2=float(input("Digite o valor da N2 :"))
media=(n1+(institucional+n2)/2)/2
print("A média é:", media)
if media>=6:
    print("Aprovado")
elif media<6 and media>=4:
    print("Você está de recuperação")
else:
    print("Reprovado")
