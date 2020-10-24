import random


playerhp = 300
enemyhp = 300
enemyattacklow = 30
enemyattackhigh = 50
playerattacklow = 30
playerattackhigh = 50

while playerhp > 0 and enemyhp > 0:
    enemydamage = random.randrange(enemyattacklow,enemyattackhigh)
    playerdamage = random.randrange(playerattacklow,playerattackhigh)
    playerhp = playerhp - enemydamage
    enemyhp = enemyhp - playerdamage

    if playerhp <= 0:
        playerhp = 0

    if enemyhp <= 0:
        enemyhp = 0

    print("Enemy attack:", enemydamage, "Points of damage. Current player hp:", playerhp)
    print("player attack:", playerdamage, "Points of damage. Current enemy hp:", enemyhp)

    if playerhp == 0:
        print("you have lost!")
        break

    if enemyhp == 0:
        print("Player have won!")
        break





