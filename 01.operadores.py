# OPERADORES DE PERTENENCIA
in_operation: bool = "hola" in "hola mundo"
not_operation: bool = "hola" not in "hola mundo"
print(in_operation)
print(not_operation)

# OPERADORES DE IDENTIDAD
x = 1
y = x
nulo = None

is_operation: bool = x is y
print(is_operation)

is_null = nulo is None or nulo is not None
print(is_null)
