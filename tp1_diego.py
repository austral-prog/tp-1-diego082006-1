# Ejercicio 1
i1 = 2
i2 = 4
i3 = i1 + i2
print("valor de i1")
print(i1)
print("valor de i2")
print(i2)
print("valor de i3")
print(i3)
print("valor total")
print(i1 + i2 + i3)

s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3)

x = "Naranja"
y = z = ", Naranja"
print(x + y + z)

z1 = i3 / i2
print(z1)
z2 = i3 % i2
print(z2)
f1 = 0.5
f2 = 10
f3 = f1 + f2
i3 = int(f3)
print("entero de i3:")
print(i3)
print("variable de f3:")
print(f3)
f2 += i1
print("el valor de i1 es igual a:")
print(f2)
print("más")
print(f1)
print("es:")
print(f2 + f1)

#Ejercicio 2
def math():
    a = 57
    b = 7
    Suma = a + b
    print(Suma)
    Diferencia = a - b
    print(Diferencia)
    Producto = a * b
    print(Producto)
    Promedio = (a + b) / 2
    print(Promedio)
    Cociente_entero = a // b
    print(Cociente_entero)
    Resto = a % b
    print(Resto)
    Division_real = a / b
    print(Division_real)

math()