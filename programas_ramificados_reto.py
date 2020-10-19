nombre_1 = input("Hola como es tu nombre?")
edad_1 = int(input('Cuantos años tenes?' + nombre_1))
nombre_2 = input('y tu amigo ¿como se llamas?')
edad_2 = int(input('y cuantos años tiene?' + nombre_2))


if edad_1 > edad_2:
    print(nombre_1 + " Tiene mas años que " + nombre_2 )
elif edad_1 < edad_2:
    print(nombre_2 + " Tiene mas años que " + nombre_1 )
else:
    print(nombre_1 + " y " + nombre_2 + " tiene la misma edad.")