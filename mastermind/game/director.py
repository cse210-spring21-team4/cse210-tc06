from game.board import Board
from game.console import Console
from game.helper import Helper
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        keep_playing (boolean): Whether or not the game can continue.
        board (Board): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        helper (Helper): An instance of the class of objects known as Helper.
        move (Move): An instance of the class of objects known as Move.
        player (Player): An instance of the class of objects known as Player.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.__keep_playing = True

        self.__board = Board()
        self.__console = Console()
        self.__helper = Helper()
        self.__move = Move()
        self.__player = Player()
        self.__roster = Roster()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        pass