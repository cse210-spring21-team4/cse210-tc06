import os

class Console:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        _method (type): Description of method goes here.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Console): an instance of Console.
        """

    def clear_screen(self):
        """Detects OS type and sends appropriate console command to clear screen.

        Args:
            self (Console): An instance of Console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_welcome(self):
        """Takes string-coded input and returns.
        
        Args:
            self (Console): an instance of Console.
        """
        pass
    
    def ask_names(self):
        """Asks records player names.
        
        Args:
            self (Console): an instance of Console.
        """
        pass

    def ask_go_again(self):
        """Takes string-coded input and returns.
        
        Args:
            self (Console): an instance of Console.
        """
        pass
