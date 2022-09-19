
def main():
    introduction = "Surviving in college! \nWelcome to your new college and congratulation on your first day here! \nYour main goal is to go through all 10 locations and survive..."
    residence = "\nNice to meet you! We will start from the first location - residence hall. \nHere you will be living with your roommate! Be sure that you know how to share space with other people."
    ok = "Okay, "
    park = "You will have more time to decorate your room, now let's move forward \nWe are now in the park. Here you can make your homework or hang out with your classmates"
    library = "Our next stop will be library. Here you can find a tone of different books \nAs well it could be quite place to study"
    dininghall = "Well..I know you are tired and hungry, right? \nHere is the dining hall! \nYou can choose any food you want and fill yourself with energy"
    classroom = "Probably, the next place is where you will spend most of your time \nThis is the lecture halls and classrooms \nIn order to survive - make your homework and be present at the lectures"
    advisor = "I know sometimes is hard to understand what you should do and understand your plan for tthe future \nYou can always come at the advisor office and ask the rule of the game or for hint"
    river = "Sometimes you just nned to calm down and spend some time with yourself \nThe river is a perfect spot! Go here at any time you want to talk to yourself."
    theater = "All events, information sessions, club activities, shows will be... \nat the theater!"
    gym = "Now we are inside the gym, perfect place to keep yourself in good form"
    gallery = "Our final stop will be at gallery \nA lot of students participate in creating annual exhibitions"
    end = "You made this! Congratulations! \nIt was not that hard, right, "
    question = "?"
    ask_for_name = "To continue, enter your name: "
    next = "Press ENTER to continue"
    
    
    print(introduction)
    name = input(ask_for_name)
    
    print(ok, name, residence)
    input(next)
    
    print(park)
    input(next)
    
    print(library)
    input(next)
   
    print(dininghall)
    input(next)
    
    print(classroom)
    input(next)
    
    print(advisor)
    input(next)
    
    print(river)
    input(next)
    
    print(theater)
    input(next)
    
    print(gym)
    input(next)
    
    print(gallery)
    input(next)
    
    print(end, name, question)
    
    
main()