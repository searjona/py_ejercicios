# Lista vacia
lista_vacia: list = []

# Lista con elementos
motocicletas: list = ['Honda', 'Yamaha', 'Suzuki', 'Honda']

""" 
# Transformando los elementos de una lista en enteros con listas de compresion
values: list = input().split(' ')
print(values)
values_transform: list = [int(i) for i in values]
print(values_transform)

# Transforma los datos de una lista en entero y los guarda en variables con el metodo map()
n, m, p = map(int, values)
print(n)
"""

# Añade un elemento al final de una lista
motocicletas.append('Kawasaki')
print(motocicletas)

# Añade un elemento en la posicion que se escoja en una lista
motocicletas.insert(0, 'Husbarna')
print(motocicletas)

# Borrar un elemento de una lista (se puede guardar en una variable)
marca_moto: str = motocicletas.pop(1)
print(motocicletas)
print(marca_moto)

# Metodo pop() sin pasarle ningun parametro borra el ultimo elemento de la lista
motocicletas.pop()
print(motocicletas)

# Elimina un elemento de la lista pero este no se puede guardar en una variable
# Si este se repite elimina el primer elemento
cars: list = ['Mustand', 'Camaro', 'Audi R8', 'Mustand']
cars.remove('Mustand')
print(cars)

# Eliminar la lista completa
cars.clear()
print(cars)

# Borrar todos los elementos repetidos en una lista
fruits: list = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Orange']
while 'Orange' in fruits:
   fruits.remove('Orange')
print(fruits)

# Ordenar listas

