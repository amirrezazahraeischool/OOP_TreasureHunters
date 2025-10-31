
class Room():

    def __init__(self, name, user_only_description, position):
        self.name = name
        self.description = user_only_description
        self.position = position

    def __str__(self):
        return f"name = {self.name.title()}\n" \
               f"description = {self.description}\n" \
               f"position = (x = {self.position[0]}, y = {self.position[1]})\n"
    

catIsland = Room("cat island", "an island full of cats", (0, 0))
weaponBase = Room("weapon base", "take any weapon you want from here", (3, 3))
bank = Room("Bank", "The most trusted map across the waters.", (0, 2))
openingIsland = Room("opening island", "if you ever found this island, you can collect all the treasure at once magicelly", (1, 1))
entrance = Room("entrance island", "enter the cruel world of figita here.", (2, 2))
exit = Room("Exit", "exit the figita world from here.", (0, 3))

print(catIsland)
print(weaponBase)
print(bank)
print(openingIsland)
print(entrance)
print(exit)
