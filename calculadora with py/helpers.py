"""En helpers.py se van a almaceras las funciones y la clase de Element."""
import math

class Element:
    """Esta clase almacena las caracteristicas de cada elemento, tablero secundario y tablero principal 
    de la instalacion. La opcion de verificacion todavia no esta implementada, pero la dejo preparada."""

    def __init__(self, name='', quantity=0, P=0, fp=0, S=0, Qi=0, Qf=0, Qc=0, verif=0):
        self.name = name
        self.P = P
        self.fp = fp
        self.S = S
        self.Qi = Qi
        self.Qf = Qf
        self.Qc = Qc
        self.verif = verif

    def ask_for_data(self):
        """Rellena los atributos con los valores pedidos."""

        self.name = input("\nName: ").lower()
        self.P = float(input("P: "))
        self.S = float(input("VA: "))
        self.fp = float(input("FP: "))
        self.quantity = int(input("Quantity: "))

    def show_data(self, decimal_number):
        """Muestra todos los atributos del objeto."""

        print(f"\nName: {self.name}")
        print(f"P: {round(self.P, decimal_number)}")
        print(f"VA: {round(self.S, decimal_number)}")
        print(f"FP: {round(self.fp, decimal_number)}")
        print(f"Qi: {round(self.Qi, decimal_number)}")
        print(f"Qf: {round(self.Qf, decimal_number)}")
        print(f"Qc: {round(self.Qc, decimal_number)}")
        print(f"Quanity: {self.quantity}")

    def solve_element(self, tg):
        """Con los valores de los atributos ingresados con ask_for_data se resuelven los atributos faltantes del elemento."""

        if self.P == 0:
            self.P = (self.S * self.fp) * self.quantity

        elif self.S == 0:
            self.P = self.P * self.quantity
            self.S = self.P / self.fp

        self.Qi = math.sqrt(self.S ** 2 - self.P ** 2)
        self.Qf = self.P * tg
        self.Qc = self.Qi - self.Qf
        self.fp = self.P / self.S

    def solve_ts(self, elements, tg, name):
        """Este metodo calcula los valores de un tablero secundario con los valores de los elementos del tablero.
        El primer argumento conciste en la lista de elementos de donde vamos a sacar los elementos, y el segundo
        conciste en la posicion que tenga el tablero secundario en una lista de tableros secundarios si es que la hay.
        Si el segundo paramtero no se rellena, por defaul sera None, por lo que se tendra en cuanta que se quiere un solo tablero."""

        for element in elements:
            self.P += element.P
            self.Qi += element.Qi

        self.name = name
        self.quantity = 1
        self.S = math.sqrt(self.P ** 2 + self.Qi ** 2) 
        self.Qf = self.P * tg
        self.Qc = self.Qi - self.Qf
        self.fp = self.P / self.S

def update_elements(temp_elements, elements):
    """Guarda todos los elementos en la lista elements y borra los de temp_elements."""

    for element in temp_elements:
        elements.append(element)
        
    del temp_elements[:len(temp_elements)]

def show_all_data(elements, secondary_board, master_board, decimal_number=2):
    """Muetra todos los datos de los elementos, tableros secundarios y tablero principal."""

    for element in elements:
        element.show_data(decimal_number)

    for ts in secondary_board:
        ts.show_data(decimal_number)

    master_board.show_data(decimal_number)
    