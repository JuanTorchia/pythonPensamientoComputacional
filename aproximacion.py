objetivo = int(input('Escogue un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

4
if abs(respuesta**2 -objetivo) >= epsilon:
    print(f'No se econtre la raiz cuadra {objetivo}')
else:
    print(f'la raiz cuadra de {objetivo} es {respuesta}')