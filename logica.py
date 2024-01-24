
from jugador import Jugador #izquierda fichero derecha clase 
from jugadorIA import JugadorIA
from mazo import Mazo
from ranking import Ranking

 
def jugar():
    ranking=Ranking() 
    mazo = Mazo()
    mazo.barajar()
    
    jugadores = []
    jugadores_que_abandonaron=[]
    
    num_jugadores=input('Introduce el número de jugadores (2-4): ') #esto es para no tener que validar y hacer los try except
    while num_jugadores not in ["2","3","4"]:
        num_jugadores = input('Número inválido de jugadores. Por favor, introduce un número entre (2-4): ')
        

    num_jugadores=int(num_jugadores)
    incluir_IA=input("Desea jugar contra la computadora? (s/n): ")
    if incluir_IA.lower()=='s':
        if num_jugadores==2:
            jugadores.append(JugadorIA("IA"))#agrego una instancia de la ia
            num_jugadores-=1
        elif num_jugadores>=3:
            while True:
                try:
                    cant_IA=int(input("Con cuantas IA desea jugar?: "))
                    while True:
                        if cant_IA>= num_jugadores:
                            
                            cant_IA=int(input("Las IA no pueden exceder ni ser iguales a la cantidad de jugadores. Con cuantas desea jugar?: ")) 
                            continue

                        else:
                            num_jugadores-=cant_IA
                            for i in range(cant_IA):
                                jugadores.append(JugadorIA(f'IA {i+1}'))  #cadena formateada para diferenciar las ia, estamos creando un objeto de la clase Jugador ia y agregandolo a la lista de jugadores
                            break                             
                    break       
                except ValueError:
                    print("Se espera un numero")
                    continue
       
    for i in range(num_jugadores):  
        nombre = input(f'Introduce el nombre del jugador {i+1}: ')
        jugadores.append(Jugador(nombre))


 
    # Repartir 7 cartas a cada jugador
    for _ in range(7): #variable anonima 
        for jugador in jugadores:
            jugador.tomar(mazo)

    # La primera carta del mazo de descarte
    carta_inicial = mazo.tomar_carta()#esta tomando esa carta y la elimina del mazo
    while carta_inicial.valor in ['Salta', 'Reversa', '+2', 'Comodín', 'Comodín +4']:  # Asegurarse de que la carta inicial no sea una carta especial
        mazo.cartas.insert(0, carta_inicial)  # Devolver la carta especial al mazo
        carta_inicial = mazo.tomar_carta()  # Tomar una nueva carta inicial
    pila_descarte = [carta_inicial]
   
    #toma la ultima posicion de la lista y la muestra 
    print(f'''
          ------------------------------
          La carta inicial es: {pila_descarte[-1]} 
          ------------------------------''')
    
    # Jugar hasta que un jugador se quede sin cartas
    turno = 0
   
    while all(jugador.mano for jugador in jugadores):#el all lo que hace es tomar iterables y si algun elemtodel iterable es falso retrona falso
        try:   
            jugador_actual = jugadores[turno % len(jugadores)]
            if isinstance(jugador_actual, JugadorIA): #isintance funcion para saber si el jugador es una instancia de la ia(para ver si es el turno de la ia ya que si es una ia pasa el codigo de abajo)
                print(jugador_actual.mano)
                indice_carta = jugador_actual.seleccionar_carta(pila_descarte[-1])#es para validar si en su mano tiene alguna carta que pueda jugar
                if indice_carta==-1 :
                    jugador_actual.tomar(mazo)
                    print(f'La {jugador_actual.nombre} ha tomado una carta del mazo.')
                else:
                    carta_jugada = jugador_actual.jugar(indice_carta)
                    if carta_jugada.valor in ['Comodín', 'Comodín +4']:
                        nuevo_color = jugador_actual.elegir_color()#hay una diferencia con respecto a cuando es un jugador ya que elige el color de forma aleatotia pyjugadorIA
                        carta_jugada.color = nuevo_color#accede al atributo color de esa carta jugada y la modifica
                        if carta_jugada.valor == 'Comodín +4':
                            siguiente_jugador = jugadores[(turno + 1) % len(jugadores)]#jugadores es la lista de jugadores
                            print(f"El siguiente jugador es: {siguiente_jugador.nombre}, roba 4 cartas y se omite su turno ")
                            for _ in range(4):
                                siguiente_jugador.tomar(mazo)                             
                            turno += 1  # Salta el turno del siguiente jugador
                        
                    elif carta_jugada.valor == 'Salta':
                        turno += 1  # Salta el turno del siguiente jugador
                    elif carta_jugada.valor == 'Reversa':
                        jugadores.reverse()  # Invierte el orden de los turnos
                    elif carta_jugada.valor == '+2':
                        siguiente_jugador = jugadores[(turno + 1) % len(jugadores)]
                        print(f"El siguiente jugador es: {siguiente_jugador.nombre}, roba 2 cartas. ")
                        for _ in range(2):  # El siguiente jugador toma 2 cartas
                            siguiente_jugador.tomar(mazo)
                    pila_descarte.append(carta_jugada)
                    
                    print(f'''
                        -------------------------
                        {jugador_actual.nombre} jugó {carta_jugada}
                        -------------------------''')
                turno+=1                  
             
            else:       
                print(jugador_actual.mano)   
                jugador_actual.mostrar_mano()#muestra la mano del jugador
            
                accion = input(f'{jugador_actual.nombre}, elige una carta para jugar o escribe "UNO" o "abandonar" para abandonar el juego: ')
          
                if accion.lower() == 'abandonar':
                    print(f'{jugador_actual.nombre} ha abandonado el juego.')            
                    jugadores_que_abandonaron.append(jugador_actual)
                    jugadores.remove(jugador_actual)
                    if len(jugadores) == 1:
                        break
                    continue
                elif accion.lower()=='uno':
                    if jugador_actual.decir_uno():
                        print(f"{jugador_actual.nombre} dice: ¡UNO!")
                        continue
                    else:
                        print(f'Penalización, {jugador_actual.nombre} debe tomar una carta del mazo.') 
                        jugador_actual.tomar(mazo)
                        turno+=1
                        continue
                try:
                    indice_carta = int(accion)
                    carta_jugada = jugador_actual.jugar(indice_carta)
                except (IndexError,ValueError): 
                    print("Acción inválida. Por favor, elige una carta válida de tu mano o toma una carta del mazo.")
                    continue
                if carta_jugada==False:
                    print(f"Penalización, {jugador_actual.nombre} no dijo UNO. Debe tomar una carta del mazo.")
                    jugador_actual.tomar(mazo)
                    turno+=1
                    continue                
                # Verificar si la carta jugada es válida
                carta_superior = pila_descarte[-1]
                if carta_jugada.color == carta_superior.color or carta_jugada.valor == carta_superior.valor or carta_jugada.valor in ['Comodín', 'Comodín +4']:
                    if carta_jugada.valor in ['Comodín', 'Comodín +4']:
                        nuevo_color = jugador_actual.elegir_color()
                        carta_jugada.color = nuevo_color
                        if carta_jugada.valor == 'Comodín +4':
                            siguiente_jugador = jugadores[(turno + 1) % len(jugadores)]
                            print(f"El siguiente jugador es: {siguiente_jugador.nombre}, roba 4 cartas y se omite su turno ")
                            for _ in range(4):  # El siguiente jugador toma 4 cartas
                                siguiente_jugador.tomar(mazo)
                            turno += 1  # Salta el turno del siguiente jugador
                        
                    elif carta_jugada.valor == 'Salta':
                        turno += 1  # Salta el turno del siguiente jugador
                    elif carta_jugada.valor == 'Reversa':
                        jugadores.reverse()  # Invierte el orden de los turnos
                    elif carta_jugada.valor == '+2':
                        siguiente_jugador = jugadores[(turno + 1) % len(jugadores)]
                        print(f"El siguiente jugador es: {siguiente_jugador.nombre}, roba 2 cartas. ")
                        for _ in range(2):  # El siguiente jugador toma 2 cartas
                            siguiente_jugador.tomar(mazo)
                    pila_descarte.append(carta_jugada)
                    

                    # jugadores[0].mano=[]  # Esta linea no entra en el juego, es para llegar al final rapido
                    print(f'''
                        -------------------------
                        {jugador_actual.nombre} jugó {carta_jugada}
                        -------------------------''')
            
                else:
                    print('Carta inválida. Debes tomar una carta del mazo.')
                    jugador_actual.tomar(mazo)
                    jugador_actual.mano.insert(indice_carta, carta_jugada)  # Devuelve la carta a la mano del jugador
 
               
                turno += 1
        except IndexError:
            mazo.reabastecer_mazo(pila_descarte)
 
    from main import main # importacion tardia para evitar el error de importacion ciclica

    try:
        if jugadores:
            ganador = next(jugador for jugador in jugadores if not jugador.mano) #si no hay jugadores sin cartas lanza una excepcion
            jugadores.remove(ganador)
            jugadores.extend(jugadores_que_abandonaron)
            print("Las cartas de los perdedores son las siguientes...")
            print([jugador.mano for jugador in jugadores])
            puntos= sumar_puntos(jugadores) 
            ganador.agregar_puntos(puntos)
            print(f'¡{ganador.nombre} ha ganado con {puntos} puntos!')
            ranking.agregar_puntos(ganador)
            main()
            
    except StopIteration:
        puntos=sumar_puntos(jugadores_que_abandonaron)
        jugadores[0].agregar_puntos(puntos)
        ranking.agregar_puntos(jugadores[0])
        print("Las cartas de los perdedores son las siguientes...")
        print([jugador.mano for jugador in jugadores_que_abandonaron])
        print(f'¡Ha ganado {jugadores[0].nombre} con {puntos} puntos!')
        main()


def sumar_puntos(jugadores):
    puntos=0
    for jugador in jugadores:
        for carta in jugador.mano:
            if carta.valor in ['Comodín', 'Comodín +4']:
                puntos+=50
            elif carta.valor in ['Salta','Reversa', '+2']:
                puntos+=20
    return puntos


