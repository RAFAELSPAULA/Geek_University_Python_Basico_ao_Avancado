n = int(input('Digite um valor: '))

s = 0
s1 = 0
s2 = 0

for i in range(1, n+1):
    s += i
print(s)

for i in range(1, n+1):
    s1 = s1 + (2 * i - 1)
print(s1)

for i in range(1, n+1):
    if i % 2 == 1:
        s2 = s2 + (2 * i - 1)
print(s2)

