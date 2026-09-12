#calculadora de frete para restaurante 
km=float(input("Digite quantos quilometros é do restaurante ao local de entrega : "))
valorcompra=float(input("Digite o valor da compra : "))
if valorcompra >= 100:
    print("O frete é gratuito")
else:
    entrega=5+km*1.5
    print("O valor do frete é de R$",entrega)