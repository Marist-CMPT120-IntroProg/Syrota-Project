class Player:
    
    def __init__(self, world_map):
        self.name = None
        self.world_map = world_map
        self.current_location_index = 0 
        self.move_counter = 0
        self.score_counter = 0
        self.player_item_list = []
        
    def __str__(self):
        return "You visited {}/10 locations within {} steps".format(self.score_counter, self.move_counter)
    
    def show_intro(self):
        print(self.world_map) #str representation of World class
        self.set_name()       #input the user to change the attribute name
        print("Okay, {}, \n{}".format(self.name, self.world_map.locale_list[0])) #player's automatic move to first location
        self.count_move()     
        self.count_score()
        self.world_map.locale_list[0].set_status_visited()
        print("___________________________________________________________________")
        print("Valid commands are North, South, East, West, Examine, Help and Quit")
        print(" ")

    def set_name(self):
        self.name = input("To continue, enter your name: ")
        
    def count_move(self):
        self.move_counter += 1
        
    def count_score(self):
        self.score_counter += 1
    
    def pickup_item(self):
        if self.world_map.locale_list[self.current_location_index].item != None: #check if there is an item in location
            print("Now you have {}!".format((self.world_map.locale_list[self.current_location_index].item.name).upper()))
            self.player_item_list.append(self.world_map.locale_list[self.current_location_index].item) #add item to players list
            self.world_map.locale_list[self.current_location_index].item = None #change current item name to None
        else:
            print("There is no item you can pick up")
    
    def drop_item(self):
        self.show_player_items()
        if len(self.player_item_list) > 0:     #check if player have any item
            if self.world_map.locale_list[self.current_location_index].item == None:   #check if there is current location contains item
                drop_index = int(input("Enter number of item you want to drop: "))
                self.world_map.locale_list[self.current_location_index].item = self.player_item_list[drop_index] #change currrent item in location to one user wants to drop
                self.world_map.locale_list[self.current_location_index].item.item_current_loc_id = self.current_location_index
                self.player_item_list.pop(drop_index) #delete item from players list
                print("You drop {} in {}".format(self.world_map.locale_list[self.current_location_index].item.name, self.world_map.locale_list[self.current_location_index].name))
                print("And this is CORRECT place!" if self.world_map.locale_list[self.current_location_index].item.check_correct_item_place() == True else "And this is incorrect place!")
            else:
                print("These location already have an item {}. To drop your item, pick up location item first.".format(self.world_map.locale_list[self.current_location_index].item.name))
        else:
            print("You have no item to drop.")
     
    #Method that prints all items that player have   
    def show_player_items(self):
        print("YOUR ITEMS")
        print("___________________________")
        if len(self.player_item_list) == 0:
            print("You have no items")
        else:
            for item in self.player_item_list:
                print("{}. {}".format(self.player_item_list.index(item), item.name))
    
    #input user's command and return it
    def get_move(self): 
        while True:
            print("___________________________________________________________________")
            print("You placed correctly {} items of {}".format(self.world_map.count_correct_items(),len(self.world_map.items_object_list)))
            print("You explored {} new location(s) within {} step(s)".format(self.score_counter, self.move_counter))
            print("___________________________________________________________________")
            command = input("Where do you want to go next? Enter a command: ").lower()
            if command not in self.world_map.nav_command:
                print('Your command is not available, try again or enter "Help"')
                continue
            if command == "help":
                print("Valid commands are North, South, East, West, Examine, Help and Quit")
                continue
            if command == "examine":
                print(self.world_map.locale_list[self.current_location_index].details)
                if self.world_map.locale_list[self.current_location_index].item != None:
                    print("You find {}!!!".format(self.world_map.locale_list[self.current_location_index].item.name))
                    print("And this is CORRECT place!" if self.world_map.locale_list[self.current_location_index].item.check_correct_item_place() == True else "And this is incorrect place!")
                else:
                    print("There is no items on this location:(")
                while True:
                    command_item = input("What do you want to do with your objects? \n \
                1 - Show all your items \n \
                2 - Take the item \n \
                3 - Drop the item, \n \
                4 - No action now and move on: ")
                    if command_item == "1":
                        self.show_player_items()
                    elif command_item == "2":
                        self.pickup_item()
                    elif command_item == "3":
                        self.drop_item()
                        if self.world_map.count_correct_items() == len(self.world_map.items_object_list):
                            break
                    elif command_item == "4":
                        break
                    else:
                        print("This command is not available! Enter a number of command")  
                continue
            break
        return command
    
    #take in a direction and updates the player’s current location
    #according to the navigation matrix for the player’s world
    def make_move(self, command_index):
        previous_location = self.current_location_index
        self.current_location_index = self.world_map.nav_list[self.current_location_index][command_index]
        if self.current_location_index != None:
            print("_____________________")
            print(self.world_map.locale_list[self.current_location_index])
            if self.world_map.locale_list[self.current_location_index].was_visited == False:
                self.count_score()
                self.world_map.locale_list[self.current_location_index].set_status_visited()
            self.count_move()
        else:
            self.current_location_index = previous_location
            print("Unfortunately, you are not allowed to go this way. Try another command or ask for Help")
        return self.current_location_index #Return new index of list in marist_map or None
    
    def show_outro(self):
        print("_____________________")
        print("     GAME OVER       ")
        if self.world_map.count_correct_items() == len(self.world_map.items_object_list):
            print("{}, YOU WIN! :)".format(self.name))
            print("You placed correctly {} items out of {}".format(self.world_map.count_correct_items(),len(self.world_map.items_object_list)))
            print("You made this! Congratulations! \nIt was not that hard, right, {}?".format(self.name))
        else:
            print("{}, YOU LOSE! :(".format(self.name))
            print(self)
            print("You placed correctly ONLY {} items out of {}".format(self.world_map.count_correct_items(),len(self.world_map.items_object_list)))     
        return  
    
    #create script of the game
    def act(self):
        self.show_intro()
        while self.move_counter < self.world_map.gameover_steps and self.world_map.count_correct_items() < len(self.world_map.items_object_list):
            # print("You find {} item(s) within {} stop(s) and place them in {} correct locations".format(len(self.player_item_list), self.gameover_steps, self.count_correct_items()))
            command = self.world_map.nav_command.index(self.get_move())
            if command == 5: #index of "quit" command
                break
            self.current_location_index = self.make_move(command_index = command)
        self.show_outro()
        return
