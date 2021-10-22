from itertools import product

palindromes = (i*j for i, j in product(range(100, 1000), repeat=2) if str(i*j) == str(i*j)[::-1])

print("O maior palíndromo encontrado foi", max(palindromes))