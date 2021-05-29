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
        self._keep_playing = True

        self._board = Board()
        self._console = Console()
        self._helper = Helper()
        self._move = Move()
        self._player = Player()
        self._roster = Roster()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """

        # Print welcome message
        self._console.show_menu
        while self._keep_playing:
            self.__ready_player(1)
            self.__ready_player(2)

    def __ready_player(self, player = int):
        """Handles gameplay for player, with player number as int.

        Args:
            self (Director): 
        """
        # Clear and reprint screen
        # Show prior guesses and hints
        # Press enter to begin turn
        # Type (or arrow select) numbers
        # Press enter to submit
        # Press enter to hide screen
