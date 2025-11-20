

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def __str__(self):
        return f"({self.first}, {self.second})"

Dimention = Pair
Location = Pair

class Map:
    def __init__(self, world):
        self.world = world
                        #        width          height
        self.dimention = Dimention(len(world[0]), len(world))

    def isInMap(self, location):
        if location.first >= 0 and location.first < self.dimention.second:
            if location.second >= 0 and location.second < self.dimention.first:
                return True
        return False
    
    def printMap(self, player):
        # max length of string in each column
        max_lengths = [0] * self.dimention.first

        for j in range(self.dimention.first):
            for i in range(self.dimention.second):
                curr_str_len = len(self.world[i][j].name)
                if max_lengths[j] < curr_str_len:
                    max_lengths[j] = curr_str_len
        
        px = player.location.first
        py = player.location.second

        print("Map:")
        print(f"Your location: ({px + 1}, {py + 1})")
        print(f"your are currently at {self.world[px][py].name}")
        for i in range(self.dimention.second):
            for j in range(self.dimention.first):
                ind_diff = max_lengths[j] - len(self.world[i][j].name)
                print(self.world[i][j].name + ind_diff * ' ' + ", ", end = "")
            print()
        
class Player:
    def __init__(self, name, which_map, location):
        self.name = name
        self.current_map = which_map
        self.location = location

    def move(self, command):

        # deep copy to avoid the loc_copy be 
        # merely a reference.
        loc_copy = Location(self.location.first, self.location.second)
        match(command):
            case "UP":
                self.location.first -= 1
            case "DOWN":
                self.location.first += 1
            case "LEFT":
                self.location.second -= 1
            case "RIGHT":
                self.location.second += 1
            case _:
                return False

        if map.isInMap(self.location):
            return True
        else:
            self.location = loc_copy
            return False



class Tile:
    def __init__(self, name, user_only_description):
        self.name = name
        self.description = user_only_description

    def __str__(self):
        return f"name = {self.name.title()}\n" \
               f"description = {self.description}\n"
    

def validityChecker():
    while(True):
        ans = input("are you sure, you want to proceed?(Y/n)")
        if ans == 'Y':
            return True
        elif ans == 'n':
            return False
        else:
            print("Error: invalid option!(Y/n)")


def printMenu(menu):
    for item in menu:
        print(f" - {item}")


catIsland = Tile("cat island", "an island full of cats")
weaponBase = Tile("weapon base", "take any weapon you want from here")
bank = Tile("Bank", "The most trusted map across the waters.")
openingIsland = Tile("opening island", "if you ever found this island, you can collect all the treasure at once magicelly")
entrance = Tile("entrance island", "enter the cruel world of figita here.")
exit_world = Tile("Exit", "exit the figita world from here.")
water = Tile("water", "vast ocean spanning the earth.")
map = Map([
    [ catIsland, water,       bank,         water], 
    [     water, water,      water, openingIsland],
    [weaponBase, water, exit_world,         water],    
    [     water, water,      water,      entrance],
])
player_start = Location(3, 3)
MOVEMENT_OPTIONS = ["UP", "DOWN", "LEFT", "RIGHT", "VIEW MAP", "EXIT"]

def main():

    player = Player("", map, player_start)

    # get player name
    while(True):
        player_name = input("what is your name? ")
        if validityChecker():
            player.name = player_name
            break
        else:
            print("that's ok, I did not like either.")

    print(f"welcome to our game {player.name}")

    while(True):
        printMenu(MOVEMENT_OPTIONS)
        option = input("where do you wanna go? ").upper()

        if option in MOVEMENT_OPTIONS:
            if option == "EXIT":
                print(f"have a good day {player.name}!")
                break
            elif option == "VIEW MAP":
                map.printMap(player)
            else:
                if not player.move(option):
                    print("Error: invalid move. You went out of map!")
                else:
                    print(f"you moved to {option}")
        else:
            print("Error: Unkown option. Try again.")

main()

        
    
