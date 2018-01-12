import random

#enemy class
class enemy:
    #attributes
    def __init__(self):
        num = random.randint(1,3)
        self.enem_hp = 10
        if(num==1):
            self.type = "melee"
        if(num==2):
            self.type = "ranged"
        if(num==3):
            self.type = "magic"

    #attack method
    def attack(self,player):

        self.hit = random.randint(1,3)

        player.hp -= self.hit

    #block method
    #blocks the player attack based on chance
    def block(self):
        block_chance = random.randint(1,10)
        if block_chance == 1:
            return True
    # checks if enemy is dead
    def isDead(self):
        if self.enem_hp <= 0:

            return True
        else:
            return False






#player class
class player:

    #attributes
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
        self.score = 0

    #Checks if player is dead
    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    #attack method
    def attack(self,enemy):
        self.damage = random.randint(4,5)
        enemy.enem_hp -= self.damage

    #block method
    #blocks the enemy attack based on chance
    def block(self):
        block_chance = random.randint(1,10)
        if block_chance in {1,2,3,4,5,6,7}:
            return True




def main():
    #Prompts user to choose their class
    typ = eval(input("Which class do you want to be? Press 1 to be a Warrior. Press 2 to be an Archer. Press 3 to be a mage. "))
    player_one = player(typ)

    #All within this while loop occurs while the player/user is still alive
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
            if foe.block():
                foe.enem_hp += player_one.damage
                print("Enemy has blocked your attack")
            else:
                if foe.isDead():
                    foe.enem_hp = 0
                    player_one.score += 1
                    print("You deal", player_one.damage, "points of damage")
                    print("The enemy has", foe.enem_hp, "health left")
                    print("The enemy is dead")
                    print("")
                    resp = eval(input("Press 1 to continue "))
                    while resp !=1:
                        resp = eval(input("Press 1 to continue "))
                else:
                    print("You deal", player_one.damage, "points of damage")
                    print("The enemy has", foe.enem_hp, "health left")

            print("")
            if not foe.isDead():
                foe.attack(player_one)
                print("The enemy attacks")
                if player_one.block():
                    player_one.hp += foe.hit
                    print("You blocked the enemy's attack")
                else:
                    if player_one.hp <=0:
                        player_one.hp = 0
                        print("The enemy deals", foe.hit, "points of damage")
                        print("You have", player_one.hp, "health left")
                        print("You are dead")
                        print("GAME OVER")
                        print("")
                        print("Your final score is:", player_one.score)
                        exit()
                    else:
                        print("The enemy deals", foe.hit,"points of damage")
                        print("You have",player_one.hp,"health left")


main()