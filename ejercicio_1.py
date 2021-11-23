# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos

operacion_aincrad = int(input('Ingrese el primer número:\n'))

operacion_heathcliff = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if operacion_aincrad > operacion_heathcliff:
    print('operacion_aincrad =', operacion_aincrad,'es mayor a operacion_heathcliff =', operacion_heathcliff)
else:
    print('operacion_heatcliff =', operacion_heathcliff, 'es mayor a operacion_aincrad =', operacion_aincrad)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if operacion_aincrad > 0:
    print('operacion_aincrad es positivo')
elif operacion_aincrad < 0:
    print('operacion_aincrad es negativo')
else:
    print('operacion_aincrad es 0')

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if operacion_aincrad < 100 and operacion_aincrad > 0:
    print('operacion_aincrad es menor a 100 y mayor a 0')

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if operacion_aincrad < 10:
    print('operacion_aincrad es menor a 10')
elif operacion_aincrad == 10:
    print('operacion_aincrad es igual a 10')
else:
    print('operacion_aincrad es mayor a 10')
if operacion_heathcliff > -2:
    print('operacion_heathcliff es mayor a -2') 
else:
    print('operacion_heathcliff es menor a -2')

print('gracias')