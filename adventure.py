def main():
    title = "Surviving in Marist college!"
    introduction = "Welcome to your new college and congratulation on your first day here! \nYour main goal is to go through all 10 locations and survive..."
    
    marist_world = [{"name": "RESIDENCE HALL", "summary": "This is RESIDENCE HALL. \nHere you will be living with your roommate! Be sure that you know how to share space with other people.", "details": "Here you will find your bed, table, chair and your wardrobe. \nAs well as a window with a view of the whole university", "was_visited": False},
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
    
    #Variables with location titles
    residence_dict = marist_world[0]
    park_dict = marist_world[1]
    library_dict = marist_world[2]
    dininghall_dict = marist_world[3]
    classroom_dict = marist_world[4]
    advisor_dict = marist_world[5]
    river_dict = marist_world[6]
    theater_dict = marist_world[7]
    gym_dict = marist_world[8]
    gallery_dict = marist_world[9]
    
    #Variables for all valid commands
    north_command = "north"
    west_command = "west"
    east_command = "east"
    south_command = "south"
    help_command = "help"
    quit_command = "quit"
    examine_command = "examine"
    player_commands = ["north", "west", "east", "south", "help", "quit", "examine"]
    
    #Promts for dialogue with user
    ask_for_name = "To continue, enter your name: "
    ask_command = "Where do you want to go next? Enter a command: "
    
    valid = "Valid commands are North, South, East, West, Examine, Help and Quit"
    no_way = "Unfortunately, you are not allowed to go this way. Try another command or ask for Help"
    copywright = "© Karina Syrota, 2022"
    end = "You made this! Congratulations! \nIt was not that hard, right, "
    stops = "You have successfully completed the following number of stops:"
    
    current_location = residence_dict
    number_of_stops = 0
    
    print(title)
    print(introduction)
    name = input(ask_for_name)
    print("Okay, " + name + ", \n" + marist_world[0]["summary"])
    print(valid)
    
    #Infinite loop to navigate user through the game map
    while True:
        command = input(ask_command).lower()
        #Check validity of the command
        if command not in player_commands:
            print('Your command is not available, try again or enter "Help"')
            continue
        #Start proceed the command
        if command == quit_command:
            break
        if command == help_command:
            print(valid)
            continue
        #Examine command
        if command == examine_command:
            print(current_location["details"])
            continue
        #manage user commands from RESIDENCE HALL position
        if current_location == residence_dict:
            if command == south_command:
                current_location = park_dict
                number_of_stops += 1
                print(park_dict["summary"])
            elif command == east_command:
                current_location = dininghall_dict
                number_of_stops += 1
                print(dininghall_dict["summary"])
            else:
                print(no_way)
        #manage user commands from park position
        elif current_location == park_dict:
            if command == north_command:
                current_location = residence_dict
                number_of_stops += 1
                print(residence_dict["summary"])
            elif command == east_command:
                current_location = library_dict
                number_of_stops += 1
                print(library_dict["summary"])
            else:
                print(no_way)
        #manage user commands from dining hall position
        elif current_location == dininghall_dict:
            if command == north_command:
                print(no_way) 
            elif command == west_command:
                current_location = residence_dict
                number_of_stops += 1
                print(residence_dict["summary"]) 
            elif command == south_command:
                current_location = library_dict
                number_of_stops += 1
                print(library_dict["summary"])
            elif command == east_command:
                current_location = advisor_dict
                number_of_stops += 1
                print(advisor_dict["summary"])
        #manage user commands from library position
        elif current_location == library_dict:
            if command == north_command:
                current_location = dininghall_dict
                number_of_stops += 1
                print(dininghall_dict["summary"]) 
            elif command == west_command:
                current_location = park_dict
                number_of_stops += 1
                print(park_dict["summary"])
            elif command == south_command:
                print(no_way)
            elif command == east_command:
                current_location = classroom_dict
                number_of_stops += 1
                print(classroom_dict["summary"])
        #manage user commands from ADVISOR OFFICE position
        elif current_location == advisor_dict: 
            if command == north_command:
                print(no_way)
            elif command == west_command:
                current_location = dininghall_dict
                number_of_stops += 1
                print(dininghall_dict["summary"])
            elif command == south_command:
                current_location = classroom_dict
                number_of_stops += 1
                print(classroom_dict["summary"])
            elif command == east_command:
                current_location = gym_dict
                number_of_stops += 1
                print(gym_dict["summary"])
        #manage user command from classroom position
        elif current_location == classroom_dict: 
            if command == north_command:
                current_location = advisor_dict
                number_of_stops += 1
                print(advisor_dict["summary"])
            elif command == west_command:
                current_location = library_dict
                number_of_stops += 1
                print(library_dict["summary"])
            elif command == south_command:
                current_location = river_dict
                number_of_stops += 1
                print(river_dict["summary"])
            elif command == east_command:
                current_location = theater_dict
                number_of_stops += 1
                print(theater_dict["summary"])
        #manage user command from river position
        elif current_location == river_dict:
            if command == north_command:
                current_location = classroom_dict
                number_of_stops += 1
                print(classroom_dict["summary"])
            elif command == east_command:
                current_location = gallery_dict
                number_of_stops += 1
                print(gallery_dict["summary"])
            else:
                print(no_way)
        #manage user command from gym position
        elif current_location == gym_dict: 
            if command == west_command:
                current_location = advisor_dict
                number_of_stops += 1
                print(advisor_dict["summary"])
            elif command == south_command: 
                current_location = theater_dict
                number_of_stops += 1
                print(theater_dict["summary"])
            else:
                print(no_way)
        #manage user command from theater position
        elif current_location == theater_dict: 
            if command == north_command:
                current_location = gym_dict
                number_of_stops += 1
                print(gym_dict["summary"])
            elif command == west_command:
                current_location = classroom_dict
                number_of_stops += 1
                print(classroom_dict["summary"])
            elif command == south_command:
                current_location = gallery_dict
                number_of_stops += 1
                print(gallery_dict["summary"])
            elif command == east_command:
                print(no_way)
        #manage user commands from gallery position
        elif current_location == gallery_dict:
            if command == north_command:
                current_location = theater_dict
                number_of_stops += 1
                print(theater_dict["summary"])
            elif command == west_command:
                current_location = river_dict
                number_of_stops += 1
                print(river_dict["summary"])
            else:
                print(no_way)

    print(stops, number_of_stops)
    print(end + name + " ?")
    print("_____________________")
    print(copywright)
    
main()