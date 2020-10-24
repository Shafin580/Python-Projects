import random
from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item

print("\n\n")

# Create black magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Frost", 10, 100, "Black")
meteor = Spell("Blast", 20, 200, "Black")
quack = Spell("Shake", 14, 140, "Black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Items
potion = Item("Potion", "Restore", "Restores 50 HP", 50)
superpotion = Item("Super potion", "Restore", "Restores 100 HP", 100)
megapotion = Item("Mega potion", "Restore", "Restores 500 HP", 500)
elixer = Item("Elixer", "Restore", "Restores all HP/MP of one member of the party", 9999)
megaelixer = Item("Mega elixer", "Restore", "Restores all HP/MP of all members of the party", 9999)
granade = Item("Granade", "destruction", "Deals 150 damage points to enemy", 150)

player_spells = [fire, thunder, blizzard, meteor, quack, cure, cura]
enemy_spells = [fire, meteor, cure]
player_items = [{"item": potion, "quantity": 3},
                {"item": superpotion, "quantity": 3},
                {"item": megapotion, "quantity": 3},
                {"item": elixer, "quantity": 2},
                {"item": megaelixer, "quantity": 1},
                {"item": granade, "quantity": 3}]

enemy_items = [{"item": superpotion, "quantity": 3},
                {"item": megapotion, "quantity": 1},
                {"item": granade, "quantity": 2}]

# Instantiate people
player1 = Person("Shafin", 1460, 170, 60, 36, player_spells, player_items)
player2 = Person("Emran", 1460, 170, 60, 36, player_spells, player_items)
player3 = Person("Nobin", 1100, 100, 60, 36, player_spells, player_items)

players = [player1, player2, player3]

enemy1 = Person("Imp-01:", 900, 80, 300, 15, enemy_spells, enemy_items)
enemy2 = Person("Boss:", 1200, 200, 250, 35, enemy_spells, enemy_items)
enemy3 = Person("Imp-02:", 900, 80, 300, 15, enemy_spells, enemy_items)

enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
print("==========================")
for enemy in enemies:
    enemy.get_enemy_status()

while running:

    for player in players:
        print("\n\n")
        player.get_stats()
        print("\n")

    for player in players:

        print(player.name + "'s turn:(Player) \n")
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You Attacked", enemies[enemy].name, "for", dmg)

            if enemies[enemy].get_hp() == 0:
                print(bcolors.FAIL, enemies[enemy].name, "has died!", bcolors.ENDC)
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.OKBLUE + "You don't have enough mp!" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            if spell.type == "Black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg), "points of damage to", enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL, enemies[enemy].name, "has died!", bcolors.ENDC)
                    del enemies[enemy]
            else:
                player.heal(magic_dmg)
                print("player heals for: " + bcolors.FAIL + str(magic_dmg) + " health points" + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item: ")) - 1
            if  item_choice == -1:
                continue

            item = player.items[item_choice]

            if item["quantity"] == 0:
                print(bcolors.FAIL + "You don't have this item!" + bcolors.ENDC)
                continue

            item["quantity"] -= 1

            if item["item"].type == "Restore":
                if item["item"].name == "Elixer":
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + bcolors.BOLD + "Player fully restored." + bcolors.ENDC)
                elif item["item"].name == "Mega elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    print(bcolors.BOLD + bcolors.OKGREEN + "All players have been restored!" + bcolors.ENDC)

                else:
                    player.heal(item["item"].prop)
                    print(bcolors.OKGREEN + bcolors.BOLD + item["item"].name, "heals player for", str(item["item"].prop), "HP" + bcolors.ENDC)

            elif item["item"].type == "destruction":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item["item"].prop)
                print(bcolors.FAIL + "Enemy:", enemies[enemy].name, "takes", str(item["item"].prop), "damage points.")
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL, enemies[enemy].name, "has died!", bcolors.ENDC)
                    del enemies[enemy]

    defeated_enemies = 0
    for enemy in enemies:
        enemy.get_enemy_status()
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    if defeated_enemies == 3:
        print(bcolors.OKGREEN + bcolors.BOLD + "You win!" + bcolors.ENDC)
        running = False

    defeated_players = 0
    for j in players:
        if j.get_hp() == 0:
            defeated_players += 1
    if defeated_players == 3:
        print(bcolors.FAIL + bcolors.BOLD + "You lost!" + bcolors.ENDC)
        running = False

    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        target = random.randrange(0, 3)

        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print("Enemy:", enemy.name, "attacked", players[target].name, "for", enemy_dmg, "points.")
            if players[target].get_hp() == 0:
                print(bcolors.FAIL, players[target].name, "has died!", bcolors.ENDC)
                del players[target]

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            if spell.type == "Black":
                players[target].take_damage(spell.dmg)
                print(bcolors.OKBLUE, "Enemy:", enemy.name, "chose:", spell.name, "\nDamage is:", spell.dmg, "points", bcolors.ENDC)
                if players[target].get_hp() == 0:
                    print(bcolors.FAIL, players[target].name, "has died!", bcolors.ENDC)
                    del players[target]
            else:
                enemy.heal(spell.dmg)
                print(bcolors.OKBLUE + "Enemy:", enemy.name, "used", spell.name, "and healed himself.")


    print("======================================")










