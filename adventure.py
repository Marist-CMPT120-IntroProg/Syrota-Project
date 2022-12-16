from locale import Locale
from world import World
from player import Player

marist_world = [{"name": "RESIDENCE HALL", "summary": "This is RESIDENCE HALL. \nHere you will be living with your roommate! Be sure that you know how to share space with other people.", "details": "Here you will find your bed, table, chair and your wardrobe. \nAs well as a window with a view of the whole university", "was_visited": True, "item": None},
                {"name": "PARK", "summary": "We are now in the PARK. \nHere you can make your homework or hang out with your classmates", "details": "Here you can see the most popular tree on the entire campus, where everyone has had a picnic at least once.", "was_visited": False, "item": None},
                {"name": "LIBRARY", "summary": "This is a LIBRARY - the best place to study and make your homework.", "details": "The LIBRARY has 3 floors. You can find here tones of different books, places for collaboration, as well as quiet spaces", "was_visited": False, "item": "Newspaper"},
                {"name": "DINING HALL", "summary": "Well..I know you are tired and hungry, right? \nHere is the DINING HALL! \nYou can choose any food you want and fill yourself with energy", "details": "We are now inside the DINING HALL. \nEach table has different food from all over the world. \nOur chefs organize different events once a week.", "was_visited": False, "item": "Burger"},
                {"name": "LECTURE HALLS AND CLASSROOMS", "summary": "Probably, here you will spend most of your time \nThis is the LECTURE HALLS AND CLASSROOMS \nIn order to survive - make your homework and be present at the lectures", "details": "You are sitting at a desk now, there is a blackboard in front of you. \nTake out your notebook and pen and prepare your ears for active listening", "was_visited": False, "item": "Pencil"},
                {"name": "ADVISOR OFFICE", "summary": "This is ADVISOR OFFICE! \nYour advisor will be helping you any time a day. \nYou can always come at the ADVISOR OFFICE to ask the rules of the game or ask for the hint", "details": "Your advisors name is Matthew Firland. He will help to develop the best strategy from start till the end", "was_visited": False, "item": None},
                {"name": "RIVER", "summary": "This is a RIVER! It is a perfect spot if you need to calm down and spend some time with yourself! Go here at any time you want to talk to yourself.", "details": "This is a bench to stop for a second and rest. You can pause your day, while sitting on it", "was_visited": False, "item": "Photo with a river view"},
                {"name": "THEATER", "summary": "All events, information sessions, club activities, shows will be here... \nat the THEATER!", "details": "If you go up this stairs, you will be right in the center of the stage. \nUse this opportunity to say what you think. This way you can find like-minded people who will become your team in the future. \nHint: Having a team will make your game go much faster and easier", "was_visited": False, "item": "Ticket"},
                {"name": "GYM", "summary": "Now we are inside the GYM, perfect place to keep yourself in good form", "details": "There are two areas: a fitness room and a swimming pool. \nTry to make it your daily routine and you will be able to do your other things more productively.", "was_visited": False, "item": "Skipping rope"},
                {"name": "GALLERY", "summary": "This is a GALLERY! \nA lot of students participate in creating annual exhibitions here", "details": "Here you can see the progress of other players, \nand at the end of your journey post your own and share your experience", "was_visited": False, "item": "Empty canvas"}
                    ]

locale_object = []
marist_map = [[None,3,1,None],[0,2,None,None],[3,4,None,1],[None,5,2,0],[5,7,6,2],[None,8,4,3],[4,9,None,None],[8,None,9,4],[None,None,7,5],[7,None,None,6]]

#replace each dictionary in marist_world with a new instance of your Locale class.
for place in marist_world:
    locale_object.append(Locale(name = place["name"], summary = place["summary"], details = place["details"], item = place["item"]))
     
#Create a new World object 
marist = World(locale_list = locale_object, nav_list = marist_map)

#Create a new Player object 
player_1 = Player(world_map = marist)

def main():
    player_1.act()
main()