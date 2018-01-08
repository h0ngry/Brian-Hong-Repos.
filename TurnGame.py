import random
class enemy:
    def __init__(self):
        num = random.randint(1,3)
        enem_hp = 10
        if(num==1):
            type = "melee"
        if(num==2):
            type = "ranged"
        if(num==3):
            type = "magic"

    def dmg(self):

        hit = random.randint(1,3)
        if (hit == 1 or hit == 2):
            player.hp -= 1






class player:
    def __init__(self,type):
        if (type == 1):
            category = "melee"
        moves
        damage range

        if (type == 2):
            category = "ranged"

        if (type == 3):
            category = "mage"

        hp = 10

    def death(self):
        if player.hp <= 0:
            return True
        else:
            return False


def main():

    typ = eval(input("Which class do you want to be? Press 1 to be a Warrior. Press 2 to be an Archer. Press 3 to be a mage."))
    player_one = player(typ)
    while not player_one.death():
        foe = enemy()
        print("You encounter an enemy and it is of the", enemy.type, "class")










main():