class Move:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        _method (type): Description of method goes here.
    """

    def __init__(self, x, o, asterisk):
        """The class constructor.
        
        Args:
            self (Move): an instance of Move.
        """
        self._x = x
        self._o = o
        self._asterisk = asterisk


    def get_x(self):
        return self._x
  
    def get_o(self):
        return self._o

    def get_asterisk(self): #Not sure if I would need to include it...
        return self._asterisk