




from math import sqrt
v1 = float(input('Valor 1: '))
v2 = float(input('Valor 2: ')) 

print(f'Valores recebidos: {v1} e {v2}')
print(f'O valor absoluto de {v2} é: {abs(v2)}')
print(f'O valor de {v1} elevado a {v2} é: {v1**v2}')
print(f'A raiz de {v1} é: {sqrt(v1)}')
print(f'O valor de {v2} arredondado é: {round(v2)}')
print(f'A parte inteira de {v2} é : {int(v2)}')
print(f'O valor de {v1} em moeda é: R$ {v1:,.2f}')