import os
import inquirer
import re
from time import sleep

from game.roster import Roster

class Console:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Console): an instance of Console.
        """

        self._roster = Roster()

        self.__stop_game = False
        self.__logo = []
        self.__rules = []
        self.__show_menu = True

        with open("mastermind/assets/logo.txt") as data:
            next(data)
            for line in data:
                self.__logo.append(line)

        with open("mastermind/assets/rules.txt") as data:
            next(data)
            for line in data:
                self.__rules.append(line)


    def clear_screen(self):
        """Detects OS type and sends appropriate console command to clear screen.

        Args:
            self (Console): An instance of Console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        

    def ask_stop_game(self):
        """Returns bool indicating whether game should continue running.
        
        Args:
            self (Console): an instance of Console.
        """
        return self.__stop_game


    def __print_logo(self, left = 0, top = 0, bottom = 0):
        """Prints logo to screen. Has optional x and y parameters to offset logo
        by specified amount of lines and spaces.

        Args:
            self (Console): An instance of Console.
            left (int): Number of spaces to offset logo from left of screen
            top (int): Number of lines to offset logo from top of screen
            bottom (int): Number of spaces to print below logo
        """
        
        print('\n' * top, end="")

        for line in self.__logo:
            print((" " * left) + line, end="")

        print('\n' * bottom, end="")


    def __print_rules(self, left = 0):
        """Prints rules to screen. Has optional x and y parameters to offset logo
        by specified amount of lines and spaces.

        Args:
            self (Console): An instance of Console.
            left (int): Number of spaces to offset rules from left of screen

        """

        for line in self.__rules:
            print((" " * left) + line, end="")


    def menu(self):
        """Shows menu to start game.
        
        Args:
            self (Console): an instance of Console.
        """
      
        while self.__show_menu and not self.__stop_game:
            
            p_num = len(self._roster.get_roster()) if self._roster.get_roster() else 0

            
            add_text = "Add Player [" + str(p_num) + " registered]"
            
            choice_list = [(add_text, "add"), "Rules", ("Leaderboard", "scores"), "Quit"]

            if self._roster.get_roster():
                choice_list.insert(0, "Start")

            questions = [
                inquirer.List(
                    'selection',
                message="MAIN MENU (Use ↑ and ↓ to select, ENTER to confirm)",
                choices=choice_list,
                carousel= True)
                ]
                
            self.clear_screen()
            self.__print_logo(5,2,2)
            selection = inquirer.prompt(questions)['selection'].lower()

            if selection == "start":
                self.__show_menu = False
            elif selection == "add":
                self.__add_players()
            elif selection == "rules":
                self.__show_rules()
            elif selection == "scores":
                self.__show_scoreboard()
            elif selection == "quit":
                self.__quit()
    

    def __add_players(self):
        """Asks records player names.
        
        Args:
            self (Console): an instance of Console.
        """
        keep_open = True


        while keep_open:
            players_list = []
            players_list.extend([("NEW PLAYER", "**new**")])
            players_list.extend(self._roster.get_roster())
            players_list.extend([("BACK TO MENU", "**menu**")])

            players = [
                inquirer.List(
                    'selection',
                message="ADD/REMOVE PLAYERS (Use ↑ and ↓ to select, ENTER to confirm)",
                choices=players_list,
                default="NEW PLAYER",
                carousel= True)
                ]
            
            self.clear_screen()
            self.__print_logo(5,2,2)
            selection = inquirer.prompt(players)['selection']

            if selection == "**menu**":
                keep_open = False
            elif selection == "**new**":
                name = self.__prompt_name()
                if name:
                    self._roster.add_player(name)
            else:
                delete = inquirer.confirm(f"Do you want to remove '{selection}'?", default = True)
                if delete:
                    self._roster.remove_player(selection)
                input(f"'{selection}' removed. Press ENTER to continue.")


    def __prompt_name(self):
        """Prompts for player name,.
        
        Args:
            self (Console): an instance of Console.
        """
        self.clear_screen()
        self.__print_logo(5,2,2)

        name = input("Enter new player name and press ENTER:\n")
        if not (2 < len(name) < 16):
            self.clear_screen()
            self.__print_logo(5,2,2)
            print("Username must be between 3 and 15 characters.")
            input("Press ENTER to return to player menu.")
        elif name in self._roster.get_roster():
            self.clear_screen()
            self.__print_logo(5,2,2)
            print("Player already exists.")
            input("Press ENTER to return to player menu.")
        else:
            return name
    

    def __show_rules(self):
        """Asks records player names.
        
        Args:
            self (Console): an instance of Console.
        """
        self.clear_screen()
        self.__print_logo(5,2,2)
        self.__print_rules(left= 20)
        input()
    

    def __show_scoreboard(self):
        """Asks records player names.
        
        Args:
            self (Console): an instance of Console.
        """
        self.clear_screen()
        self.__print_logo(5,2,2)
        input("Here's the screen to show high scores")
    

    def __quit(self):
        """Asks records player names.
        
        Args:
            self (Console): an instance of Console.
        """
        self.clear_screen()
        self.__print_logo(5,2,2)
        print('\n\n')
        print(f"{'THANKS FOR PLAYING!' : ^100}")
        sleep(2)
        self.__stop_game = True

    
        