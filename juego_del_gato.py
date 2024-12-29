#Importamos la libreria random
from random import * 

#Definimos variables
posicion = [1,2,3,4,5,6,7,8,9] 
contador = 0 
bot = False
jugador2 = False
temporizador = 0

#definiendo la funcion victoria
def victoria():
    if posicion[0] == "O" and posicion[1] == "O" and posicion[2] == "O" or posicion[0] == "X" and posicion[1] == "X" and posicion[2] == "X":
        if posicion[0] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()
    elif posicion[3] == "O" and posicion[4] == "O" and posicion[5] == "O" or posicion[3] == "X" and posicion[4] == "X" and posicion[5] == "X":
        if posicion[3] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()      
    elif posicion[6] == "O" and posicion[7] == "O" and posicion[8] == "O" or posicion[6] == "X" and posicion[7] == "X" and posicion[8] == "X":
        if posicion[6] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()    
    elif posicion[0] == "O" and posicion[3] == "O" and posicion[6] == "O" or posicion[0] == "X" and posicion[3] == "X" and posicion[6] == "X":
        if posicion[0] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()   
    elif posicion[1] == "O" and posicion[4] == "O" and posicion[7] == "O" or posicion[1] == "X" and posicion[4] == "X" and posicion[7] == "X":
        if posicion[1] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()          
    elif posicion[2] == "O" and posicion[5] == "O" and posicion[8] == "O" or posicion[2] == "X" and posicion[5] == "X" and posicion[8] == "X":
        if posicion[2] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()  
    elif posicion[0] == "O" and posicion[4] == "O" and posicion[8] == "O" or posicion[0] == "X" and posicion[4] == "X" and posicion[8] == "X":
        if posicion[0] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()
    elif posicion[2] == "O" and posicion[4] == "O" and posicion[6] == "O" or posicion[2] == "X" and posicion[4] == "X" and posicion[6] == "X":
        if posicion[2] == marca1:
            print("Felicidades! el ganador fue el jugador 1!!")
            exit()
        else:
            print("Felicidades! el ganador fue el bot!!")
            exit()
    elif type(posicion[0]) == str and type(posicion[1]) == str and type(posicion[2]) == str and type(posicion[3]) == str and type(posicion[4]) == str and type(posicion[5]) == str and type(posicion[6]) == str and type(posicion[7]) == str and type(posicion[8]) == str:
           print("Esto ha sido un empate! GGs! Esperamos volver a verte jugar!")  
           exit()

def tablero(contador):
        for i in range(3):
            print("-" * 19)
            print("|", f" {posicion[contador]} ","|", f" {posicion[contador + 1]} ","|", f" {posicion[contador + 2]} ","|")
            contador += 3
            print("-" * 19)
            i += 1    
        contador = 0    


#Bienvenida al usuario
print("bienvenido al juego del gato!")
respuesta = input("listo para comenzar? (escribe si o no) ").lower().replace(" ", "")
#Preguntamos al usuario si esta listo
if respuesta == "si":
    print("Perfecto!, Comenzemos el juego")
else:
    print("Vuelve Cuando estes listo!")
    exit()

#preguntamos al usuario si jugara solo o multijugador
while 0 == 0:
    try:
        cantidad_jugadores = int(round(float(input("Quieres jugar de 1 o 2 personas?: "))))
        if cantidad_jugadores > 2 or cantidad_jugadores < 1:
            print("Porfavor escribe 1 o 2, dependiendo de las personas que jugaran")
        else: 
            break
    except:
        print("El valor que introduciste no fue un numero")  

if cantidad_jugadores == 1:
    bot = True
else:
    jugador2 = True    




if bot == True:
    
    while 0 == 0:
       try:
         marca1 = input("Elige tu marca (X o O): ").capitalize().replace(" ", "")
         marca2 = 0
         #verificamos que el usuario haya elegido X o O
         if marca1 == "X" :
             marca2 = "O"
             break
         elif marca1 == "O" :
             marca2 = "X"
             break
         else: 
             print("Escribe X o O")   
                                                    
       except:
         print("El valor que introduciste no fue X o O")  
         
    
    while temporizador != 2.5:

                
        #Imprimimos tablero con sus posiciones
        tablero(contador)
        victoria() 
        print('Turno del jugador 1...')
        while 0 == 0:
               #preguntamos al usuario que posicion quiere    
               try:
                 movimiento = int(round(float(input("En que posicion pondras tu ficha? (Elige un numero del 1 al 9): "))))
                 movimiento -= 1
                 #verificamos que el usuario haya elegido un numero del 1 al 9
                 if posicion[movimiento] == "O" or posicion[movimiento] == "X":
                     print("Esa casilla, ya esta ocupada elige otra")                 
                 
                 elif movimiento > 8 or movimiento < 0:
                    print("Tiene que ser un numero del 1 al 9")
                     
                 else:
                    posicion[movimiento] = marca1  
                    break 
                   
               except:
                 print("El valor que introduciste no fue un numero")
        tablero(contador)         
        victoria()                                          
        print('Turno del bot...')

        
        while 0 == 0:   
                movimiento_bot = randrange(0,9) 
                if posicion[movimiento_bot] == "O" or posicion[movimiento_bot] == "X":
                    movimiento_bot = randrange(0,9) 
                else:
                    posicion[movimiento_bot] = marca2    
                    break       
                
if jugador2 == True:
    
    while 0 == 0:
       try:
         marca1 = input("Elige tu marca (X o O): ").capitalize().replace(" ", "")
         marca2 = 0
         #verificamos que el jugador 1 haya elegido X o O
         if marca1 == "X" :
             marca2 = "O"
             break
         elif marca1 == "O" :
             marca2 = "X"
             break
         else: 
             print("Escribe X o O")   
                                                    
       except:
         print("El valor que introduciste no fue X o O")  
         
    
    while temporizador != 2.5:

                
        #Imprimimos tablero con sus posiciones
        tablero(contador)
        victoria() 
        print('Turno del jugador 1...')
        while 0 == 0:
               #preguntamos al usuario que posicion quiere    
               try:
                 movimiento = int(round(float(input("En que posicion pondras tu ficha? (Elige un numero del 1 al 9): "))))
                 movimiento -= 1
                 #verificamos que el usuario haya elegido un numero del 1 al 9
                 if posicion[movimiento] == "O" or posicion[movimiento] == "X":
                     print("Esa casilla, ya esta ocupada elige otra")                 
                 
                 elif movimiento > 8 or movimiento < 0:
                    print("Tiene que ser un numero del 1 al 9")
                     
                 else:
                    posicion[movimiento] = marca1  
                    break 
                   
               except:
                 print("El valor que introduciste no fue un numero")
        tablero(contador)         
        victoria()                                        
        print('Turno del jugador 2...')

        
        while 0 == 0:
               #preguntamos al usuario que posicion quiere    
               try:
                 movimiento_bot = int(round(float(input("En que posicion pondras tu ficha? (Elige un numero del 1 al 9): "))))
                 movimiento_bot -= 1
                 #verificamos que el usuario haya elegido un numero del 1 al 9
                 if posicion[movimiento_bot] == "O" or posicion[movimiento_bot] == "X":
                     print("Esa casilla, ya esta ocupada elige otra")                 
                 
                 elif movimiento_bot > 8 or movimiento_bot < 0:
                    print("Tiene que ser un numero del 1 al 9")
                     
                 else:
                    posicion[movimiento_bot] = marca2 
                    break  
               except:
                 print("El valor que introduciste no fue un numero")
    


