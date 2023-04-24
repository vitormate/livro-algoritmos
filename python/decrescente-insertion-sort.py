a = [31, 41, 59, 26, 41, 58]

print(a)

for j in range(1, len(a)):
    chave = a[j]
    i = j - 1
    while i >= 0 and a[i] < chave:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = chave

print(a)