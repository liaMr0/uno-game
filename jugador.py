class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.puntos=0
        self.dijo_uno=False
        
        
    def tomar(self, mazo):
        self.mano.append(mazo.tomar_carta())
        if len(self.mano)>=2 and self.dijo_uno:
            self.dijo_uno=False
            
    def jugar(self, indice_carta):
        if len(self.mano)==2 and self.dijo_uno ==False:    
            return False
        return self.mano.pop(indice_carta)

    def mostrar_mano(self):
        print(f'{self.nombre} tiene:')
        for i, carta in enumerate(self.mano):
            print(f'{i}: {carta}')#la i muestra el indice (numeros de la izquierda) y muestra las cartas a la derecha llamando al metodo str y el repr

    def carta_valida(self, carta_superior):
        for carta in self.mano:
            if carta.color == carta_superior.color or carta.valor == carta_superior.valor or carta.valor in ['Comodín', 'Comodín +4']:
                return True
        return False

    def elegir_color(self):
        colores = ['Rojo', 'Verde', 'Azul', 'Amarillo']
        color_elegido = input('Has jugado un comodín. Elige un color (Rojo, Verde, Azul, Amarillo): ')
        while color_elegido not in colores:
            print('Color inválido. Por favor, elige un color válido (Rojo, Verde, Azul, Amarillo).')
            color_elegido = input('Elige un color: ')
        return color_elegido

    def agregar_puntos(self,puntos):
        self.puntos+=puntos
        
    def decir_uno(self):
        if len(self.mano) == 2:
            self.dijo_uno = True  # Actualizamos el estado dijo_uno a True al anunciar "UNO"
            return True
        return False
