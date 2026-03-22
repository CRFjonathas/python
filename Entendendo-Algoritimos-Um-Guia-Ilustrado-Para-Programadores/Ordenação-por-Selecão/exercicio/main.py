def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice 

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

array = []
tam_array = int(input("QUAL O TAMANHO DA SUA LISTA? "))

for i in range(tam_array):
    valor_array = int(input("INSIRA UM VALOR NUMERICO PARA A SUA LISTA: "))
    array.append(valor_array)

print(ordenacaoporSelecao(array))