from classes.game import Person,bcolors
from classes.game import Spell
from classes.inventory import Item
import random


'''print("\n\n")
print("NAME               HP                                 MP")
print("                   ________________________          __________")
print(bcolors.BOLD + "Valos:    460/460 " +  bcolors.OKGREEN + "|////////////////////////| " + bcolors.ENDC + bcolors.BOLD +  "65/65 " +  bcolors.OKBLUE  + " |///////////|" + bcolors.ENDC )


print("                   ________________________          __________")
print(bcolors.BOLD + "Valos:    460/460 " +  bcolors.OKGREEN + "|////////////////////////| " + bcolors.ENDC + bcolors.BOLD +  "65/65 " +  bcolors.OKBLUE  + " |///////////|" + bcolors.ENDC )


print("                   ________________________          __________")
print(bcolors.BOLD + "Valos:    460/460 " +  bcolors.OKGREEN + "|////////////////////////| " + bcolors.ENDC + bcolors.BOLD +  "65/65 " +  bcolors.OKBLUE  + " |///////////|" + bcolors.ENDC )
'''
print("\n\n")


fire=Spell("Fire",40,600,"Black")
thunder=Spell("Thunder",40,600,"Black")
blizzard=Spell("Blizzard",40,600,"Black")
meteor=Spell("Meteor",100,1200,"Black")
quake=Spell("Quake",80,1040,"Black")

cure=Spell("Cure",50,620,"White")
cura=Spell("Cura",80,1500,"White")
curaga=Spell("Curaga",50,6000,"White")



potion = Item("Potion","potion","Heals 50 HP",50)
hipotion = Item("Hi-Potion","potion","Heals 100 HP",100)
superpotion = Item("Super Potion","potion","Heals 1000 HP",1000)
elixer = Item("Elixer","elixer","Fully restores MP/HP of one member",9999)
hielixer = Item("MegaElixer","elixer","Fully Restore's party's MP/HP",9999)

grenade = Item("Grenade","attack","Deals 500 damage",500)

player_magic = [fire,thunder,blizzard,meteor,quake,cure,cura]
enemy_spells =[fire,meteor,curaga]
player_items= [{"item" : potion , "quantity" : 10},{"item" : hipotion , "quantity" : 5},
               {"item" : elixer , "quantity" : 5},{"item" : hielixer , "quantity" : 2},
               {"item" : superpotion , "quantity" : 5},{"item" : grenade , "quantity" : 5}]


'''magic = [{"name":"Fire","cost":10,"dmg":100},
         {"name":"Thunder","cost":12,"dmg":124},
         {"name":"Blizzard","cost":10,"dmg":100}]'''
player1 = Person("VALOS :",3260,132,60,34,player_magic,player_items)
player2 = Person("NICK  :",4160,188,60,34,player_magic,player_items)
player3 = Person("ROBOT :",3089,174,60,34,player_magic,player_items)




enemy2 = Person("Magus :",12000,221,245,25,enemy_spells ,[])
enemy1 = Person("Imp   :",1250,130,560,325,enemy_spells ,[])
enemy3 = Person("Imp   :",1250,130,560,325,enemy_spells ,[])

players = [player1,player2,player3]
enemies = [enemy1,enemy2,enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "An Enenmy Attacks!!" + bcolors.ENDC)
while running :
     print("======================")

     print("\n\n")
     print("NAME          HP                                       MP")
     for player in players :
          player.get_stats()

     print("\n")

     for enemy in  enemies :
         enemy.get_enemy_stats()

     for player in players :

         player.choose_action()
         choice = input("    Choose action: ")
         index = int(choice) - 1

         if index == 0:
             dmg = player.generate_damage()
             enemy = player.choose_target(enemies)

             enemies[enemy].take_damage(dmg)
             print("You attacked " + enemies[enemy].name.replace(" ","") + "for", dmg, "points of damage.")

             if enemies[enemy].get_hp() == 0 :
                 print(enemies[enemy].name + "has died.")
                 del enemies[enemy]
         elif index == 1:
             player.choose_magic()
             magic_choice = int(input("    Choose Magic:")) - 1
             if magic_choice == -1:
                 continue

             '''magic_dmg=player.generate_spell_damage(magic_choice+1)
             spell = player.get_spell_name(magic_choice)
             cost = player.get_spell_mp_cost(magic_choice)
             '''

             spell = player.magic[magic_choice]
             magic_dmg = spell.generate_damage()

             current_mp = player.get_mp()

             if spell.cost > current_mp:
                 print(bcolors.FAIL + "\nNot Enough MP\n" + bcolors.ENDC)
                 continue

             player.reduce_mp(spell.cost)

             if spell.type == "White":
                 player.heal(magic_dmg)
                 print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
             elif spell.type == "Black":
                 enemy = player.choose_target(enemies)
                 enemies[enemy].take_damage(magic_dmg)

                 print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                       "points of damage to " + enemies[enemy].name.replace(" ","") + bcolors.ENDC)
                 if enemies[enemy].get_hp() == 0:
                     print(enemies[enemy].name.replace(" ","") + "has died.")
                     del enemies[enemy]

         elif index == 2:
             player.choose_item()
             item_choice = int(input("Choose Item :")) - 1

             if item_choice == -1:
                 continue
             item = player.items[item_choice]["item"]

             if player.items[item_choice]["quantity"] == 0:
                 print(bcolors.FAIL + "\n" + "None Left..." + bcolors.ENDC)
                 continue

             player.items[item_choice]["quantity"] -= 1

             if item.type == "potion":
                 player.heal(item.prop)
                 print(bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), "HP" + bcolors.ENDC)

             elif item.type == "elixer ":

                 if item.name == "MegaElixer" :
                     for i in players :
                         i.hp = i.maxhp
                         i.mp = i.maxmp
                 else :
                     player.hp = player.maxhp
                     player.mp = player.maxmp
                 print(bcolors.OKGREEN + "\n" + " Fully restores MP/HP " + bcolors.ENDC)

             elif item.type == "attack":
                 enemy = player.choose_target(enemies)
                 enemies[enemy].take_damage(item.prop)

                 print(bcolors.FAIL + "deals", str(item.prop), "points of damage to " + enemies[enemy].name + bcolors.ENDC)
                 if enemies[enemy].get_hp() == 0:
                     print(enemies[enemy].name.replace(" ","") + "has died.")
                     del enemies[enemy]

     defeated_enemies = 0
     defeated_players = 0
     for enemy in enemies:
         if enemy.get_hp() == 0:
             defeated_enemies += 1
     if defeated_enemies == 2:
         print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
         running = False

     for player in players:
         if player.get_hp() == 0:
             defeated_players += 1
     if defeated_players == 2:
         print(bcolors.FAIL + "Your Enemy has defeated you!!" + bcolors.ENDC)
         running = False

     for enemy in enemies :
         enemy_choice = random.randrange(0,2)
         if enemy_choice == 0 :
             target = random.randrange(0,3)
             enemy_dmg = enemy.generate_damage()

             players[target].take_damage(enemy_dmg)
             print(enemy.name.replace(" ","") + "attacks " + players[target].name.replace(" ","") +  str(enemy_dmg), "points of damage . Player HP :", players[target].get_hp())
         elif enemy_choice == 1 :
             spell,magic_dmg = enemy.choose_enemy_spell()
             enemy.reduce_mp(spell.cost)

             if spell.type == "White":
                 enemy.heal(magic_dmg)
                 print(bcolors.OKBLUE + "\n" + spell.name + " heals " + enemy.name + "for", str(magic_dmg), "HP." + bcolors.ENDC)
             elif spell.type == "Black":
                 target = random.randrange(0,3)
                 players[target].take_damage(magic_dmg)

                 print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ","") + spell.name + " deals", str(magic_dmg),
                       "points of damage to " + players[target].name.replace(" ","") + bcolors.ENDC)
                 if players[target].get_hp() == 0:
                     print(players[target].name.replace(" ","") + "has died.")
                     del players[target]
             print("Enemy chose",spell.name,"damage is ",magic_dmg)






