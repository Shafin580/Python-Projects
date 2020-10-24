import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\33[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.arkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.arkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTION" + bcolors.ENDC)
        for item in self.action:
            print(str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = (self.hp / self.maxhp) * 100

        if self.mp < spell.cost or spell.type == "Restore" and pct > 50:
            self.choose_enemy_spell()
        else:
           return spell, magic_dmg

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print(str(i) + ".", item["item"].name, ":", item["item"].description, "x", str(item["quantity"]))
            i += 1

    def choose_target(self, enemies):
        i = 1
        print(bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(str(i) + ".", enemy.name)
                i += 1
        choice = int(input("Choose target: ")) - 1
        return choice


    def get_enemy_status(self):

        enemy_hp_bar = ""
        enemy_hp_bar_ticks = ((self.hp/self.maxhp)*100)/2

        while enemy_hp_bar_ticks > 0:
            enemy_hp_bar += "█"
            enemy_hp_bar_ticks -= 1

        while len(enemy_hp_bar) < 50:
            enemy_hp_bar += " "

        enemy_hp_string = str(self.hp) + "/" + str(self.maxhp)
        enemy_current_hp = ""

        if len(enemy_hp_string) < 9:
            decreased = 9 - len(enemy_hp_string)
            while decreased > 0:
                enemy_current_hp += " "
                decreased -= 1

            enemy_current_hp += enemy_hp_string
        else:
            enemy_current_hp += enemy_hp_string

        print("ENEMY NAME                         HP                                                ")
        print("                                   __________________________________________________")
        print(bcolors.BOLD + self.name + "                  " +
              enemy_current_hp + "|" + bcolors.FAIL + enemy_hp_bar + "|" + bcolors.ENDC)

    def get_stats(self):

        hp_bar = ""
        hp_bar_ticks = ((self.hp/self.maxhp)*100)/4
        mp_bar = ""
        mp_bar_ticks = ((self.mp/self.maxmp)*100)/10
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp += hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 6:
            decreased_m = 6 - len(mp_string)
            while decreased_m > 0:
                current_mp += " "
                decreased_m -= 1

            current_mp += mp_string
        else:
            current_mp += mp_string

        print("PLAYER NAME                       HP                                     MP")
        print("                                  _________________________              __________")
        print(bcolors.BOLD + self.name + "                  " +
              current_hp + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|     " +
              current_mp + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")