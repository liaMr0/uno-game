
from logica import jugar
from ranking import Ranking

  
def main():   
    print('''
    ------BIENVENIDO------
        1: Jugar
        2: Ranking
        3: Salir
    ''')

    opcion=input("Elija una opción: ")

    while opcion not in ["1", '2','3' ] :
        opcion=input("Elija una opción válida: ")
    
    if opcion=='1':
        jugar()
    elif opcion=='2':
        mostrar_ranking()
    else:
        return 
     
def mostrar_ranking():
    ranking=Ranking()
    print('''
------Ranking de jugadores-----
          ''')
    for i, jugador in enumerate(ranking.ordenar()):
        print(f"{i+1}- {jugador[0]}: {jugador[1]} puntos")
          
    print("""-------------------
1-Modificar nombre
2-Eliminar jugador
3-Eliminar todo          
4-Atrás
                """
            )
    
    
    opcion2=input("Elija una opción: ")
    while opcion2 not in ['1','2','3','4']:
        opcion2=input("Elija una opción válida: ")
    
    
    if opcion2=='1':
        nombre1=input("Entre el nombre del jugador que desea modificar: ")
        if ranking.combrobar_que_existe_jugador(nombre1):
            nombre2=input("Entre el nuevo nombre: ")
            ranking.modificar_jugador(nombre1,nombre2)
            print(f"El jugador {nombre1} ha sido modificado a {nombre2}")
            mostrar_ranking()
        else:
            print("No existe un jugador registrado con ese nombre")  
            mostrar_ranking() 
    elif opcion2=='2':
        nomb=input("Entre el nombre del jugador que desea eliminar: ")
        if ranking.combrobar_que_existe_jugador(nomb):
            ranking.eliminar_jugador(nomb)
            print(f"El jugador {nomb} ha sido eliminado.")
            mostrar_ranking()
        else:
            print("No existe un jugador registrado con ese nombre")  
            mostrar_ranking()  
    elif opcion2=='3': 
        ranking.eliminar_todo()  
        main()       
    elif opcion2=='4':
        main()


        
if __name__ == "__main__":
    main()