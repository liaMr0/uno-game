from pickle import * #guarda y carga el objeto en binario
from jugador import *

class Ranking():
    def __init__(self) -> None:
        self.diccionario=self.cargar() #llamando al metodo cargar
    
    def crear_fichero(self):
        self.fichero=open('ranking.pickle','wb')#actualizar fichero
        dump(self.diccionario,self.fichero)#toma el diccionario y lo sobrescribe en el fichero
        self.fichero.close()
        
    def cargar(self):
        try:
            self.fichero=open('ranking.pickle','rb') #carga el fichero y el rb es para hacer la lectura binaria
            diccionario=load(self.fichero)
            self.fichero.close()
            return diccionario
        except FileNotFoundError:
            return {}
        
    def combrobar_que_existe_jugador(self,nombre1):
        if nombre1 in self.diccionario:
            return True
        return False
    
    def agregar_puntos(self,jugador):
        if jugador.nombre in self.diccionario:
            self.diccionario[jugador.nombre]+=jugador.puntos #acumula los puntos si el jugador esta guardado
            self.crear_fichero()
        else:
            self.diccionario[jugador.nombre]=jugador.puntos #si no esta el jugador registrado lo agrega al dic
            self.crear_fichero()
                    
    def ordenar(self):
        lista=list((self.diccionario.items()))   #[('Oslaniel', 260), ('Juan', 0), ('ffg', 60)] una lista de tuplas es lo q almacena
        lista.sort(key=lambda x: x[1],reverse=True)  #la expresion x[1] significa que va a tomar el segundo elemento cada tupla q son los puntos para ordenarlos de mayor a menor
        return lista
    
    def modificar_jugador(self,nombre1, nombre2):
        self.diccionario[nombre2]=self.diccionario.pop(nombre1)   #elimina el nombre anterior y crea una nueva clave con el nuevo nombre
        self.crear_fichero()
    
    
    def eliminar_jugador(self,nombre):
        self.diccionario.pop(nombre)
        self.crear_fichero()

    def eliminar_todo(self):
        self.diccionario={}
        self.crear_fichero()