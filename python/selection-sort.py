lista = [7, 5, 1, 8, 3]

for i in range(len(lista) - 1):
    min_index = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[min_index]:
            min_index = j
    if lista[i] > lista[min_index]:
        aux = lista[i]
        lista[i] = lista[min_index]
        lista[min_index] = aux

print(lista)