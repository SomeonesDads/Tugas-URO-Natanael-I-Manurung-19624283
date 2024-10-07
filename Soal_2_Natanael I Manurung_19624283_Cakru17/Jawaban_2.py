import random, math


## UI Elements
def border():
    print("-----------------------------------------------------")


def health_bar(name, cur, max):
    bars = math.floor(cur / max * 40)
    hp_bar = ""
    for i in range(bars):
        hp_bar += '|'
    for i in range(40 - bars):
        hp_bar += "-"
    print(name + '\n' + hp_bar + "    " + str(cur) + '/' + str(max))


def display_moves(moves):
    space1 = "      "
    space2 = "      "
    difference = len(moves[0]) - len(moves[1])
    if difference > 0:
        for i in range(difference):
            space2 += " "
    elif difference < 0:
        for i in range(-difference):
            space1 += " "
    print("1. " + moves[0] + space1 + "3. " + moves[2] + "\n2. " + moves[1] + space2 + "4. " + moves[3])


# List Robot
robot_list = (
    ("Tiger-Bot", 100, 100, 100, 0, ["HEAL", "ELECTRIC CLAW", "PROPELLED LUNGE", "RAWRRR"]),
    ("Elephant-Bot", 200, 75, 125, 0, ["PLASMA BRACE", "SEISMIC BLAST", "QUANTUM CHARGE", "RECHARGE"]),
    ("Eagle-Bot", 85, 120, 50, 20, ["SONIC BOOM", "MACH FIVE", "ROOST", "METEORIC DIVE"])
)


class robot:
    def __init__(self, attributes):
        self.name, self.hp, self.attack, self.defense, self.evasion, self.moves = attributes
        self.maxhp = self.hp

    def move(self, opponent, index):
        movesets = {  ## Nama: (Damage, healing, +attack, +defense, +evasi, akurasi)
            "HEAL": (0, 50, 0, 0, 0, 0),
            "ELECTRIC CLAW": (35, 0, 0, 0, 0, 100),
            "PROPELLED LUNGE": (70, 0, 0, 0, 0, 50),
            "RAWRRR": (0, 0, 60, 0, 0, 0),
            "PLASMA BRACE": (0, 0, 0, 20, 0, 0),
            "SEISMIC BLAST": (25, 0, 0, 0, 0, 100),
            "QUANTUM CHARGE": (45, 0, 0, 0, 0, 50),
            "RECHARGE": (0, 35, 0, 0, 0, 0),
            "SONIC BOOM": (20, 0, 0, 0, 0, 100),
            "MACH FIVE": (0, 0, 0, 0, 10, 0),
            "ROOST": (0, 21, 0, 0, 0, 0),
            "METEORIC DIVE": (40, 0, 0, 0, 0, 50)
        }
        current_move = movesets[self.moves[index]]
        if random.randint(0, 100) > current_move[5] - opponent.evasion and current_move[0] != 0:
            print(self.name + " used " + self.moves[index] + " towards " + opponent.name + " and it MISSED!")
        elif current_move[0] > 0:
            damage = math.floor(current_move[0] * self.attack / opponent.defense)
            print(self.name + " used " + self.moves[index] + " towards " + opponent.name + " and it dealt " + str(
                damage) + " HP!")
            opponent.hp -= damage
        if current_move[1] > 0:
            self.hp += current_move[1]
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            print(
                self.name + " used " + self.moves[index] + " on itself and recovered " + str(current_move[1]) + ' HP!')
        if current_move[2] > 0:
            self.attack += current_move[2]
            print(self.name + " used " + self.moves[index] + " on itself and increased its attack by " + str(
                current_move[2]) + '!')
        if current_move[3] > 0:
            self.evasion += current_move[3]
            print(self.name + " used " + self.moves[index] + " on itself and increased its defense by " + str(
                current_move[3]) + '!')
        if current_move[4] > 0:
            self.evasion += current_move[4]
            print(self.name + " used " + self.moves[index] + " on itself and increased its evasion by " + str(
                current_move[4]) + '!')


class battle:
    def start_fight(self, player, opponent):
        while True:
            border()
            health_bar(player.name, player.hp, player.maxhp)
            health_bar(opponent.name, opponent.hp, opponent.maxhp)
            display_moves(player.moves)
            while True:
                try:
                    selected_move = input("Select your move: ")
                    player.move(opponent, int(selected_move) - 1)
                    break
                except:
                    input("Please type in numbers from 1 to 4")
            input('')
            if opponent.hp <= 0:
                print("The opponent's   " + opponent.name + " is defeated!")
                print("Your             " + player.name + " wins!")
                border()
                break
            border()
            health_bar(player.name, player.hp, player.maxhp)
            health_bar(opponent.name, opponent.hp, opponent.maxhp)
            opponent.move(player, random.randint(0, 3))
            input('')
            if player.hp <= 0:
                print("Your             " + player.name + " is defeated!")
                print("The opponent's   " + opponent.name + " wins!")
                border()
                break


class game:
    def __init__(self, is_ongoing):
        self.is_ongoing = is_ongoing

    def add_robot(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def start_game(self):
        while self.is_ongoing:
            menu_open = True
            while menu_open:
                print("------------------- GAME ROBOT ----------------------")
                print("Choose your robot!")
                for i in range(len(robot_list)):
                    print(str(i + 1) + '. ' + robot_list[i][0])
                print(str(len(robot_list) + 1) + ". Help")
                try:
                    robot1 = robot(robot_list[int(input("Which one: ")) - 1])
                    robot2 = robot(robot_list[int(input("Against: ")) - 1])
                except IndexError or NameError:
                    border()
                    print("Either you pressed help or a number outside the selection")
                    print("To continue the game, press ENTER after every move, including the opponent's")
                    print("Robot descriptions:")
                    print("1. Tiger-Bot         A furious attacker")
                    print("2. Elephant-Bot      A tough defender")
                    print("3. Eagle-Bot         A speed master")
                    input("Press ENTER to continue")
                    continue
                except ValueError:
                    border()
                    print("ERROR: Please input an integer\nPress ENTER to continue")
                    input("")
                menu_open = False
            border()
            self.add_robot(robot1, robot2)
            ongoing_battle = battle()
            ongoing_battle.start_fight(self.player, self.opponent)
            if input("Play Again? (y/n) ") == 'y' or 'Y':
                self.is_ongoing = True
            else:
                break


# Main
ongoing_game = game(True)
ongoing_game.start_game()
