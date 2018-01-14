import random

#enemy class
class enemy:
    #attributes
    #If enemy or player is melee, then it will do more damage to ranged opponents.
    #Ranged will do more damage to magic opponents.
    #Magic will do more damage to melee opponents.
    def __init__(self):
        num = random.randint(1,3)
        self.enem_hp = 10
        if(num==1):
            self.type = "warrior"

        if(num==2):
            self.type = "archer"
        if(num==3):
            self.type = "mage"

    #attack method
    def attack(self,player):
        dmg_multiplier = 2
        self.hit = random.randint(1,3)

        if self.type == 'warrior' and player.type == 'archer':
            self.hit = self.hit * dmg_multiplier

        if self.type == 'archer' and player.type == 'mage':
            self.hit = self.hit * dmg_multiplier

        if self.type == 'mage' and player.type == 'warrior':
            self.hit = self.hit * dmg_multiplier



        player.hp -= self.hit

    #block method
    #blocks the player attack based on chance
    #Enemy has a 20% chance of blocking
    def block(self):
        block_chance = random.randint(1,10)

        if block_chance in {1,2}:
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
    def __init__(self,category):
        if (category == 1):
            self.type = "warrior"
        #moves
        #damage range

        if (category == 2):
            self.type = "archer"

        if (category == 3):
            self.type = "mage"

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
        self.hit = random.randint(4,5)
        if self.type == 'warrior' and enemy.type == 'archer':
            self.hit = self.hit * dmg_multiplier

        if self.type == 'archer' and enemy.type == 'mage':
            self.hit = self.hit * dmg_multiplier

        if self.type == 'mage' and enemy.type == 'warrior':
            self.hit = self.hit * dmg_multiplier
        enemy.enem_hp -= self.hit

    #block method
    #blocks the enemy attack based on chance
    #You have a 50% chance of blocking an attack
    def block(self):
        block_chance = random.randint(1,10)
        if block_chance in {1,2,3,4,5}:
            return True




def main():

    #INTRODUCTION part
    #Prompts user to choose their class
    typ = eval(input("Which class do you want to be? Press 1 to be a Warrior. Press 2 to be an Archer. Press 3 to be a Mage. "))
    while typ not in {1,2,3}:
        typ = eval(input("Which class do you want to be? Press 1 to be a Warrior. Press 2 to be an Archer. Press 3 to be a Mage. "))
    if typ == 1:
        print("")
        print("You choose to be a Warrior which has a damage boost against archers")
        print("")
    if typ == 2:
        print("")
        print("You choose to be an Archer which has a damage boost against mages")
        print("")
    if typ == 3:
        print("")
        print("You choose to be a Mage which has a damage boost against warriors")
        print("")
    player_one = player(typ)


    #All within this while loop occurs while the player/user is still alive
    while not player_one.isDead():
        foe = enemy()
        print("You encounter an enemy and it is of the", foe.type, "class")
        while not foe.isDead():
            print("")
            atk = eval(input("Press 1 to attack "))
            while atk != 1:
                atk = eval(input("Press 1 to attack "))
            print("")
            player_one.attack(foe)
            if foe.block():
                foe.enem_hp += player_one.hit
                print("Enemy has blocked your attack")
                print("The enemy has", foe.enem_hp, "health left")
            else:
                if foe.isDead():
                    foe.enem_hp = 0
                    player_one.score += 1
                    print("You deal", player_one.hit, "points of damage")
                    print("The enemy has", foe.enem_hp, "health left")
                    print("The enemy is dead")
                    print("")
                    resp = eval(input("Press 1 to continue "))
                    while resp !=1:
                        resp = eval(input("Press 1 to continue "))
                else:
                    print("You deal", player_one.hit, "points of damage")
                    print("The enemy has", foe.enem_hp, "health left")

            print("")
            if not foe.isDead():
                foe.attack(player_one)
                print("The enemy attacks")
                if player_one.block():
                    player_one.hp += foe.hit
                    print("You blocked the enemy's attack")
                    print("You have", player_one.hp, "health left")
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