# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
ggo_online = str(input('Ingrese la primera palabra:\n'))

sao_online = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if ggo_online > sao_online:
    print('{} es mayor que {}'.format(ggo_online, sao_online))
else:
    print('{} es mayor que {}'.format(sao_online, ggo_online))

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(ggo_online) > len(sao_online):
    print('{} tiene mas caracteres que {}'.format(ggo_online, sao_online))
else:
    print('{} tiene mas caracteres que {}'.format(sao_online, ggo_online))

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if len(ggo_online[0]) > len(sao_online[0]):
    print('la primera letra de {} es mayor a la primera letra de {}'.format(ggo_online, sao_online))
else:
    print('la primera letra de {} es mayor a la primera letra de {}'.format(sao_online, ggo_online))

copia_ggo_online = ggo_online  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_ggo_online == ggo_online:
    print('ggo_online es igual a copia_ggo_online')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if not(sao_online == copia_ggo_online):
    print('sao_online es distinto a copia_ggo_online')

print('gracias')
