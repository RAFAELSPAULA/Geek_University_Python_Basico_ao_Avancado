def anagrama():
    a = str(input('Digite uma palavra: '))
    if a == a[::-1]:
        return True
    else:
        return False


print(anagrama())
