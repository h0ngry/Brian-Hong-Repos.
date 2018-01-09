import random
class enemy:
    def __init__(self):
        num = random.randint(1,3)
        self.enem_hp = 10
        if(num==1):
            self.type = "melee"
        if(num==2):
            self.type = "ranged"
        if(num==3):
            self.type = "magic"

    def attack(self,player):

        self.hit = random.randint(1,3)

        player.hp -= self.hit

    def isDead(self):
        if self.enem_hp <= 0:

            return True
        else:
            return False







class player:
    def __init__(self,type):
        if (type == 1):
            category = "melee"
        #moves
        #damage range

        if (type == 2):
            category = "ranged"

        if (type == 3):
            category = "mage"

        self.hp = 10

    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def attack(self,enemy):
        self.damage = random.randint(4,5)
        enemy.enem_hp -= self.damage




def main():

    typ = eval(input("Which class do you want to be? Press 1 to be a Warrior. Press 2 to be an Archer. Press 3 to be a mage. "))
    player_one = player(typ)
    while not player_one.isDead():
        foe = enemy()
        print("You encounter an enemy and it is of the", foe.type, "class")
        while not foe.isDead():
            print("")
            atk = eval(input("Press 1 to attack "))
            while atk != 1:
                atk = eval(input("Press 1 to attack"))
            print("")
            player_one.attack(foe)
            if foe.isDead():
                foe.enem_hp = 0
                print("You deal", player_one.damage, "points of damage")
                print("The enemy has", foe.enem_hp, "health left")
                print("The enemy is dead")
            else:
                print("You deal", player_one.damage, "points of damage")
                print("The enemy has", foe.enem_hp, "health left")

            print("")
            if not foe.isDead():
                foe.attack(player_one)
                if player_one.hp <=0:
                    player_one.hp = 0
                    print("The enemy deals", foe.hit, "points of damage")
                    print("You have", player_one.hp, "health left")
                    print("You are dead")
                    print("GAME OVER")
                    exit()
                else:
                    print("The enemy deals", foe.hit,"points of damage")
                    print("You have",player_one.hp,"health left")













main()