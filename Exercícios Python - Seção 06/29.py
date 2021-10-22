from math import factorial

s = [0]

for n in range(2, 11, 2):
    s.append(1 / factorial(n))
print(f'A soma da sequência é {sum(s):.2f}')
