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

    def paint_screen(self, player = str, history = list):
        """Creates image of text on an ASCII art computer screen.
        
        Args:
            self (Console): an instance of Console.
            player (string): name of player.
            history (list): list of (guess, hint) tuples.
        """
        print(self.__top)
        self.__paint_header(player)
        for i in range(1,14):
            self.__paint_line(str(i), str(i + 2))
        print(self.__bottom)

    def __paint_header(self, player = str):
        """Paints header text on an ASCII art computer screen.
        
        Args:
            self (Console): an instance of Console.
            player (string): name of player.
        """

        title = " User: " + player + " >> echo $HISTORY"
        print(self.__left_border, end='')
        print(f"{title:<41}", end='')
        print(self.__right_border)

        print(self.__left_border, end='')
        print(f"{'........INPUT.......':^20}", end='')
        print(f"{'|':^1}", end='')
        print(f"{'.......OUTPUT.......':^20}", end='')
        print(self.__right_border)


    def __paint_line(self, left_col = str, right_col = str):
        """Paints one line of text, in two columns, on ASCII
        art computer screen.
        
        Args:
            self (Console): an instance of Console.
            left_col (string): text to paint in left column 
            right_col (string): text to paint in right column 
        """
        print(self.__left_border, end='')
        print(f"{left_col:^20}", end='')
        print(f"{'|':^1}", end='')
        print(f"{right_col:^20}", end='')
        print(self.__right_border)