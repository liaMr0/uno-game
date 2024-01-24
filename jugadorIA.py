import random

from jugador import Jugador


class JugadorIA(Jugador):
    def __init__(self,nombre):
        super().__init__(nombre) 
        
    def seleccionar_carta(self, carta_superior):
        for i, carta in enumerate(self.mano):
            if carta.color == carta_superior.color or carta.valor == carta_superior.valor or carta.valor in ['Comodín', 'Comodín +4']:
                return i 
        return -1

    def elegir_color(self):
        colores = ['Rojo', 'Verde', 'Azul', 'Amarillo']
        return random.choice(colores)
    
    def jugar(self,indice_carta):
        if len(self.mano)==2:
            print(f'{self.nombre} dice UNO!' )
        return self.mano.pop(indice_carta)
    
    def tomar(self, mazo):
        self.mano.append(mazo.tomar_carta())
