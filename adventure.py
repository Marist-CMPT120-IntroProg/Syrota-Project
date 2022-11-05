def main():
    title = "Surviving in college!"
    introduction = "Welcome to your new college and congratulation on your first day here! \nYour main goal is to go through all 10 locations and survive..."
    
    marist_world = [{"name": "Residence Hall", "summary": "This is Residence Hall. \nHere you will be living with your roommate! Be sure that you know how to share space with other people.", "details": "Here you will find your bed, table, chair and your wardrobe. \nAs well as a window with a view of the whole university", "was_visited": False},
                    {"name": "Park", "summary": "We are now in the Park. \nHere you can make your homework or hang out with your classmates", "details": "Here you can see the most popular tree on the entire campus, where everyone has had a picnic at least once.", "was_visited": False},
                    {"name": "Library", "summary": "Library is the best place to study and make your homework.", "details": "The Library has 3 floors. You can find here tones of different books, places for collaboration, as well as quiet spaces", "was_visited": False},
                    {"name": "Dining Hall", "summary": "Well..I know you are tired and hungry, right? \nHere is the Dining Hall! \nYou can choose any food you want and fill yourself with energy", "details": "We are now inside the dining hall. \nEach table has different food from all over the world. \nOur chefs organize different events once a week.", "was_visited": False},
                    {"name": "Lecture Halls and Classroom", "summary": "Probably, here you will spend most of your time \nThis is the lecture halls and classrooms \nIn order to survive - make your homework and be present at the lectures", "details": "You are sitting at a desk now, there is a blackboard in front of you. \nTake out your notebook and pen and prepare your ears for active listening", "was_visited": False},
                    {"name": "Advisor Office", "summary": "This is Advisor Office! \nYour advisor will be helping you any time a day. \nYou can always come at the Advisor Office to ask the rules of the game or ask for the hint", "details": "Your advisors name is Matthew Firland. He will help to develop the best strategy from start till the end", "was_visited": False},
                    {"name": "River", "summary": "This is a River! It is a perfect spot if you need to calm down and spend some time with yourself! Go here at any time you want to talk to yourself.", "details": "This is a bench to stop for a second and rest. You can pause your day, while sitting on it", "was_visited": False},
                    {"name": "Theater", "summary": "All events, information sessions, club activities, shows will be here... \nat the Theater!", "details": "If you go up this stairs, you will be right in the center of the stage. \nUse this opportunity to say what you think. This way you can find like-minded people who will become your team in the future. \nHint: Having a team will make your game go much faster and easier", "was_visited": False},
                    {"name": "Gym", "summary": "Now we are inside the Gym, perfect place to keep yourself in good form", "details": "There are two areas: a fitness room and a swimming pool. \nTry to make it your daily routine and you will be able to do your other things more productively.", "was_visited": False},
                    {"name": "Gallery", "summary": "This is a Gallery! \nA lot of students participate in creating annual exhibitions here", "details": "Here you can see the progress of other players, \nand at the end of your journey post your own and share your experience", "was_visited": False}
                    ]
    
    #Location descriptions
    residence = "\nNice to meet you! We will start from the first location - residence hall. \nHere you will be living with your roommate! Be sure that you know how to share space with other people."
    ok = "Okay, "
    park = "You will have more time to decorate your room, now let's move forward \nWe are now in the park. Here you can make your homework or hang out with your classmates"
    library = "Our next stop will be library. Here you can find a tone of different books \nAs well it could be quite place to study"
    dininghall = "Well..I know you are tired and hungry, right? \nHere is the dining hall! \nYou can choose any food you want and fill yourself with energy"
    classroom = "Probably, the next place is where you will spend most of your time \nThis is the lecture halls and classrooms \nIn order to survive - make your homework and be present at the lectures"
    advisor = "I know sometimes is hard to understand what you should do and understand your plan for the future \nYou can always come at the advisor office to ask the rules of the game or ask for the hint"
    river = "Sometimes you just need to calm down and spend some time with yourself \nThe river is a perfect spot! Go here at any time you want to talk to yourself."
    theater = "All events, information sessions, club activities, shows will be... \nat the theater!"
    gym = "Now we are inside the gym, perfect place to keep yourself in good form"
    gallery = "Our final stop will be at gallery \nA lot of students participate in creating annual exhibitions"
    end = "You made this! Congratulations! \nIt was not that hard, right, "
    question = "?"
    stops = "You have successfully completed the following number of stops:"
    
    #Promts for dialogue with user
    ask_for_name = "To continue, enter your name: "
    ask_command = "Enter a command: "
    valid = "Valid commands are North, South, East, West, Examine, Help and Quit"
    no_way = "Unfortunately, you are not allowed to go this way. Try another command or ask for Help"
    copywright = "© Karina Syrota, 2022"
    
    #Variables containing details of each location
    residence2 = "Here you will find your bed, table, chair and your wardrobe. As well as a window with a view of the whole university"
    park2 = "Here you can see the most popular tree on the entire campus, where everyone has had a picnic at least once."
    library2 = "The library has 4 floors, and each floor is dedicated to a separate theme. \nFor example, now we are on the ground floor, where you can find all the books related to science"
    dininghall2 = "We are now inside the dining hall. \nEach table has different food from all over the world."
    classroom2 = "You are sitting at a desk now, there is a blackboard in front of you. \nTake out your notebook and pen and prepare your ears for active listening"
    advisor2 = "Your advisors name is Matthew Firland. He will help to develop the best strategy from start till the end"
    river2 = "This is a bench to stop for a second and rest. Sitting on it you can pause your day."
    theater2 = "If you go up this stairs, you will be right in the center of the stage. \nUse this opportunity to say what you think. This way you can find like-minded people who will become your team in the future. \nHint: Having a team will make your game go much faster and easier"
    gym2 = "There are two areas: a fitness room and a swimming pool. \nTry to make it your daily routine and you will be able to do your other things more productively."
    gallery2 = "Here you can see the progress of other players, \nand at the end of your journey post your own and share your experience"
    
    #Variables with location titles
    residence_name = "Residence Hall"
    park_name = "Park"
    library_name = "Library"
    dininghall_name = "Dining Hall"
    classroom_name = "Lecture Halls and Classroom"
    advisor_name = "Advisor Office"
    river_name = "River"
    theater_name = "Theater"
    gym_name = "Gym"
    gallery_name = "Gallery"
    
    #Variables for all valid commands
    north_command = "north"
    west_command = "west"
    east_command = "east"
    south_command = "south"
    help_command = "help"
    quit_command = "quit"
    examine_command = "examine"
    
    current_location = residence_name
    number_of_stops = 0
    
    print(title)
    print(introduction)
    name = input(ask_for_name)
    print(ok + name + residence)
    print(valid)
    
    #Infinite loop to navigate user through the game map
    while True:
        command = input(ask_command).lower()
        #Check validity of the command
        if command != quit_command and command != help_command and command != examine_command \
            and command != north_command and command != west_command and command != east_command and command != south_command:
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
            if current_location == residence_name:
                print(residence2)
            elif current_location == dininghall_name:
                print(dininghall2)
            elif current_location == park_name:
                print(park2)
            elif current_location == library_name:
                print(library2)
            elif current_location == advisor_name:
                print(advisor2)
            elif current_location == classroom_name:
                print(classroom2)
            elif current_location == river_name:
                print(river2)
            elif current_location == gym_name:
                print(gym2)
            elif current_location == theater_name:
                print(theater2)
            elif current_location == gallery_name:
                print(gallery2)
        if current_location == residence_name:
            if command == north_command:
                print(no_way)
            elif command == west_command:
                print(no_way) 
            elif command == south_command:
                current_location = park_name
                number_of_stops += 1
                print(park)
            elif command == east_command:
                current_location = dininghall_name
                number_of_stops += 1
                print(dininghall)
        #manage user commands from park position
        elif current_location == park_name:
            if command == north_command:
                current_location = residence_name
                number_of_stops += 1
                print(ok + name + residence)
            elif command == west_command:
                print(no_way) 
            elif command == south_command:
                print(no_way)
            elif command == east_command:
                current_location = library_name
                number_of_stops += 1
                print(library)
        #manage user commands from dining hall position
        elif current_location == dininghall_name:
            if command == north_command:
                print(no_way) 
            elif command == west_command:
                current_location = residence_name
                number_of_stops += 1
                print(ok + name + residence) 
            elif command == south_command:
                current_location = library_name
                number_of_stops += 1
                print(library)
            elif command == east_command:
                current_location = advisor_name
                number_of_stops += 1
        #manage user commands from library position
        elif current_location == library_name:
            if command == north_command:
                current_location = dininghall_name
                number_of_stops += 1
                print(dininghall) 
            elif command == west_command:
                current_location = park_name
                number_of_stops += 1
                print(park)
            elif command == south_command:
                print(no_way)
            elif command == east_command:
                current_location = classroom_name
                number_of_stops += 1
                print(classroom)
        #manage user commands from advisor office position
        elif current_location == advisor_name: 
            if command == north_command:
                print(no_way)
            elif command == west_command:
                current_location = dininghall_name
                number_of_stops += 1
                print(dininghall)
            elif command == south_command:
                current_location = classroom_name
                number_of_stops += 1
                print(classroom)
            elif command == east_command:
                current_location = gym_name
                number_of_stops += 1
                print(gym)
        #manage user command from classroom position
        elif current_location == classroom_name: 
            if command == north_command:
                current_location = advisor_name
                number_of_stops += 1
                print(advisor)
            elif command == west_command:
                current_location = library_name
                number_of_stops += 1
                print(library)
            elif command == south_command:
                current_location = river_name
                number_of_stops += 1
                print(river)
            elif command == east_command:
                current_location = theater_name
                number_of_stops += 1
                print(theater)
        #manage user command from river position
        elif current_location == river_name:
            if command == north_command:
                current_location = classroom_name
                number_of_stops += 1
                print(classroom)
            elif command == west_command:
                print(no_way)
            elif command == south_command:
                print(no_way)
            elif command == east_command:
                current_location = gallery_name
                number_of_stops += 1
                print(gallery)
        #manage user command from gym position
        elif current_location == gym_name: 
            if command == north_command:
                print(no_way)
            elif command == west_command:
                current_location = advisor_name
                number_of_stops += 1
                print(advisor)
            elif command == south_command: 
                current_location = theater_name
                number_of_stops += 1
                print(theater)
            elif command == east_command:
                print(no_way)
        #manage user command from theater position
        elif current_location == theater_name: 
            if command == north_command:
                current_location = gym_name
                number_of_stops += 1
                print(gym)
            elif command == west_command:
                current_location = classroom_name
                number_of_stops += 1
                print(classroom)
            elif command == south_command:
                current_location = gallery_name
                number_of_stops += 1
                print(gallery)
            elif command == east_command:
                print(no_way)
        #manage user commands from gallery position
        elif current_location == gallery_name:
            if command == north_command:
                current_location = theater_name
                number_of_stops += 1
                print(theater)
            elif command == west_command:
                current_location = river_name
                number_of_stops += 1
                print(river)
            elif command == south_command:
                print(no_way)
            elif command == east_command:
                print(no_way)

    print(stops, number_of_stops)
    print(end + name + question)
    print("_____________________")
    print(copywright)
    
main()