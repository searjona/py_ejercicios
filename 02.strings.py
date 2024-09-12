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

# Colocar un string en minusculas o mayusculas
cadena_minuscula: str = "Esto ES UN Texto QUE saldrA en MINÚSCULAS"
print(cadena_minuscula.lower())
cadena_mayuscula: str = "este saldra convertido en mayúsculas"
print(cadena_mayuscula.upper())

# Comprobar si un string tiene prefijos y sufijos
url: str = "www.r2d2.com"
prefijo: bool = url.startswith('www')
sufijo: bool = url.endswith('.com')
print(prefijo)
print(sufijo)

# Encontrar la posicion del primer carácter en la primera posicion de un string, si no lo encuentra devuelve -1
indice: int = url.find("2")
print(indice)