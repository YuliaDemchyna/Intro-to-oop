def monty_hall():
    import random 

    the_doors = ["goat", "goat", "goat"]
    car_ran = random.randint(0, 2)
    the_doors[car_ran] = "car"

    user_choice = int(input("choose between the doors(0-2): "))
    print("one door will be revealed to make it easier")

    door_index = [0, 1, 2]
    door_index.remove(user_choice)
    if user_choice != car_ran:
        door_index.remove(car_ran)

    doors_index_all = [0, 1, 2]
    door_index_game_choice = random.choice(door_index)
    doors_index_all.remove(door_index_game_choice)
    print("the door nr", door_index_game_choice, "is opened and has a", the_doors[door_index_game_choice], "inside")
    print("you can now have theese doors to choose between: ", doors_index_all)
    
    switch_doors = input("do you wish to switch your choice?: ")
    if (switch_doors == "no" and the_doors[user_choice] == "car") or (switch_doors == "yes" and the_doors[user_choice] != "car"):
        print("Congratulations! You won a car")
    else:
        print("You lost! Here is your goat")
    return

monty_hall()
