from contextlib import _SupportsClose
from enum import Enum


class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2
    
class Play(object):
    """
    Clase que representa una jugada
    """
    def description(self):
        pass
    def compare(self,otherPlay): 
        """
        Metodo que se compara con la otra jugada
        y devuelve un resultado de la comparación:
        comparo piedra con piedra = empate
        piedra y tijera = gano
        Gano, pierdo o empato. --> hacemos enum (EQUAL,WINS,LOSES)
        """
        pass

class Paper(Play):
     def description(self):
        return "Paper"
     def compare(self,otherPlay):
        """
        Metodo que compara papel con otras jugadas y devuelve Result
        """
        result = None # Variable que la inicializo con cualquier valor
        if type(otherPlay) == Rock or type(otherPlay) == Spock: 
            result = Result.WINS
        elif type(otherPlay) == Scissors or type(otherPlay) == Lagarto:
            result = Result.LOSES
        else:
            result = Result.EQUAL
        return result 
    

class Scissors(Play):
     def description(self):
        return "Scissors ✂️✂️✂️ "
     def compare(self,otherPlay):
        """
        Metodo que compara papel con otras jugadas y devuelve Result
        """
    
        result = None # Variable que la inicializo con cualquier valor
        if type(otherPlay) == Paper or type(otherPlay) == Lagarto: 
            result = Result.WINS
        elif type(otherPlay) == Rock or type(otherPlay) == Spock:
            result = Result.LOSES
        else:
            result = Result.EQUAL
        return result 
    

class Rock(Play):
     def description(self):
        return "Rock "
     def compare(self,otherPlay):
        """
        Metodo que compara papel con otras jugadas y devuelve Result
        """
        result = None # Variable que la inicializo con cualquier valor
        if type(otherPlay) == Paper or type(otherPlay) == Spock: 
            result = Result.LOSES
        elif type(otherPlay) == Scissors or type(otherPlay) == Lagarto:
            result = Result.WINS
        else:
            result = Result.EQUAL
        return result 

class Spock(Play):
    def description(self):
        return "Spock 🖖🖖🖖🖖🖖"
    def compare(self,otherPlay):
        """
        Metodo que compara papel con otras jugadas y devuelve Result
        """
        result = None # Variable que la inicializo con cualquier valor
        if type(otherPlay) == Paper or type(otherPlay) == Lagarto: 
            result = Result.LOSES
        elif type(otherPlay) == Scissors or type(otherPlay) == Rock:
            result = Result.WINS
        else:
            result = Result.EQUAL
        return result
 
class Lagarto(Play):
    def description(self):
        return "Lagarto 🦎🦎🦎🦎🦎"
    def compare(self,otherPlay):
        result = None # Variable que la inicializo con cualquier valor
        if type(otherPlay) == Rock or type(otherPlay)  == Scissors:
            result = Result.LOSES
        elif type(otherPlay) == Spock or type(otherPlay) == Paper:
            result = Result.WINS
        else:
            result = Result.EQUAL
        return result
    
 

