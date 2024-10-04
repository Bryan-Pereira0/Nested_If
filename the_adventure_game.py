#task1+2+3 code correction setting the scene and default path
place = input("Choose a place: forest or cave?: ")

if place == "forest":
    action = input("climb a tree or cross a river?: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if  action == "cross a river":
        print("You found a boat!")
    else: print("No.")
    pass
            
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("light a torch or proceed in the dark: ")
    if action == "light a torch":
        print("You light a torch and see a dragons nest.")
    if action == "proceed in the dark":
        print("you stumble into a dwarf city!")
    else: print("you can't do that.")
    pass
else: print("NO!")
pass