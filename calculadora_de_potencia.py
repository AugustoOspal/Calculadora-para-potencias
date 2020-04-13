# Version de prueba

from math import *

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


qi_grupal = []
qf_grupal = []
qc_grupal = []
qi_global = []
qc_global = []
qf_global = []
qi_individual = []
qf_individual = []
qc_individual = []
fp_individual = []
elementos_por_grupo = []
potencia_activa_grupal = []
potencia_activa_global = []
cantidad_por_elementos = []
potencia_aparente_grupal = []
potencia_aparente_global = []
potencia_activa_individual = []
potencia_aparente_individual = []
potencia_activa_total_individual = []

####CONFIGURACIONES######
decimales_de_redonde = 2
#########################

contador_de_pasadas = 0
sumador_de_qi_grupal = 0
sumador_de_potencia_activa_grupal = 0

cantidad_de_grupos = int(input("\nIngrese la cantidad de grupos totales: "))
cantidad_de_elementos = int(input("Ingrese la cantidad de elemtos totales: "))

fp_final = float(input("\nIngrese el fp final: "))
tg_final = float(input("Ingrese el tg final: "))

for grupo in range(cantidad_de_grupos):

    sumador_de_potencia_activa_elemental = 0
    sumador_de_qi_elemental = 0

    print("\n====================================================")
    elementos_por_grupo.append(int(input("Ingrese la cantidad de elementos de grupo " + str(grupo + 1) + ": ")))
    print("====================================================")

    for elemento in range(elementos_por_grupo[grupo]):

        print("\n----------------------------------------------------\nElemento " + str(elemento + 1) + "\n----------------------------------------------------")
        seleccion = int(input("\nIngrese que potencia quiere ingresar\n\nActiva = 1\nAparente = 2\nOpcion: "))

        if seleccion == 1:

            potencia_activa_individual.append(float(input("\nIngrese la potencia activa: ")))
            fp_individual.append(float(input("Ingrese el fp: ")))
            cantidad_por_elementos.append(int(input("Ingrese la cantidad del elemento: ")))

            potencia_activa_total_individual.append(potencia_activa_individual[contador_de_pasadas] * cantidad_por_elementos[contador_de_pasadas])
            potencia_aparente_individual.append(potencia_activa_total_individual[contador_de_pasadas] / fp_individual[contador_de_pasadas])
            qi_individual.append(sqrt(pow(potencia_aparente_individual[contador_de_pasadas], 2) - pow(potencia_activa_total_individual[contador_de_pasadas], 2)))
            qf_individual.append(potencia_activa_total_individual[contador_de_pasadas] * tg_final)
            qc_individual.append(qi_individual[contador_de_pasadas] - qf_individual[contador_de_pasadas])

        elif seleccion == 2:

            potencia_aparente_individual.append(float(input("\nIngrese la potencia aparente: ")))
            fp_individual.append(float(input("Ingrese el fp: ")))

            potencia_activa_total_individual.append(potencia_aparente_individual[contador_de_pasadas] * fp_individual[contador_de_pasadas])
            potencia_activa_individual.append(0)
            cantidad_por_elementos.append(0)
            qi_individual.append(sqrt(pow(potencia_aparente_individual[contador_de_pasadas], 2) - pow(potencia_activa_total_individual[contador_de_pasadas], 2)))
            qf_individual.append(potencia_activa_total_individual[contador_de_pasadas] * tg_final)
            qc_individual.append(qi_individual[contador_de_pasadas] - qf_individual[contador_de_pasadas])

        sumador_de_qi_elemental = sumador_de_qi_elemental + qi_individual[-1]
        sumador_de_potencia_activa_elemental = sumador_de_potencia_activa_elemental + potencia_activa_total_individual[-1]
        contador_de_pasadas = contador_de_pasadas + 1

    qi_grupal.append(sumador_de_qi_elemental)
    potencia_activa_grupal.append(sumador_de_potencia_activa_elemental)
    potencia_aparente_grupal.append(sqrt(pow(potencia_activa_grupal[-1], 2) + pow(qi_grupal[-1], 2)))
    qf_grupal.append(potencia_activa_grupal[-1] * tg_final)
    qc_grupal.append(qi_grupal[-1] - qf_grupal[-1])

for i in range(cantidad_de_grupos):
    sumador_de_qi_grupal = sumador_de_qi_grupal + qi_grupal[i]
    sumador_de_potencia_activa_grupal = sumador_de_potencia_activa_grupal + potencia_activa_grupal[i]

qi_global.append(sumador_de_qi_grupal)
potencia_activa_global.append(sumador_de_potencia_activa_grupal)
potencia_aparente_global.append(sqrt(pow(potencia_activa_global[-1], 2) + pow(qi_global[-1], 2)))
qf_global.append(potencia_activa_global[-1] * tg_final)
qc_global.append(qi_global[-1] - qf_global[-1])
                                                                                  
segunda_seleccion = int(input("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nIngrese la opcion de visualizacion\n\nMostrar los valores en el programa = 1\nCrear un archivo .txt con los datos = 2\n\nOpcion: "))

if segunda_seleccion == 1:

    print("====================================================\n\nResultado individuales\n")

    for elemento in range(cantidad_de_elementos):

        print("Elemento " + str(elemento + 1))

        print("\nWT = " + str(float(round(potencia_activa_total_individual[elemento], decimales_de_redonde))))
        print("VA = " + str(float(round(potencia_aparente_individual[elemento], decimales_de_redonde))))
        print("Qi = " + str(float(round(qi_individual[elemento], decimales_de_redonde))))
        print("Qf = " + str(float(round(qf_individual[elemento], decimales_de_redonde))))
        print("Qc = " + str(float(round(qc_individual[elemento], decimales_de_redonde))) + "\n")

    print("====================================================\n\nResultado grupales\n")

    for grupo in range(cantidad_de_grupos):

        print("Grupo " + str(grupo + 1))

        print("\nWT = " + str(float(round(potencia_activa_grupal[grupo], decimales_de_redonde))))
        print("VA = " + str(float(round(potencia_aparente_grupal[grupo], decimales_de_redonde))))
        print("Qi = " + str(float(round(qi_grupal[grupo], decimales_de_redonde))))
        print("Qf = " + str(float(round(qf_grupal[grupo], decimales_de_redonde))))
        print("Qc = " + str(float(round(qc_grupal[grupo], decimales_de_redonde))) + "\n")

    print("====================================================\n\nResultado globales\n")

    print("\nWT = " + str(float(round(potencia_activa_global[-1], decimales_de_redonde))))
    print("VA = " + str(float(round(potencia_aparente_global[-1], decimales_de_redonde))))
    print("Qi = " + str(float(round(qi_global[-1], decimales_de_redonde))))
    print("Qf = " + str(float(round(qf_global[-1], decimales_de_redonde))))
    print("Qc = " + str(float(round(qc_global[-1], decimales_de_redonde))) + "\n")

elif segunda_seleccion == 2:

    link = input("Ingrese la ruta de acceso donde quiere guardar el documento .txt: ")
    documento = input("\nIngrese como quiere que se llame el documento: ") + ".txt"
    escritura_file = open(link + documento, "w")

    escritura_file.write("========================\nResultados Individuales\n========================\n")
    contador_de_pasadas = 0

    for grupo in range(cantidad_de_grupos):

        escritura_file.write("\n------------------------\nGrupo " + str(grupo + 1) + "\n------------------------\n\n\n")

        for elemento in range(elementos_por_grupo[grupo]):
            escritura_file.write("Elemento " + str(elemento + 1))
            escritura_file.write("\nWT = " + str(float(round(potencia_activa_total_individual[contador_de_pasadas], decimales_de_redonde))))
            escritura_file.write("\nVA = " + str(float(round(potencia_aparente_individual[contador_de_pasadas], decimales_de_redonde))))
            escritura_file.write("\nQi = " + str(float(round(qi_individual[contador_de_pasadas], decimales_de_redonde))))
            escritura_file.write("\nQf = " + str(float(round(qf_individual[contador_de_pasadas], decimales_de_redonde))))
            escritura_file.write("\nQc = " + str(float(round(qc_individual[contador_de_pasadas], decimales_de_redonde))) + "\n\n")
            contador_de_pasadas = contador_de_pasadas + 1

    escritura_file.write("==========================\nResultados Grupales\n==========================\n")

    for grupo in range(cantidad_de_grupos):
        escritura_file.write("\n--------------------------\nGrupo " + str(grupo + 1) + "\n\n")
        escritura_file.write("\nWT = " + str(float(round(potencia_activa_grupal[grupo], decimales_de_redonde))))
        escritura_file.write("\nVA = " + str(float(round(potencia_aparente_grupal[grupo], decimales_de_redonde))))
        escritura_file.write("\nQi = " + str(float(round(qi_grupal[grupo], decimales_de_redonde))))
        escritura_file.write("\nQf = " + str(float(round(qf_global[-1], decimales_de_redonde))))
        escritura_file.write("\nQc = " + str(float(round(qc_global[-1], decimales_de_redonde))) + "\n\n")

    escritura_file.write("==========================\nResultados Globales\n==========================\n\n")

    escritura_file.write("\nWT = " + str(float(round(potencia_activa_global[-1], decimales_de_redonde))))
    escritura_file.write("\nVA = " + str(float(round(potencia_aparente_global[-1], decimales_de_redonde))))
    escritura_file.write("\nQi = " + str(float(round(qi_global[-1], decimales_de_redonde))))
    escritura_file.write("\nQf = " + str(float(round(qf_global[-1], decimales_de_redonde))))
    escritura_file.write("\nQc = " + str(float(round(qc_global[-1], decimales_de_redonde))) + "\n")

    escritura_file.close()
    
mail = input("Desea que le enviemos un mail con los resultados:\n1 = si\n2 = no\n>>> ")
while not mail.isdigit() or int(mail) > 2 or int(mail) < 1:
    mail = input("Desea que le enviemos un mail con los resultados:\n1 = si\n2 = no\n>>> ")

destinatario = input("\nIngrese su mail:\n>>> ")

if int(mail) == 1:

    import smtplib

    mensage = "Te la creiste we XD"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('AugustoOspal@gmail.com', 'Augustofelipe24')
    server.sendmail('AugustoOspal@gmail.com', destinatario, mensage)

    server.quit()

    print("El mail ah sido exitosamente")