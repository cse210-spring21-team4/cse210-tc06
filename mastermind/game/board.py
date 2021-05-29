import random


class Board:
    """ (AH). The Prepare Method and _Create_Hint Method were given.

    A code template to track the gameboard for a Mastermind game.
    The responsibility of this class of objects is to prepare the gameboard
    with a random four digit number and create hints for the players.

    Mastermind is a game in which each player seeks to guess the secret code
        they've been assigned before the other players do.

    In the Prepare Method:
    The code is a randomly generated, four digit number between 1000 and 9999.

    In the _Create_Hint Method:
    The players take turns guessing the secret code based on the hint that is offered.
        An x means a correct number in a correct position.
        An o means a correct number in an incorrect position.
        An * means an incorrect number (see interface section).

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        _method (type): Description of method goes here.

        code (integer): a randomly generated four digit number between 1000 and 9999.
        guess (integer): each player guesses a four digit number.
    """

    def __init__(self):
        """
        The class constructor.

        Args:
            self (Board): an instance of Board.
        """
        pass

    def prepare(self, player):
        """ (Prepare Method was given in a requirement snippet.)
        Sets up the board with an entry for each player.

        Args:
            self (Board): an instance of Board.
            player (Player): an instance of Player.  (AH).
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def validate_guess(self, guess):
        """ (AH).
        Board.validate_guess verifies that guess is a four-digit integer.

        Args:
            self (Board): an instance of Board.
            guess (string): The guess that was made.

        Returns:
            Boolean: whether the guess is a four-digit integer.
        """
        pass

    def _create_hint(self, code, guess):
        """ (_Create_Hint Method was given in a requirement snippet.)
        Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def update_board(self, player, guess):
        """ (AH).
        Updates the gameboard with player, current guess, and current hint.

        Args:
            self (Board): An instance of Board.
            player (Player): an instance of Player.
            guess (string): The guess that was made.

        Returns:
            None.
        """

    def info_to_display(self, player):
        """ (AH).
        Passes current board information for Director to call Console to display.

        Args:
            self (Board): An instance of Board.
            player (Player): an instance of Player.

        Returns:
            string: A four-digit integer guess in the form [xxxx].
            string: A hint in the form [xxxx]
        """
        pass
