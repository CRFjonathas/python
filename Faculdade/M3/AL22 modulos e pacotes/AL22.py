import uteis

num = int(input('Digite um valor: '))

fat = uteis.fatorial(num)
double = uteis.dobro(num)
triple = uteis.triplo(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {double}')
print(f'O triplo de {num} é {triple}')