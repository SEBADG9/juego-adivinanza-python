import random

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("bienvenido al juego de adivinar el numero secreto")

while not adivinado: 
    if not cant_intentos < cant_max_intentos:
        print("game over ! no has podido adivinar dentro de los 5 intentos")
        break
    entrada = input("introduce un numero del 1 al 99: ") # 
    numero = int(entrada)
    
    if numero == numero_secreto:
       print("felicidades adivinaste el numero")
       adivinado = True
    elif numero < numero_secreto:
        print("el numero es mayor al ingresado")
    else: 
        print("elnumero es menor al ingresado")

    cant_intentos +=1

   
