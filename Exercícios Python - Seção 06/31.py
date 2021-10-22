c = 0
razao = 0
s = 0

for i in range(1, 100, 2):
    c += 1
    razao = i / c
    s += razao
print(s)
