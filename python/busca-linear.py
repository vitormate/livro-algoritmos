a = [31, 41, 59, 26, 41, 58]

v = 31

for index, num in enumerate(a):
    if v == num:
        print(index)
        break
else:
    print(None)