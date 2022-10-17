import os


imput:os
c:str
compra: float; cv: float; cp; float; ct: float
compra= 0
cv= 0
cp= 0


for n in range (1,16):
    print(f"Dados da {n}ª venda")
    c = imput('digite o código da compra(v-a vista ou - a prazo):')


if c == 'v':
     compra = float(imput("digite o valor da compra: R$ "))
     CV = CV + compra
elif c == 'p':
     compra=float(imput("digíte o valor da compra: R$"))
     cp = cp + compra

     os.systen('cls')

print(f"o valor total à vista: R$ {cv:2f}")
print(f"o valor total à prazo: R$ {cp:2f}")
print(f"o valor total das compras: R$ {cp+ cv:2f}")
print(f"o valor da primeira prestaçâo das compras a prazo juntas: R${cp/3:2f}")


