n = int(input('Digite um valor: '))
q = 0
q2 = 0
q3 = 0

q = n ** 2
q2 = n ** 3
q3 = n ** 0.5
print(q)
print(q2)
print(q3)

while True:
    if n <= 0:
        break
    if n > 0:
        n = int(input('Digite um valor: '))
        q = n ** 2
        q2 = n ** 3
        q3 = n ** 0.5
        print(q)
        print(q2)
        print(q3)




