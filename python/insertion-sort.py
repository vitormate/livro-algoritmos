a = [5, 2, 4, 6, 1, 3]

print(a)

for j in range(1, len(a)):
    chave = a[j]
    i = j - 1
    while i >= 0 and a[i] > chave:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = chave

print(a)