a = int(input("Nota 1: "))
while a > 10 or a < 0:
    a = int(input("Nota inválida. Entre com a nota correta: "))
b = int(input("Nota 2: "))
while b > 10 or b < 0:
    b = int(input("Nota inválida. Entre com a nota correta: "))
c = int(input("Nota 3: "))
while c > 10 or c < 0:
    c = int(input("Nota inválida. Entre com a nota correta: "))
d = int(input("Nota 4: "))
while d > 10 or d < 0:
    d = int(input("Nota inválida. Entre com a nota correta: "))

media = (a+b+c+d)/4
print("Média: " + str(media))