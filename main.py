import random
class LootStack:
    def __init__(self):
        self.loot = {
            "potions": [],
            "weapons": [],
            "armor": [],
            "misc": [],
        }
    
    def is_empty(self):
        return len(self.loot) == 0
    
    def push_loot(self, item):
        if item == "Magic Sword" or item == "well-worn shield":
            category = "weapons"
        elif item == "Health Potion" or item == "vial of poison":
            category = "potions"
        elif item == "pristine helmet" or item == "pair of boots with wings attatched to the heels":
            category = "armor"
        else:
            category = "misc"
        if len(self.loot[category]) < 10:
            print(f"{item} acquired!")
            self.loot[category].append(item)
        else:
            print(f"You go to put the {item} in your {category} bag... but it's full. You chuck the item back on the ground.")
    
    def pop_loot(self):
        tryAgain = True
        while tryAgain:
            category = input("which category?\nWeapons\nPotions\nArmor\nMisc\n").lower()
            if category != "weapons" and category != "potions" and category != "armor" and category != "misc":
                print("Sorry, not an option!")
                tryAgain = True
            else: tryAgain = False
        try:
            print(f"You used your {self.loot[category][-1]}. It shatters instantly. You weren't really expecting that")
            self.loot[category].pop
        except:
            print(f"Your {category} bag is empty!")
    
    def peek_loot(self):
        tryAgain = True
        while tryAgain:
            category = input("which category?\nWeapons\nPotions\nArmor\nMisc\n").lower()
            if category != "weapons" and category != "potions" and category != "armor" and category != "misc":
                print("Sorry, not an option!")
                tryAgain = True
            else: tryAgain = False
        try:
            return self.loot[category][-1]
        except:
            print(f"Your {category} bag is empty!")

RANDOM_LOOT = ["Magic Sword", "Health Potion", "vial of poison", "well-worn shield", "weird bat figurine", "chunk of some kind of rock", "pristine helmet", "pair of boots with wings attatched to the heels"]

# Initialize LootStack object
player_loot = LootStack()

# Simple game loop for interaction
while True:
    print("\n=== Loot Bag Menu ===")
    print("1: Acquire new loot")
    print("2: Use loot")
    print("3: Check top loot item")
    print("4: Get random new loot")
    print("5: Exit")
    choice = input("What would you like to do? ")

    if choice == '1':
        new_loot = input("Enter the name of the loot item you acquired: ")
        player_loot.push_loot(new_loot)
    elif choice == '2':
        player_loot.pop_loot()
    elif choice == '3':
        top_loot = player_loot.peek_loot()
        if top_loot:
            print(f"The top loot item is: {top_loot}")
    elif choice == '4':
        randomLoot = RANDOM_LOOT[random.randint(1,len(RANDOM_LOOT)) - 1]
        player_loot.push_loot(randomLoot)
    elif choice == '5':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
