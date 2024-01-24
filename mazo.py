import random
from carta import Carta
from jugador import Jugador


class Mazo:
    def __init__(self):
        self.cartas = []
        self.construir()
      

    def construir(self):
        colores = ['Rojo', 'Verde', 'Azul', 'Amarillo']
        valores = list(range(0, 10)) + ['Salta', 'Reversa', '+2', 'Comodín', 'Comodín +4']
        for color in colores:
            for valor in valores:
                self.cartas.append(Carta(color, valor))

    def barajar(self):
        random.shuffle(self.cartas)

    def tomar_carta(self):
        return self.cartas.pop()#retorna la carta y la elimina del mazo 

    def reabastecer_mazo(self,pila_descarte):
        ultima_carta=pila_descarte.pop() #elimina la ultima carta de la lista y la retorna
        self.cartas=pila_descarte[:]
        pila_descarte.clear()
        pila_descarte.append(ultima_carta)
        self.barajar()
