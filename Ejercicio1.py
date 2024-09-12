"""
   Escribir un programa que calcule cuántos litros de combustible consumió un automóvil. 
   El usuario ingresará una cantidad de litros de combustible cargados en la estación y una cantidad 
   de kilómetros recorridos, después, el programa calculará el consumo (km/lt) y se lo mostrará al usuario.

   FORMULA PARA CALCULAR CONSUMO DE COMBUSTIBLE
   (Kilómetros recorridos / litros de combustible cargados)
"""
import os

os.system('cls')

#Definir variables
litros_combusible:float = 0.0
kilometros_recorridos:float = 0.0
consumo_combustible:float = 0.0

#Ingresar los valores
litros_combusible:float = float(input("Ingrese cuantos litros cargo en su automóvil: "))
kilometros_recorridos:float = float(input("Ingrese cuantos kilometros recorrió: "))

#Calcular el consumo de combustible
consumo_combustible:float = kilometros_recorridos/litros_combusible

#Imprimir el consumo de combustible
print(f'Consumo de combustible: {consumo_combustible:.2f}(Km/Lt)')