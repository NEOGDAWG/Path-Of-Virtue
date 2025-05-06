import random #import random to use random numbers
import time #import time to add pauses in the text display
import sys #import sys so the text prints 1 by 1






#these are all the variables that store the main information to play the game
morality = 100
health = 100
strength = 15
inventory = []
name = "TAURUS DEMON"
player_health = 100
done1 = True
done2 = True
flag = False
current_room = 0
next_room = 0
done = False
dialogue1 = "you are in a alleyway where you see a goblin gang being very aggresive to and old man. If you wish to go find help for the old man go north. There are passeges to the east and west."
dragon = 0






#this is the function that is used to print the text letter be letter
def print1(text, delay=0.003):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.003)
    print1
  





#the rooms
room_list = []
#room 0
room = ["You are in the main city hub. Many magical beasts and unusal beings are walking around enjoying the night life. There are passages in all directions.", 1, 2, 3, 4, "", "", ""]
room_list.append(room)
#room 1
room = [dialogue1 , 10 , 6, 0, 7, "Shiny Sword", "A shiny sword that looks like it could do some damage.", ""]
room_list.append(room)
#room 2
room = ["You are at a pathway which leads back to the cabbin where storm is. Go east to keep going towards Storm. However, there are passeges to the north and west", 6, 5, None, 0, "", "", "WAREWOLF",]
room_list.append(room)
#room 3
room = ["You enter an antique building but quickly realize that everything is very overpriced. The man running the shop is wearing a gold coat and seems to just stare at you. Go north to go back into the city", 0, None, None, None, "money", "Someone seems to have dropped some money", ""]
room_list.append(room)
#room 4
room = ["You are now at an arena where there are 2 wizards fighting using spells. There is a large crown cheering them on. Passages to the north and east", 7, 0, None, None, "broken wand", "a broken wand that has sparks flying out the tip", ""]
room_list.append(room)
#room 5
room = ["You are in an abandoned building where there seems to be a mystical aura. Someone in the distance keeps repeating the words storm. There are passeges to the west and east", None, 8, None, 2, "", "", "BANDIT"]
room_list.append(room)
#room 6
room = ["you are on top of some stairs where you see the entire city. It is lit with torches and has a very high population of ogres and goblins. Passeges to the south or west.", None, None, 2, 1, "", "", ""]
room_list.append(room)
#room 7
room = ["You go into a shop and there seems to be a strong smell of food there. Exit to the south or go east", None, 1, 4, None, "Food", "nothing you have ever seen before but it looks eddible alright", ""]
room_list.append(room)
#room 8
room = ["You are on the pathway towards the cabbin. Go back downt he path towards west, or go back to storm by goin east", None, 9, None, 5, "", "", ""]
room_list.append(room)
#room 9
room = ["storm", None, None, None, None,"","",""]
room_list.append(room)
#room 10
room = ["You are in a police station. You have helped the old man by reporting the goblins. go back south", None, None, 1, None, "", "", ""]
room_list.append(room)






#MENU SCREEN
print1("""╔╦╗╦ ╦╔═╗  ╔═╗╔═╗╔╦╗╦ ╦  ╔═╗╔═╗  ╦  ╦╦╦═╗╔╦╗╦ ╦╔═╗
 ║ ╠═╣║╣   ╠═╝╠═╣ ║ ╠═╣  ║ ║╠╣   ╚╗╔╝║╠╦╝ ║ ║ ║║╣ 
 ╩ ╩ ╩╚═╝  ╩  ╩ ╩ ╩ ╩ ╩  ╚═╝╚     ╚╝ ╩╩╚═ ╩ ╚═╝╚═╝""")#ASCII ART


time.sleep(1) #this makes it so that there is a one second wait before the next code is executed
print()
print()
print("Welcome to path of vertue. press I for instructions. Press P to play. Press E to exit.")
print()

while done1:
  answer = input(">").lower() #all the inputs are in lowercase to avoid case sensitive errors
  if answer == "p":
    break
  elif answer == "e":
    exit()
  elif answer == "i":
    print1("""You will be presented by chioces through the game where you pick your answer.
    Here are some of the controls: [NOTE: that these controls can only be used when the open world aspect of the game is reached, after the intro.]
    H: display current health
    I: display inventory
    M: display morality (how moral your choices have been. the higher the number the better)
    """)
    time.sleep(3)
    print("press e to start playing")
    intro_answer = input(">")
    if intro_answer.lower() == "e":
      break
    else:
      print("please enter e to start playing")
  else:
    print("invalid answer")









#LEVEL ONE, THIS IS THE INTRO OF THE GAME

time.sleep(2)


print1('Storm: Hello traveller, I see that you have ventured into the lands of shadoville, home to the ungodly')
time.sleep(1)
print()
print1("Storm: my name is Storm Shadowwalker, but you can call me storm")
print()
print1("strom: I will you guide through the city, as most travellers can't survive alone")
print()
time.sleep(4)
print1("game: how will you respond?")
print()
print("----------------------------------")
print("a: Why would you be so kind?" )
print()
print("b: I dont need your help")
print()
print("c: ...")
print()
print("d: why am I here?")
print()


while done1:
  ans = input(">").lower()

  if ans == 'a':
    print1("strom: dont question it mortal, I am just here to help and it is in your best interest to accept this offering")
    break #breaks out of the loop

  if ans == "b":
    print1("No need to be rude. I shall leave you alone then. Try ur best to stay alive.")
    print()
    morality = morality - 15 #morality is deducted when an immoral choice is made according to the game
    print1("you: ... what a weird guy. I must find some shelter before it gets dark, he did say this city was dangerous.")
    print()
    print1("On your way to find shelter you are encountered by the {}." .format(name)) #the format function makes it so that the {} are replaced with the order of variables after .format
    print()
    print1("Would you like to fight or run? (f/r)")
    ans3 = input(">")
    while done2:
      if ans3 == "f":
        print1("you tried fighting the beast but ended up dying bc it was too strong and you had no experience in the world and no weapons or items in your inventory.")
        print("""
    _____                         ____                 
    / ____|                       / __ \                
  | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
  | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
    \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                        
                                                        
  """)
        exit()
      elif ans3 == "r":
        print1("you manage to run away into a forest where storm seems to be waiting for you.")
        print()
        print1("storm: I told you it would be hard, now come with me.")
        flag = True
        break     #flag variable is set to true so that if r is pressed it breaks out of both the while loops in order to continue the game
    if flag:
      break

  elif ans == 'c':
    print1("storm: okay lets get moving then it is going to be dark soon and we must find a place to stay the night")
    break
  elif ans == "d":
    print1(" Storm: I am afraid that is something I cannot tell you yet. I know you are curious. come walk with me and and you will find answers in due time.")
    break   
  else:
    print("invalid answer")





print()
print1("Game: as you walk through a forest towards the city with storm, you are encountered by an unconcious body who seems to have a lot of money on them. what will you do?")
print()
time.sleep(2)
print()
print("a: steal the money and leave the body")
print()
print("b: rescue the body")
while done1:

  ans2 = input(">").lower()

  if ans2 == 'a':
    print1("strom: wow, a little greedy are we. my eyes are closed")
    print()
    morality = morality - 30
    statement = "He asks you to use the money you stole to obtain the food, while he takes care of the unconcius body at the cabin" #statement changes for further dialogue dependning on if you saved the body or not
    break

    

  elif ans2 == 'b':
    print1("storm: are you sure you want the weight of another body as you first go into the city?")
    morality = morality + 30
    statement = "he gives you money to buy food since you decided not to rob the unconcius body."
    break

  else:
    print("please pick either a or b")

print()

while done1:
  print1("Game: you get closer and closer to the city and stop and notice an injured baby dragon")
  print()
  print1("would you like to rescue the dragon? (y/n)")
  print()
  ans4 = input(">")
  if ans4 == "y":
    morality = morality + 30
    print1("the dragon flies away happily")
    print()
    help = "dragon"
    dragon = dragon + 1 #variable that keeps traack of if u saved the dragon or not. Used for the seceret ending.
    break
  elif ans4 == "n":
    morality = morality - 30
    print1("you ignore the dragon and keep walking")
    print()
    break
  else:
    print("enter either y or n")

print1("Storm: okay then. Let's go into the city. I have a cabin in the woods where we can stay.")
print()
print("game: it is getting dark as you and storm walk into the city. When you get there storm asks you to go into the city and get food", statement) 
#the statement made here changes based on the choice you made earlier in the game














#lEVEL 2
while done is not True:


#this is the main part of the game and the main game loop

#it it takes the user input and moves them either north west east and south in the rooms that are in the list above. It does this by assigning a number on the list to each direction and changing that room to current room, which is the one that is displayed to the player
  print()
  print1(room_list[current_room][0])
  print()
  print("What direction do you go? (N,S,E,W)")
  direction = input(">")
  if direction.upper() == "N":
    next_room = room_list[current_room][1]
  elif direction.upper() == "E":
    next_room = room_list[current_room][2]
  elif direction.upper() == "S":
    next_room = room_list[current_room][3]
  elif direction.upper() == "W":
    next_room = room_list[current_room][4]
  elif direction.upper() == "I":
    print("Inventory:", inventory)
  elif direction.upper() == "M":
    print("morality = ", morality)
  elif direction.upper() == "H":
    print("health = ", player_health)

  else:
    print()
    print("Please enter either N, S, E or W")
  if next_room == None:
    print()
    print("you can not go this way, pick another passege way")
  else:
    current_room = next_room
  # Check if there is an item in the current room

  if current_room < len(room_list):
    if str(room_list[current_room][5]) != "":
      print1("There is a " + str(room_list[current_room][5]) + " in this area. " + room_list[current_room][6])
      ans = input("Do you want to pick it up? (y/n)")
      if ans.lower() == "y":
    # Add the item to the inventory
        inventory.append(room_list[current_room][5])
        print1("You picked up the " + room_list[current_room][5])
    # Remove the item from the room
        room_list[current_room][5] = ""
        room_list[current_room][6] = ""




  #Same code as the item cheking code.
   



   #check if there is an enemy in the area
  if current_room < len(room_list):
    if str(room_list[current_room][7]) != "":

      #display the enemy you encountered
      print("YOU ARE ENCOUNTERED BY A " + str(room_list[current_room][7]))
      print1("you are fighting the " + str(room_list[current_room][7]))
      print()
      print1("your health is " + str(player_health))
      print()

      #fight code executed until one of the entities is eliminated
      while health > 0 and player_health > 0:
        action = input(" Do you want to attack or defend? (type either \"attack\" or \"defend\") ")
        if action.lower() == "attack":

          #50/50 chance to hit or miss the target
          if random.randint(1, 2) == 1:
            damage = random.randint(10, 27)
            health -= damage
            print("you hit the " + room_list[current_room][7], "for {} damage. it now has {} health" .format(damage, health))
              
              #constant damage done to player if targer missed
          else:
            player_health -= 7
            print("Your attack missed! The {} hits you for 7 damage. Your health is now {}.".format(room_list[current_room][7], player_health))
            
            #defending makes player take 3 damage only no matter what
        elif action.lower() == "defend":
            player_health -= 3
            print1("You defend and take 3 damage. Your health is now {}.".format(player_health))
            #if invalid action entered then player takes 9 damage
        else:
          player_health -= 9
          print("Invalid action! The {} hits you for 9 damage. Your health is now {}.".format(room_list[current_room][7], player_health))
        if player_health <= 0:
          print("You have been defeated")
          print()
          print("""   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  """)
          exit()#game over if player dies
            

        if health <= 0:
          print("you have defeated the encounter! good job.")
          health = 100 #health is restored to 100 if encounter is defeated
          room_list[current_room][7] = ""
          break

  if current_room == 10:
    morality = morality + 20 #if you decide to save the old man from the goblins your morality increases and it repleaces the text for that room.
    room_list[1][0] = "You are in an alleyway where the thankful old man exprsses his gratitude. Passages to the south, east, and west"
  if current_room == 9:
    health = 100
    player_health = 100 #health restored to 100 before boss fight. if you enter room 9 you break out of the open world adventure loop and move on to the boss fight.
    done = True





print1("Game: You make it back to the cabin; However, Storm seems to have left the cabin. There is a note on the floor")
print()
print1("NOTE: What is your name? You don't remember don't you? you dicided to come along with me and venture into the dangerous city, why? why did you trust a stranger? Come to the sacred bridge and defeat the Tauraus demon. The items and weapons you may have picked up from the city will increase the damage you do to that mystical beast. If you are able to do defeat the demon, I will reveal the secrets of your existance to you.")
print("")
print1("you notice a healing potion behind the note that restores your health to 100.")
print()
print()

# Print a welcome message for the boss fight
print1("You make it to the bridge, you take one step in and are faced by the TAURUS DEMON. You are fighting a {} with {} health points.".format(name, health))
time.sleep(3)
print1("the demon aproaches you")
time.sleep(4)
print("""                                                                                        
                                                                                        
                ████                ████████████████                ████                
                ██░░██████      ████░░░░░░░░░░░░░░░░████      ██████░░██                
                ██▓▓░░░░░░██████░░▓▓██░░████████░░██▓▓░░██████░░░░░░▓▓██                
                ██▓▓▓▓██░░░░░░▓▓████████▓▓████▓▓████████▓▓░░░░░░██▓▓▓▓██                
                  ██▓▓▓▓████▓▓░░░░░░▓▓████████████▓▓░░░░░░▓▓████▓▓▓▓██                  
                  ████▓▓▓▓▓▓██████████▓▓▓▓████▓▓▓▓██████████▓▓▓▓▓▓████                  
                  ██▓▓████▓▓▓▓████▓▓░░░░░░░░░░░░░░░░▓▓████▓▓▓▓████▓▓██                  
                    ██▓▓████▓▓██▓▓░░░░░░░░░░░░░░░░░░░░▓▓██▓▓████▓▓██                    
                    ██▓▓▓▓██▓▓██░░░░░░░░░░░░░░░░░░░░░░░░██▓▓██▓▓▓▓██                    
                      ██▓▓▓▓██▓▓░░░░░░▓▓░░░░░░░░▓▓░░░░░░▓▓██▓▓▓▓██                      
                      ██▓▓▓▓██▓▓████░░░░▓▓░░░░▓▓░░░░████▓▓██▓▓▓▓██                      
                      ████▓▓██▓▓▓▓░░██████░░░░██████░░▓▓▓▓██▓▓████                      
                    ██▓▓▓▓██▓▓░░▓▓░░  ▓▓▓▓░░░░▓▓▓▓  ░░▓▓░░▓▓██▓▓▓▓██                    
                    ██▓▓██▓▓▓▓░░░░▓▓▓▓▓▓░░▓▓▓▓░░▓▓▓▓▓▓░░░░▓▓▓▓██▓▓██                    
                      ████▓▓██░░░░░░░░▓▓▓▓░░░░▓▓▓▓░░░░░░░░██▓▓████                      
                      ██▓▓████░░░░░░░░▓▓▓▓░░░░▓▓▓▓░░░░░░▓▓████▓▓██                      
                        ██░░▓▓██░░░░░░▓▓██░░░░██▓▓░░░░░░██▓▓░░██                        
                        ██░░▓▓▓▓▓▓░░░░░░▓▓████▓▓░░░░░░▓▓▓▓▓▓░░██                        
                      ██░░░░░░▓▓▓▓▓▓▓▓░░░░▓▓▓▓░░░░▓▓▓▓▓▓▓▓░░░░░░██                      
                      ██░░░░░░██▓▓░░▓▓████████████▓▓░░▓▓██░░░░░░██                      
                    ██░░░░░░████▓▓░░░░▓▓░░░░░░░░▓▓░░░░▓▓████░░░░░░██                    
                    ████████    ██▓▓░░░░▓▓▓▓▓▓▓▓░░░░▓▓██    ████████                    
                                  ██▓▓▓▓░░░░░░░░▓▓▓▓██                                  
                                    ████▓▓▓▓▓▓▓▓████                                    
                                        ████████                                        
                                                                                        
                                                                                        
""")

print()
print()
print()
time.sleep(4)

print("""____   ___  ____ ____    _____ ___ ____ _   _ _____ 
| __ ) / _ \/ ___/ ___|  |  ___|_ _/ ___| | | |_   _|
|  _ \| | | \___ \___ \  | |_   | | |  _| |_| | | |  
| |_) | |_| |___) |__) | |  _|  | | |_| |  _  | | |  
|____/ \___/|____/____/  |_|   |___\____|_| |_| |_| """)

newdamage = int(len(inventory))*13 #based on the ammount items picked up, the maximum damage u can do is increased
print()
print("Game: the maximum damage that u can do is ", newdamage, "this is owed to how many items you picked up when exploring the city")
# Keep fighting until one of you is defeated
while health > 0 and player_health > 0:
    # Ask the player to attack or defend
    action = input("Do you want to attack or defend? ")
    

    # If the player attacks, there is a 50% chance of hitting the character
    if action.lower() == "attack":
      chance = random.randint(1, 2)
      if chance == 1:
            # If the attack hits, the character's health decreases by a random amount
        damage = random.randint(15, newdamage)
        health -= damage
        print1("You hit the {} for {} damage. Its health is now {}.".format(name, damage, health))
      else:
            # If the attack misses, the character gets a free hit
        player_health -= 15
        print1("Your attack missed! The {} hits you for 15 damage. Your health is now {}.".format(name, player_health))

    # If the player defends, they take half damage from the character's attacks
    elif action.lower() == "defend":
        player_health -= 7.5
        print1("You defend and take 7 damage. Your health is now {}.".format(player_health))

    # If the player inputs an invalid action, they take a lot of damage from the character's attack
    else:
        player_health -= 25
        print("Invalid action! The {} hits you for 25 damage. Your health is now {}.".format(name, player_health))

# outcome of the fight
if health <= 0:
    print1("You have defeated the {}!".format(name))
    print()
else:
    print1("The {} has defeated you. Better luck next time!".format(name))
    print("""    _____                         ____                 
    / ____|                       / __ \                
  | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
  | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
    \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  """)
    exit()

print()
print("------------------------------------------------------------------------")
time.sleep(3)
print1("Game: After after the demon is defeated, it turns into a human. what Would you like to do with the life of the this human who is begging u for mercy?")
time.sleep(1)
print()
print("a: spare his life")
print("b: end his life")
print("c: give him the rest of your healing potion")


#choice presented to save or kill that human that increases or decreases your morality based on your choice
while done1:
  ans6 = input(">").lower()
  if ans6 == "a":
    print1("Game: The human says \"thank you KING STORM\" and flees")
    morality = morality + 30
    break
  if ans6.lower() == "b":
    print1("""Human: WHY WOULD YOU DO THIS KING STORM
    Game: the human dies""")
    morality = morality - 40
    break
    
  if ans6 == "c":
    print1("Game: The human says \"thank you KING STORM\" and flees")
    morality = morality + 50
    break


#ending plot twist of the game. 
print()
time.sleep(3)
print1("Game: You see storm shadow walker approaching you")
print()
time.sleep(4)
print1("""Storm: So you made it huh?
Well I will hold up my end of the deal, and explain why you are here.
""")
print()
time.sleep(2)
print1("you see...")
print()
time.sleep(2)
print1("YOU ARE ME")
print()
time.sleep(2)
print()
print1("""yes, you are The famous Storm shadowwalker, just from the past.
This is why that human just refered to you as \"King storm.\"
In the future you lead your army into an unwinnable battle. Burried with guilt
you use a time jumping spell that was given to you by the dark lord melina.
However, the spell was cursed and ereased your memories in the process.
When you used the spell, the version of you that was burried with guilt still stayed in this world, which is me
the spell had seemed to create an alternate version of me and sent it back in time, that would be you.
Since my attempt to time jump had failed, I started to wonder. Is there still hope?
Maybe I am still a good guy deep down.
So I put you through tests. I presented you with choices where I morally judged you
You really expected a baby dragon to be found that easily in the wild? I planted everything.
""")
print()
time.sleep(6)
print("game: press c to continue")

while done1:
  end_ans = str(input(">").lower())
  if end_ans == "c":
    break
  else:
    print("please enter c to continue")

time.sleep(2)










#Outcome of the game:

#this code checks your morality based on the choices you made throughout the game
#It gives you a different ending based on your morality.


if morality <=100 and morality > 40:
  print1("""I have decided from watching you all this time that you, I mean we, are a terrible human being. Some of your decisions were moral, 
  but most of them were evil, but not evil enough to join me in being a king. which is why I have decided to KILL YOU""")
  print()
  time.sleep(2)
  print1("Game: Storm pulls out his sword and is about to kill you.")
  print()
  time.sleep(3)
  if dragon == 1:
    print1("Storm: WHAT IS THAT")                               #SECRET ENDING IF YOU SAVED THE BABY DRAGON
    time.sleep(2)
    print1("IS THAT THE BABY DRAGON?") 
    print() 
    time.sleep(2)
    print1("Game: since you saved the baby dragon earlier in the game, It came to rescue u from storm")
    print()
    time.sleep(1.5)
    print1("Storm: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    print()
    time.sleep(2)
    print()
    print1("Game: Storm dies")
  else:
    print1("Storm ends your life.")

if morality <= 40:
  print1("""I have decided from watching you all this time that you are downright evil. This is the kind of evil that overpowers all good.
   I shall have you work for me as the heir to the throne. Together we will take over the world.""")
  time.sleep(2)
  print()
  print("storm spares you")
  print()

if morality >= 100:
  print1("""I have decided from watching you all this time that you are actually a good person. You have impressed me,
   and I have realized that there is hope and room for imporvement. We shall work together to better ourselves while running this kingdom.""")
  time.sleep(2)
  print()
  print("storm spares you")




time.sleep(4)
print()
print()

print1("""_____ _            _____           _ 
|_   _| |__   ___  | ____|_ __   __| |
| | | '_ \ / _ \ |  _| | '_ \ / _` |
| | | | | |  __/ | |___| | | | (_| |
|_| |_| |_|\___| |_____|_| |_|\__,_|


Thanks for playing""")
#END OF CODE
time.sleep(3)
    
    
    