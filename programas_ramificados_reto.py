nombre_1 = input("Hola como es tu nombre?\n")
edad_1 = int(input('Cuantos años tenes ' + nombre_1 + '?\n'))
nombre_2 = input('y tu amigo ¿como se llamas?\n')
edad_2 = int(input('y cuantos años tiene ' + nombre_2 + '?\n'))


if edad_1 > edad_2:
    print(nombre_1 + " Tiene mas años que " + nombre_2 )
elif edad_1 < edad_2:
    print(nombre_2 + " Tiene mas años que " + nombre_1 )
else:
    print(nombre_1 + " y " + nombre_2 + " tiene la misma edad.")