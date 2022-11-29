class World:
    
    def __init__(self, locale_list, nav_list):
        """locale_list - list of objects of Locale class
        nav_list - navigation matrix that defines how the locales are connected"""
        self.locale_list = locale_list 
        self.nav_list = nav_list
        self.nav_command = ["north", "east", "south", "west", "help", "quit", "examine"]
       
    def __str__(self):
        return "Surviving in Marist college!\nWelcome to your new college and congratulation on your first day here! \nYour main goal is to go through all 10 locations and survive..."

    