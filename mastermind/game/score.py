from time import time


class Score:
    """A code template for a person keeping track of the number of turns
    each player has taken, as well as how long each turn took.

    Stereotype:
        Information Holder
    """

    def __init__(self, players=list):
        """The class constructor.

        Args:
            self (Score): an instance of Score.
            players (list): a list of players in the round
        """
        self.__turns = {player: [] for player in players}
        self.__start = 0
        self.__end = 0

    def turn_start(self):
        """Records start time (in seconds, starting at Epoch) of players turn.

        Args:
            self (Score): an instance of Score.
        """
        self.__start = time()

    def turn_end(self, player=str):
        """Records end time (in seconds, starting at Epoch) of players turn.
        Start time is subtracted from end time, and the resulting elapsed time
        is appended to a given player's

        Args:
            self (Score): an instance of Score.
        """
        self.__end = time()
        self.__turns[player].append(self.__end - self.__start)

    def get_scores(self):
        """Returns a dictionary of lists of player turn times, with structure:
        {"Player 1":[10, 7, 15, 20], "Player 2":[13, 12.5, 15, 21], etc.}

        Args:
            self (Score): an instance of Score.
        """
        return self.__turns
