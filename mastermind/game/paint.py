class Paint:
    """A code template for a person creating a picture.
    
    Stereotype:
        Service Provider, Interfacer
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Console): an instance of Console.
        
        All assets in this init method are raw strings, derived from ASCII art by Roland Hangg.
        Original image may be found at https://www.asciiart.eu/computers/computers
        """
        self.__top = r"""                     ________________________________________________
                    /                                                \
                   |    _________________________________________     |"""
    
        self.__left_border = """                   |   |"""
    
        self.__right_border = """|    |"""

        self.__bottom = r"""                   |   |_________________________________________|    |
                   |                                                  |
                    \_________________________________________________/
                           \___________________________________/
                        ___________________________________________
                     _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
                  _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
               _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
            _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
         _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
        :-------------------------------------------------------------------------:
        `---._.-------------------------------------------------------------._.---'"""

    def paint_screen(self):
        """Creates image of text on an ASCII art computer screen.
        
        Args:
            self (Console): an instance of Console.
        """
        print(self.__top)
        print(self.__left_border, end='')
        print(" " * 41, end="")
        print(self.__right_border)
        print(self.__bottom)

