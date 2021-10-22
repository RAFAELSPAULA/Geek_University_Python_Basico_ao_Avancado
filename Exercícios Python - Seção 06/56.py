def testaPrimo(num):
    if num == 1:
        return False
    for d in range(2, int(num / 2) + 1):
        if num % d == 0:
            return False
    else:
        return True


soma = 0

for i in range(1, 10):
    if testaPrimo(i):
        soma += i

else:
    print(soma)
