import math
from helpers import *

print("\n24/12/2019")
print("E-Mail: AugustoOspal@icloud.com\n")

print("   /| |   | |'''  |   | |'''  '''|''' |'''|")
print("  / | |   | |  __ |   | |___     |    |   |")
print(" /__| |   | |   | |   |     |    |    |   |")
print("/   | |___| |___| |___|  ___|    |    |___|")
print("                                           ")
print("|'''| |'''  |'''|    /| |    ")
print("|   | |___  | __|   / | |    ")
print("|   |     | |      /__| |    ")
print("|___|  ___| |     /   | |____")

####CONFIGURACIONES######
decimales_de_redonde = 2
#########################

ts_list = []
elements = []
temp_elements = []

separador0 = "----------------------------------------------------"
separador1 = "===================================================="

fp_final = float(input("\n\nIngrese el cos 𝜑 final: "))
tg_final = float(input("Ingrese el tg 𝜑 final: "))

num_elements = 0
num_tablero = int(input("\nIngrese la cantidad de tableros secundarios: ")) 

print("\nA acontinuacion va a introducir los datos de cada elemento")
print("PD: Si no tiene ese dato ingrese 0")

for tablero_secundario in range(num_tablero):
    print(f"\n{separador1}\nGrupo {tablero_secundario + 1}\n{separador1}")
    num_elements = int(input(f"Ingrese la cantidad de elementos del grupo {tablero_secundario + 1}: "))

    for elemento in range(num_elements):
        print(f"\n{separador0}\nElemento {elemento + 1}\n{separador0}") 
        element = Element()
        element.ask_for_data()
        element.solve_element(tg_final)
        temp_elements.append(element)

    ts = Element()
    ts.solve_ts(temp_elements, tg_final, f"Ts {tablero_secundario + 1}")
    update_elements(temp_elements, elements)
    ts_list.append(ts)

tp = Element()
tp.solve_ts(ts_list, tg_final, "Tp")
show_all_data(elements, ts_list, tp)