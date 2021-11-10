"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursos pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

# seek() - > A função seek() é utilizada para movimentação do cursor pelo arquivo. ele recebe um parâmetro que indica
# onde queremos colocar o cursor.
# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)

print(arquivo.read())


arquivo.seek(22)

print(arquivo.read())

# readline () -> Função que lê o arquivo linha a linha (readline -> lê linha)

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))



# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: quando abrimos um arquivo com a função open() é criada conexão entre o arquivo no disco do computador e nosso
programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para
isso utilizamos a função close()

# Abrir o arquivo
arquivo = open('texto.txt')

# Trabalhar o arquivo.
print(arquivo.read())

# Verificar se o arquivo está aberto ou fechado

print(arquivo.closed)

# Fechar o arquivo
arquivo.close()

# print(arquivo.read()) - > Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError.

dentro do read podemos limitar quantidade de caracteres
"""

