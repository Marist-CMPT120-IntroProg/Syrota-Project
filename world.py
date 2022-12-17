class World:
    
    def __init__(self, locale_list, nav_list, items_object_list):
        """locale_list - list of objects of Locale class
        nav_list - navigation matrix that defines how the locales are connected"""
        self.locale_list = locale_list 
        self.nav_list = nav_list
        self.nav_command = ["north", "east", "south", "west", "help", "quit", "examine"]
        self.gameover_steps = 50
        self.items_object_list = items_object_list
       
    def __str__(self):
        return "Surviving in Marist college!\nWelcome to your new college and congratulation on your first day here! \nYour main goal is find and place all {} items in correct locations in {} steps".format(len(self.items_object_list), self.gameover_steps)
    
    def count_correct_items(self):
        self.summ_correct_items = 0
        for place in self.locale_list:
            if place.item != None and place.item.check_correct_item_place() == True:
                self.summ_correct_items += 1
        return self.summ_correct_items
    
            