#task1 task2 task3
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
if attendees>50:
    print(venue+(" with projector and speakers"))
else: print(venue+" with projector")
if attendees>20:
    meal = str(input("Would you like vegetarian food? Y/N: ")) 
if meal == "Y":
    print("Veggie Delight Caterers")
else: print("Gourmet Meal Caterers")
    
