a = int(input("Nota 1: "))
if a < 0 or a > 10:
    a = int(input("Nota errada. Digite a Nota 1 novamente: "))
b = int(input("Nota 2: "))
if b < 0 or b > 10:
    b = int(input("Nota errada. Digite a Nota 2 novamente: "))
c = int(input("Nota 3: "))
if c < 0 or c > 10:
    c = int(input("Nota errada. Digite a Nota 3 novamente: "))
d = int(input("Nota 4: "))
if d < 0 or d > 10:
    d = int(input("Nota errada. Digite a Nota 4 novamente: "))

media = (a+b+c+d)/4
print("Média: " + media)

# if a >= 0 and a <= 10 and b >= 0 and b<= 10 and c >= 0 and c <= 10 and d >= 0 and d <= 10:
#     print("Média: {:.2f}".format(media))
# else:
#     print("Alguma nota está errada")

