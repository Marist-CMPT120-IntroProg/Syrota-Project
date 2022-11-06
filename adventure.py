def main():
    title = "Surviving in Marist college!"
    introduction = "Welcome to your new college and congratulation on your first day here! \nYour main goal is to go through all 10 locations and survive..."
    
    marist_world = [{"name": "RESIDENCE HALL", "summary": "This is RESIDENCE HALL. \nHere you will be living with your roommate! Be sure that you know how to share space with other people.", "details": "Here you will find your bed, table, chair and your wardrobe. \nAs well as a window with a view of the whole university", "was_visited": True},
                    {"name": "PARK", "summary": "We are now in the PARK. \nHere you can make your homework or hang out with your classmates", "details": "Here you can see the most popular tree on the entire campus, where everyone has had a picnic at least once.", "was_visited": False},
                    {"name": "LIBRARY", "summary": "This is a LIBRARY - the best place to study and make your homework.", "details": "The LIBRARY has 3 floors. You can find here tones of different books, places for collaboration, as well as quiet spaces", "was_visited": False},
                    {"name": "DINING HALL", "summary": "Well..I know you are tired and hungry, right? \nHere is the DINING HALL! \nYou can choose any food you want and fill yourself with energy", "details": "We are now inside the DINING HALL. \nEach table has different food from all over the world. \nOur chefs organize different events once a week.", "was_visited": False},
                    {"name": "LECTURE HALLS AND CLASSROOMS", "summary": "Probably, here you will spend most of your time \nThis is the LECTURE HALLS AND CLASSROOMS \nIn order to survive - make your homework and be present at the lectures", "details": "You are sitting at a desk now, there is a blackboard in front of you. \nTake out your notebook and pen and prepare your ears for active listening", "was_visited": False},
                    {"name": "ADVISOR OFFICE", "summary": "This is ADVISOR OFFICE! \nYour advisor will be helping you any time a day. \nYou can always come at the ADVISOR OFFICE to ask the rules of the game or ask for the hint", "details": "Your advisors name is Matthew Firland. He will help to develop the best strategy from start till the end", "was_visited": False},
                    {"name": "RIVER", "summary": "This is a RIVER! It is a perfect spot if you need to calm down and spend some time with yourself! Go here at any time you want to talk to yourself.", "details": "This is a bench to stop for a second and rest. You can pause your day, while sitting on it", "was_visited": False},
                    {"name": "THEATER", "summary": "All events, information sessions, club activities, shows will be here... \nat the THEATER!", "details": "If you go up this stairs, you will be right in the center of the stage. \nUse this opportunity to say what you think. This way you can find like-minded people who will become your team in the future. \nHint: Having a team will make your game go much faster and easier", "was_visited": False},
                    {"name": "GYM", "summary": "Now we are inside the GYM, perfect place to keep yourself in good form", "details": "There are two areas: a fitness room and a swimming pool. \nTry to make it your daily routine and you will be able to do your other things more productively.", "was_visited": False},
                    {"name": "GALLERY", "summary": "This is a GALLERY! \nA lot of students participate in creating annual exhibitions here", "details": "Here you can see the progress of other players, \nand at the end of your journey post your own and share your experience", "was_visited": False}
                    ]
    
    #2D matrix of Marist map
    marist_map = [[None,3,1,None],[0,2,None,None],[3,4,None,1],[None,5,2,0],[5,7,6,2],[None,8,4,3],[4,9,None,None],[8,None,9,4],[None,None,7,5],[7,None,None,6]]
    
    #Function that help to determine user move through the map
    def move(current_location_index, command_index):
        new_current_location = marist_map[current_location_index][command_index] 
        if new_current_location != None:
            print(marist_world[new_current_location]["summary"])
            if marist_world[new_current_location]["was_visited"] == False:
                nonlocal visited_location
                visited_location += 1
                marist_world[new_current_location]["was_visited"] = True
        return new_current_location #Return new index of list in marist_map or None

    player_commands = ["north", "east", "south", "west", "help", "quit", "examine"]
    
    #Promts for dialogue with user
    ask_for_name = "To continue, enter your name: "
    ask_command = "Where do you want to go next? Enter a command: "
    
    valid = "Valid commands are North, South, East, West, Examine, Help and Quit"
    no_way = "Unfortunately, you are not allowed to go this way. Try another command or ask for Help"
    copywright = "© Karina Syrota, 2022"
    end = "You made this! Congratulations! \nIt was not that hard, right, "
    stops = "You have successfully completed the following number of stops:"
    score = "Your score is: "
    
    current_location = 0
    number_of_stops = 0
    visited_location = 1 #Starting from Residence Hall
    
    print(title)
    print(introduction)
    name = input(ask_for_name)
    print("Okay, " + name + ", \n" + marist_world[0]["summary"])
    print(valid)
    
    #Infinite loop to navigate user through the game map with the use of matrix and dictionary
    while True:
        command = input(ask_command).lower() 
        if command in player_commands:
            command = player_commands.index(command)  #Checks if the command in the list of commands and determine the index of desire command
            if command == 4:                          #Help command
                print(valid)
                continue
            elif command == 5:                        #Quit command
                break
            elif command == 6:                        #Determine command
                print(marist_world[current_location]["details"])
                continue
        else: 
            print('Your command is not available, try again or enter "Help"')
            continue
        previous_location = current_location          
        current_location = move(current_location, command) 
        print("You find ", visited_location, " locations out of 10") 
        if current_location == None:
            current_location = previous_location      #Return previous location index to make examine command work
            print(no_way)
        else:
            number_of_stops += 1

    print(stops, number_of_stops)
    print(end + name + " ?")
    print(score, visited_location)
    print("_____________________")
    print(copywright)
    
main()