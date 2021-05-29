class Roster:
    """This class is used for keeping track of the players.

    Attributes:
        ___current_player: keeps track of the current player
        ___player_list: adds players to a list of players
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Roster): an instance of Roster.
        """
        self.___current_player = -1
        self.___player_list = []

    

    def get_player_list(self):
        """ gets the player list
        
        Args:
            self (Roster): an instance of Roster.
        """
        return self.___player_list

    def get_current_player(self):
        """ gets the current player
        
        Args:
            self (Roster): an instance of Roster.
        """
        return self.___player_list[self.___current_player]

    def add_new_player(self, player):
        """ adds a new player
        
        Args:
            self (Roster): an instance of Roster.
            player: the new player to be added.
        """
        if player not in self.___player_list:
            self.___player_list.append(player)

    def pass_turn(self):
        """ goes to the next players turn
        
        Args:
            self (Roster): an instance of Roster.
        """
        if self.___current_player < len(self.___player_list):
            self.___current_player = self.___current_player + 1
        else:
            self.___current_player = 0
