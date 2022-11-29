class Player:
    
    def __init__(self, world_map):
        self.name = None
        self.world_map = world_map
        self.current_location_index = 0 
        self.move_counter = 0
        self.score_counter = 0
        
    def __str__(self):
        return "You visited {}/10 locations with {} stops".format(self.score_counter, self.move_counter)
    
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
    
    #input user's command and return it
    def get_move(self): 
        while True:
            command = input("Where do you want to go next? Enter a command: ").lower()
            if command not in self.world_map.nav_command:
                print('Your command is not available, try again or enter "Help"')
                continue
            if command == "help":
                print("Valid commands are North, South, East, West, Examine, Help and Quit")
                continue
            if command == "examine":
                print(self.world_map.locale_list[self.current_location_index].details)
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
        print(self)
        if self.score_counter == 10:
            print("You made this! Congratulations! \nIt was not that hard, right, {}?".format(self.name))
        else:
            print("Come back next time to discover new interesting Marist locations, which you are not visited yet. \nSee you!")
        print("_____________________")
        print("© Karina Syrota, 2022")
        return  
    
    #create script of the game
    def act(self):
        self.show_intro()
        while self.score_counter < 10:
            print("You explored {} new location(s) within {} stop(s)".format(self.score_counter, self.move_counter))
            command = self.world_map.nav_command.index(self.get_move())
            if command == 5: #index of "quit" command
                break
            self.current_location_index = self.make_move(command_index = command)
        self.show_outro()
        return
