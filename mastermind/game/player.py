class Player:
    """A person taking part in a game. 
       The responsibility of Player is to record player moves and hints.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _move (Move): The player's last move.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self.__moves = {}


        
    def get_moves(self, player = str):
        """Returns a player's move/hint record. If the player 
        hasn't moved yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self.__moves[player]


    def record_move(self, player = str, move_hint = tuple):
        """Sets the player's last move to the given instance of Move.

        Args:
            self (Player): an instance of Player.
            move_hint (tuple): a tuple of strings of the player's move, 
                                followed by the resulting hint.
        """
        current = self.get_moves(player) if self.get_moves(player) else []
        self.__moves[player] = current.extend(move_hint)
