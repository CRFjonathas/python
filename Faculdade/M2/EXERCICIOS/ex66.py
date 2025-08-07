soma = count = 0

while True:
    num = int(input('Digite um numero: (999 para parar) '))
    count += 1
    if num == 999:
        break
    soma += num
print(f'A soma dos valores digitados foi: {soma}')
print(f'Você digitou {count} valores')
