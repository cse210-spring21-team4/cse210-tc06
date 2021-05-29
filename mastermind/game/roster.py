class Roster:
    """This class is used for keeping track of the players.

    Attributes:
        __current_player: keeps track of the current player
        __player_list: adds players to a list of players
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Roster): an instance of Roster.
        """
        # self.__current_player = -1
        self.__player_list = []

    def get_player_list(self):
        """ gets the player list
        
        Args:
            self (Roster): an instance of Roster.
        """
        return self.__player_list

    def add_new_player(self, player):
        """ adds a new player
        
        Args:
            self (Roster): an instance of Roster.
            player: the new player to be added.
        """
        if player not in self.__player_list:
            self.__player_list.append(player)

    # def get_current_player(self):
    #     """ gets the current player
        
    #     Args:
    #         self (Roster): an instance of Roster.
    #     """
    #     return self.__player_list[self.__current_player]

    # def pass_turn(self):
    #     """ goes to the next players turn
        
    #     Args:
    #         self (Roster): an instance of Roster.
    #     """
    #     if self.__current_player < len(self.__player_list):
    #         self.__current_player = self.__current_player + 1
    #     else:
    #         self.__current_player = 0
