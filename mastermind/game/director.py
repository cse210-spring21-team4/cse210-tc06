from game.board import Board
from game.console import Console
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
        self.__stop_round = False

        self._board = Board()
        self._console = Console()


    def run_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while not self._console.ask_stop_game():
            players = self._console.menu()
            input('marf')
            if not self._console.ask_stop_game():
                self.__play_round(players)
            print("\n"*15)
        self._console.clear_screen()


    def __play_round(self, players= list):
        """Runs a round of play and returns a winner.
        
        Args:
            self (Director): an instance of Director.
            players (list): a list of player names.
        """
        code = self._board.generate_code()
        self._player = Player(players)

        input(code)

        while not self.__stop_round:
            for player in players:
                self._console.confirm_start(player)
                
                history = self._player.get_moves(player)
                guess = self._console.play_turn(player, code, history)
                               
                while not self._board.validate_guess(guess):
                    guess = self._console.play_turn(player, code, history, redo=True)

                if guess == code:
                    self.__end_round(player)
                    self.__stop_round =True
                    self._console.restart_menu()
                    break
                hint = self._board.create_hint(code, guess)

                self._player.record_move(player, (guess, hint))
                

    def __end_round(self, winner = str):
        """Announces the winner and ends the round
        
        Args:
            self (Director): an instance of Director.
            winner (list): name of the victor.
        """
        self._console.clear_screen()
        print("\n"*15)
        self._console.cool_print(f'           {winner} wins!')
        input()
