class Carta:
    def __init__(self, color, valor):
        self.color = color
        self.valor = valor

    def __str__(self):
        return f'{self.color} {self.valor}'
    
    def __repr__(self) -> str:#es un metodo especial para mostrar una representacion legible del objeto
        return str(self)