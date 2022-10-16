def main():
    title = "Surviving in college!"
    introduction = "Welcome to your new college and congratulation on your first day here! \nYour main goal is to go through all 10 locations and survive..."
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
    
    ask_for_name = "To continue, enter your name: "
    next = "Press ENTER to continue"
    details = "Press ENTER to learn more"
    command = "Enter a command: "
    no_way = "Unfortunately, you are not allowed to go this way. Try another direction or ask for Help"
    
    residence2 = "Here you will find your bed, table, chair and your wardrobe. As well as a window with a view of the whole university"
    park2 = "Here you can see the most popular tree on the entire campus, where everyone has had a picnic at least once."
    library2 = "The library has 4 floors, and each floor is dedicated to a separate theme. \nFor example, now we are on the ground floor, where you can find all the books related to science"
    dininghall2 = "We are now inside the dining hall. \nEach table has different food from all over the world."
    classroom2 = "You are sitting at a desk now, there is a blackboard in front of you. \nTake out your notebook and pen and prepare your ears for active listening"
    advisor2 = "Your advisors name is Matthew Firland. He will help to develop the best strategy from start till the end"
    river2 = "This is a bench to stop for a second and rest. Sitting on it you can pause your day."
    theater2 = "If you go up this stairs, you will be right in the center of the stage. \nUse this opportunity to say what you think. This way you can find like-minded people who will become your team. \nHint: it will make your game go much faster and easier"
    gym2 = "There are two areas: a fitness room and a swimming pool. \nTry to make it your daily routine and you will be able to do your other things more productively."
    gallery2 = "Here you can see the progress of other players, \nand at the end of your journey post your own and share your experience"
    
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
    
    current_location = residence_name
    number_of_stops = 0
    
    print(title)
    print(introduction)
    name = input(ask_for_name)
    print(ok + name + residence)
    input(details)
    print(residence2)
    input(next)
    
    while True:
        direction = input(command)
        #residence_hall
        if current_location == residence_name and direction.lower() == "north":
            print(no_way)
        elif current_location == residence_name and direction.lower() == "west":
            print(no_way) 
        elif current_location == residence_name and direction.lower() == "south":
            current_location = park_name
            number_of_stops += 1
            print(park)
            input(details)
            print(park2)
            input(next)
        elif current_location == residence_name and direction.lower() == "east":
            current_location = dininghall_name
            number_of_stops += 1
            print(dininghall)
            input(details)
            print(dininghall2)
            input(next)
        #park
        elif current_location == park_name and direction.lower() == "north":
            current_location = residence_name
            number_of_stops += 1
            print(ok + name + residence)
            input(details)
            print(residence2)
            input(next)
        elif current_location == park_name and direction.lower() == "west":
            print(no_way) 
        elif current_location == park_name and direction.lower() == "south":
            print(no_way)
        elif current_location == park_name and direction.lower() == "east":
            current_location = library_name
            number_of_stops += 1
            print(library)
            input(details)
            print(library2)
            input(next) 
        #dining hall
        elif current_location == dininghall_name and direction.lower() == "north":
            print(no_way) 
        elif current_location == dininghall_name and direction.lower() == "west":
            current_location = residence_name
            number_of_stops += 1
            print(ok + name + residence)
            input(details)
            print(residence2)
            input(next) 
        elif current_location == dininghall_name and direction.lower() == "south":
            current_location = library_name
            number_of_stops += 1
            print(library)
            input(details)
            print(library2)
            input(next) 
        elif current_location == dininghall_name and direction.lower() == "east":
            current_location = advisor_name
            number_of_stops += 1
            print(advisor)
            input(details)
            print(advisor2)
            input(next)
        #library
        elif current_location == library_name and direction.lower() == "north":
            current_location = dininghall_name
            number_of_stops += 1
            print(dininghall)
            input(details)
            print(dininghall2)
            input(next) 
        elif current_location == library_name and direction.lower() == "west":
            current_location = park_name
            number_of_stops += 1
            print(park)
            input(details)
            print(park2)
            input(next)
        elif current_location == library_name and direction.lower() == "south":
            print(no_way)
        elif current_location == library_name and direction.lower() == "east":
            current_location = classroom_name
            number_of_stops += 1
            print(classroom)
            input(details)
            print(classroom2)
            input(next)
        #advisor office
        elif current_location == advisor_name and direction.lower() == "north":
            print(no_way)
        elif current_location == advisor_name and direction.lower() == "west":
            current_location = dininghall_name
            number_of_stops += 1
            print(dininghall)
            input(details)
            print(dininghall2)
            input(next)
        elif current_location == advisor_name and direction.lower() == "south":
            current_location = classroom_name
            number_of_stops += 1
            print(classroom)
            input(details)
            print(classroom2)
            input(next)
        elif current_location == advisor_name and direction.lower() == "east":
            current_location = gym_name
            number_of_stops += 1
            print(gym)
            input(details)
            print(gym2)
            input(next)
        #classroom
        elif current_location == classroom_name and direction.lower() == "north":
            current_location = advisor_name
            number_of_stops += 1
            print(advisor)
            input(details)
            print(advisor2)
            input(next)
        elif current_location == classroom_name and direction.lower() == "west":
            current_location = library_name
            number_of_stops += 1
            print(library)
            input(details)
            print(library2)
            input(next)
        elif current_location == classroom_name and direction.lower() == "south":
            current_location = river_name
            number_of_stops += 1
            print(river)
            input(details)
            print(river2)
            input(next)
        elif current_location == classroom_name and direction.lower() == "east":
            current_location = theater_name
            number_of_stops += 1
            print(theater)
            input(details)
            print(theater2)
            input(next)
        #river
        elif current_location == river_name and direction.lower() == "north":
            current_location = classroom_name
            number_of_stops += 1
            print(classroom)
            input(details)
            print(classroom2)
            input(next)
        elif current_location == river_name and direction.lower() == "west":
            print(no_way)
        elif current_location == river_name and direction.lower() == "south":
            print(no_way)
        elif current_location == river_name and direction.lower() == "east":
            current_location = gallery_name
            number_of_stops += 1
            print(gallery)
            input(details)
            print(gallery2)
            input(next)
        #gym
        elif current_location == gym_name and direction.lower() == "north":
            print(no_way)
        elif current_location == gym_name and direction.lower() == "west":
            current_location = advisor_name
            number_of_stops += 1
            print(advisor)
            input(details)
            print(advisor2)
            input(next)
        elif current_location == gym_name and direction.lower() == "south":
            current_location = theater_name
            number_of_stops += 1
            print(theater)
            input(details)
            print(theater2)
            input(next)
        elif current_location == gym_name and direction.lower() == "east":
            print(no_way)
        #theater
        elif current_location == theater_name and direction.lower() == "north":
            current_location = gym_name
            number_of_stops += 1
            print(gym)
            input(details)
            print(gym2)
            input(next)
        elif current_location == theater_name and direction.lower() == "west":
            current_location = classroom_name
            number_of_stops += 1
            print(classroom)
            input(details)
            print(classroom2)
            input(next)
        elif current_location == theater_name and direction.lower() == "south":
            current_location = gallery_name
            number_of_stops += 1
            print(gallery)
            input(details)
            print(gallery2)
            input(next)
        elif current_location == theater_name and direction.lower() == "east":
            print(no_way)
        #gallery
        elif current_location == gallery_name and direction.lower() == "north":
            current_location = theater_name
            number_of_stops += 1
            print(theater)
            input(details)
            print(theater2)
            input(next)
        elif current_location == gallery_name and direction.lower() == "west":
            current_location = river_name
            number_of_stops += 1
            print(river)
            input(details)
            print(river2)
            input(next)
        elif current_location == gallery_name and direction.lower() == "south":
            print(no_way)
        elif current_location == gallery_name and direction.lower() == "east":
            print(no_way)
        elif direction.lower() == "help":
            print("Valid commands is North, South, East, West, Help and Quit")
        elif direction.lower() == "quit":
            break
        else:
            print('Your command is not found, try again or enter "Help"')

    print(stops, number_of_stops)
    print(end + name + question)
    
main()