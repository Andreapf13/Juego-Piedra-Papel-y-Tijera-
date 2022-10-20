from random import choice # para la funcion display_gaime (nos va a dar un numero al azar)
from PLAY import Paper , Rock , Scissors
from PLAY import Result
def run_game():
    """
    Funcion que arranca el juego 
    """
    ask = True 
    while ask :
        display_game() #funcion que muestra el nombre del juego
        user_play = get_user_play() # le pide la jugada al usuario (piedra,papel o tijera)
        comp_play = random_play() #jugada al azar del ordenador 
        winner = get_winner(user_play,comp_play)#determina qué jugada(la de user o la comp) ES LA GANDORA O SI HAY EMPATE (no hay ganador). Si hay empate devolverá None.
        display_match(user_play,comp_play) # funcion que va a mostrar por ej. papel vs tissors 
        
        if winner == None: #empate
            display_tie(user_play,comp_play) #funcion que muestra el empate 
        else:
    
            display_victory(winner)# muestro si ha habido una victoria, le paso el ganador.
        
        ask = another_match()
        

def another_match():

    while True: 
        answer= input("Quieres jugar otra vez? S / N ")
        if answer == "S":
            return True
        elif answer == "N":
            return False 
       



   
def display_match(play1,play2):
    print(f"{play1.description()} vs {play2.description()}")
# ej. Te muestra el papel vs tissors


def display_game():
    """
    Funcion que muestra el nombre del  juego 
    """  
    print("  Rock Paper Scsissor" )


def get_user_play():
    """
    Funcion que le pregunta al usuario que quiere jugar y lo devuelve
    """
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    else: 
        return Scissors()
    
def get_user_response():
    """
    Funcion que presenta un menu de opciones y pide que seleccione una.
    Devuelve una cadena que indica lo que ha elegido 
    """
    response = None # ponemos None por poner algo 
    while True:
        print("Choose your play: ")
        print("1. Rock ")
        print("2. Paper ")
        print("3. Scissors ")

        raw = input("Enter 1, 2 or 3 : ")
        #validar raw (por si el usuario al escribirlo pone cosas raras)
        raw = raw.strip() #quita espacios al principio o al final por si el usuario pone espacios cuando le pides
        if raw == "1":
            response = 1 # si el usuario lo pone como string se lo devolvemos como int
            break
        elif raw == "2":
            response = 2
            break
        elif raw == "3":
            response = 3
            break 
        else :
            continue 
            
            
    return response

def random_play():
    """
    Funcion que selecciona una jugada al azar para competir con el usuario
    """
    return choice([Paper(),Scissors(),Rock()]) #importamos choice que nos permite que escoja al azar una de esas. 

    
def get_winner(play1,play2):#recibe la jugada 1 y la jugada 2 
    """
    Funcion que obtiene el vencedor o None si hay empate
    """
    result = play1.compare(play2)
    if result == Result.WINS:
        winner = play1
    elif result == Result.EQUAL:
        winner = None
    else:
        winner = play2
    return winner 

def  display_tie(play1,play2):#recibe la jugada 1 y la jugada 2 
    """ 
    Funcion que imprime que ha habido un empate 
    """
    print(f"Empate entre dos {play1.description()} ")
    pass

def display_victory(winner):
    """
    Funcion que muestre que winner ha ganado
    """
    print(f"Ha ganado {winner.description()}")
    
    
if __name__ == "__main__":
    run_game()
    