# Imprime todos metodos que se pueden usar con un string
#print(dir(''))

# Longitud de un string --> len()
saludo: str = "Este es un curso de python"
print(len(saludo))

# Quitar espacios en blanco --> strip()
cadena_espacios: str = "   Texto con espacios  "
print(cadena_espacios.strip())

# Reemplazar partes de un string por otro
cadena_reemplazo: str = "ESTOPEESPEUNPEMENSAJEPECIFRADO"
print(cadena_reemplazo.replace('PE', ' '))

# Colocar un string en minusculas
cadena_minuscula: str = "Esto ES UN Texto QUE saldrA en MINÚSCULAS"
print(cadena_minuscula.lower())