"""En helpers.py se van a almaceras las funciones y la clase de Element."""
import math

class Element:
    """Esta clase almacena las caracteristicas de cada elemento, tablero secundario y tablero principal de la instalacion."""
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

        print(f"Name: {self.name}")
        print(f"P: {round(self.P, decimal_number)}")
        print(f"VA: {round(self.S, decimal_number)}")
        print(f"FP: {round(self.fp, decimal_number)}")
        print(f"Quanity: {self.quantity}")

        print(f"Qi: {round(self.Qi, decimal_number)}")
        print(f"Qf: {round(self.Qf, decimal_number)}")
        print(f"Qc: {round(self.Qc, decimal_number)}")

    def solve_element(self, tg):
        """Con los valores de los atributos ingresados con ask_for_data se resuelven los atributos faltantes del elemento."""

        if self.P == 0:
            self.P = self.S * self.fp

        elif self.S == 0:
            self.S = self.P / self.fp

        self.Qi = math.sqrt(self.S ** 2 - self.P ** 2)
        self.Qf = self.P * tg
        self.Qc = self.Qi - self.Qf