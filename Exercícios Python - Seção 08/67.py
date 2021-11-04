import sys
str = ""
while True:
    c = sys.stdin.read(1) # reads one byte at a time, similar to getchar()
    if c == ' ':
        break
    str += c
print(str)