# a = 0
# b = 1
# c = 0

# while a <= 10:
#     c = a + b
#     print(a)
#     a = b
#     b = c

# secuencia = [0, 1]
# limite = 100

# while secuencia[-1] < limite:
#   secuencia.append(secuencia [-1] + secuencia [-2])

#   print(secuencia)

a = 0
b = 1

while a <= 100:
    print(a)
    (a,b) = (b, a+b )