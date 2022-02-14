# Date: 1/26/2022
# Name: Yohan Park
# Created: 1/13/2022
# Description: the text-based game that you basically need to search objects inside the room to escape the room.


def handle_input(in_list):
  print("I have split your commands into a list of words.")
  list_length = len(in_list)
  print("You typed", list_length, "words.")
  print("The first word was:", in_list[0])
  if list_length > 1:
    print("The second word was:", in_list[1])
  elif list_length > 2:
    print("the third word was: ", in_list[2])
  
#dictionary statesment to track if boxs are open or locked
box = {"box_open": False, "locker": False}
cabinet = {"cabinet_open": False }
locker = {"locker_open" : False}
pinata = {"pinata_open": False }

inventory = [] #inventory list
box_open = 1 #checking if the wooden box is open to check if they have access to the objects in the box, if box_open = 1, it means it is opened.
current_level = 1


# this function will show the commands that user can use and how to use them.
def execute_help():
  print("Type quit if you wanna leave the game")
  print("Type start if you wanna start the game")
  print("Type help if you want to see the commands again")
  print("Type pick if you want to add item to your inventory\n")
  print("Ex: Pick apple\n")
  print("Type inventory if you want to see inventory")
  print("Type use if you wanna use the item in your inventory")
  print("Ex: use gun human")
  print("Type examine if you want to interact.\n")
  print("Ex: examine apple\n")
  print("Type inspect to check what objects are inside the room.")
  print("Type Restart to restart")
  print("By the way, you are not suppoed to use spacebar for the objects\n")
  print("Ex: use key bluedoor\n")

#this function will restart the program 
def restart():
    inventory.clear()
    #set all the statemeans as false to reset completely
    box["box_open"] = False
    cabinet["box_open"] = False
    locker["box_open"] = False
    execute_start()

#this functtion will start the program and explain basic story of the life
def execute_start():
  print("i woke up in strange place")
  print("where am i..?\n")
  print("you can see a window, post-it note, a locker, cabinet, a box on the desk and door with plates on the left.")
  print("you see the letters in the room\n")
  print("< welcome! my friend, You'd better escape before it rains.")
  print("since this room will be flood. > ")
  print("\n")
  print("< P.S. try to open the locker >")

#examine function
def execute_examine(object):
  #make it as global variable to control the roomlevel in every subprogram
  global current_level 

#you can only examine these objects if current level is 1(first room)
  if current_level == 1:
    if object == "post-itnote":
      print("it says")
      print("< dont forget to take your item! >")
    elif object == "paper" and box["box_open"]:
      print("< 2+2*2^2  = ? >")
      print("1) 4 2) 5 \n3) 2 4) 10")
      print("< What walk on 4 legs in the morning 2 in the afternoon and 3 at night? >")
      print("1) Dog 2) Human \n3) Cat 4) Piñata")
      print("< 3+3*3+3-3 = ? >")
      print("1) 15 2) 6 \n3) 10 4) 12")
      print("hint: A D D ")
      
    elif object == "keycard" and locker["locker_open"]:#only if locker is opened  
      print("it's a blue keycard, where can i use this to?")
    elif object == "locker":
      if locker["locker_open"]:
        print("it's opened locker")
      else:
        print("Stained locker, it is locked.")
    elif object == "box":
      #if the answer is string "y" (either upper/lower) it'll set statement box_open as true (box_open)
      answer = str(input("it's a wooden box, should i open? Y/N: "))
      if answer.lower() == "y": 
        print("there is a gun inside the box and small paper")
        box["box_open"] = True #set box_open statement as open to give the user access to get/examine item inside
    elif object == "window":
      print("It is a window of iron bars through which the wind flows.")
    elif object == "gun" and box["box_open"]: #only if the box is opened
      print("it's a revovle, where can i use this to?")
    elif object == "key" and cabinet["cabinet_open"]: #only if cabinet is opened
      print("it's a golden key.")
      print("where can i use this to?")
    elif object == "cabinet":
      execute_cabinet() #execute cabinet function
    else:
      print("you can't do that")
 #only if current_level is 2(only can be used when the user is in second room)
  elif current_level == 2:
    if object == "bluedoor":
      print("it's a blue door. it says thursday on top of the door")
    elif object == "reddoor":
      print("it's a red door. it says sunday on top of the door")
    elif object == "pinata":
      print("it's on the ceiling, looks like there is something inside..")
    elif object == "paper" and pinata["pinata_open"]: #only if pinata is opened
      print("it says 'If yesterday was tomorrow, then today will be Saturday.. wait.. what day is today..?'")
    elif object == "goldenkey" and pinata["pinata_open"]: #only if pinata is opened
      print("it's a golden key.. it says 'you got one chance' on the key.")
      
def second_room():
  print("it's an.. another room..??\n")
  print("there is a Piñata on the top of the room.\n")
  print("why is there a Piñata..?\n")
  print("and i see red door and blue door.\n")
  print("type < inspect > if you want to know what objects are here\n")

#function to pick item 
def execute_pick(object):
  if current_level == 1:
    if object == "gun" and box["box_open"]: #only if when box_open is True (only when the box is opened)
      print("it's a six shooter, Bodeo Model made in 1889")
      inventory.append(object) #add to list inventory
      print("you have picked up the gun")
    elif object == "key" and cabinet["cabinet_open"]: #only if when cabinet is True (only when the cabinet is opened)
      print("it's a key, no idea where i could use this key to")
      inventory.append(object)
      print("you have picked up the key")
    elif object == "keycard" and locker["locker_open"]:
      inventory.append(object) #add to list inventory
      print("where can i use this to?")
      print("you have picked up the keycard")
    else:
      print("you cant do that")
  elif current_level == 2:
    if object == "pinata":
      print("it's too high.. wish if i could break that pinata..")
    elif object == "paper" and pinata["pinata_open"]: #only when pinata is open
      print("i think i should examine this.")

    elif object == "goldenkey" and pinata["pinata_open"]: #only when pinata is open
      inventory.append(object) #add to list inventory
      print("it's a golden key.. it says 'you got one chance' on the key.")
      print("you have picked up the goldenkey")
  
#use function 
def use_item(object,target):
  global current_level
  if current_level == 1:
    if object == "gun" and target == "window":
      print("you shooted the window, but of course you can not break the iron")
      #if this code executes, it removes the item from inventory
    elif object == "key" and target == "locker":
      print("Locker opens!")
      print("There is a keycard inside.")
      inventory.remove("key")
      locker["locker_open"] = True  #set locker_open statement as open to give the user access to get/examine item inside

    elif object == "keycard" and target == "plate": 
      print("Door opens!")
      inventory.remove("keycard") #if this code executes, it removes the item from inventory
      current_level = 2 #go to second room
      second_room()  #run second_room() function.
    else:
      print("you can't do that")
    #only if current_level is 2(only can be used when the user is in second room)
  elif current_level == 2:
    if object == "gun" and target == "pinata":
      print('nice shot!, pinata broke! i see a paper inside.')
      pinata["pinata_open"] = True #set pinata_open statement as open to give the user access to get/examine item inside
    elif object == "goldenkey" and target == "bluedoor": #lose ending
      print("there is a small room inside.. ")
      print("you walked in to the room to check what is inside.")
      print("as soon as you walked in, door locks and you see a paper on the ground")
      print("< you've lost your game, you have nothing to do except drowning slowly!")
      print("wait, nevermind! good news, you had the gun!\n")
      lost()
    elif object == "goldenkey" and target == "reddoor": #win ending
      print("finally.. it's outside..!")
      print("you see a card with a letter outside..")
      print("< sorry for testing you, i wanted to check if you deserve my legacy..")
      print("it's a card with a billion dollar, congrat..")
      print("\nfrom your grandfather.")
      won()

#this function will be executed if you win
def won():
  print("you won")
  if score <= 20: #if score is less than 20(total number of execution examine/use/pick)
    print("Congratulation! you've achieve S Rank!") 
  elif score <= 30: 
    print("Congratulation! you've achieve A Rank!") 
  elif score <= 35: 
    print("Congratulation! you've achieve B Rank!") 
  elif score <= 40: 
    print("Congratulation! you've achieve C Rank!") 
  elif score <= 45: 
    print("Congratulation! you've achieve D Rank!") 
  print("would you like to try again?") 
  answer = str(input("Y/N: ")) 
  if answer.lower() == "y": 
    restart() 

def lost():
  print("\nyou lost!")
  print("\nwould you like to try again?")
  answer = str(input("Y/N: "))
  if answer.lower() == "y": #if the user type "y", restart function executes
    restart ()


def execute_use(object,target):
  if object in inventory: #execute use_item subprogram only if object is in list inventory
    use_item(object,target)  #use augment as target and object. (in_list 1 and 2)
  else:
    print("you do not have the item, pick up the item first!")

#inventory 
def execute_inventory():
  print(inventory)

#cabinet function
def execute_cabinet():
  print("there is 40 cabinets, which one are you going to search? ")
  #if user input is 10, print "key inside" and set cabinet_open as True
  num_cabinet = int(input("type number between 1 ~ 40: ")) 
  if num_cabinet == 10: 
    print("there is a key inside the cabinet")
    cabinet["cabinet_open"] = True
  else:
    print("it's empty inside") #if not, print this sentence

#it shows what objects are inside the level you are on.
def execute_inspect():
  if current_level == 1:  #if the user is in the first room.
    print("you can see a small window, a locker, cabinet, a wooden box on the desk and iron door with the plate on the left.")
  elif current_level == 2: #if the user is in the second room.
    print("there is a Piñata, red door and blue door.")
    
#checking inputs
def input_loop():
  global score  #global variable to calculate the rank to display when you win
  score = 0
  while True:
    in_list = input("> ").lower().strip().split()
    if in_list[0] == "quit":
      break
    elif in_list[0] == "start":
      execute_start()
    elif in_list[0] == "help":
      execute_help()
    elif in_list[0] == "pick":
      if len(in_list) >= 2: #if the input has more than 2 words, it'll not be executed. (to prevent error)
        execute_examine(in_list[1])
        score += 1 #add score to count rank next time
      else:
        print("you have to put second word!")
        print("Ex: pick apple")
    elif in_list[0] == "inventory":
      execute_inventory()
    elif in_list[0] == "start": 
      execute_start()
    elif in_list[0] == "use": 
      if len(in_list) >= 3: #if the input has more than 3 words, it'll not be executed. (to prevent error)
        execute_use(in_list[1],in_list[2])
        score += 1
      else:
        print("you have to follow the format")
        print("Ex: Use key closet")
    elif in_list[0] == "examine":
      if len(in_list) >= 2: #if the input has more than 2 words, it'll not be executed. (to prevent error)
        execute_examine(in_list[1])
        score += 1
      else:
        print("you have to put second word!")
        print("Ex: Examine desk")
    elif in_list[0] == "inspect":
      execute_inspect()
    elif in_list[0] == "restart":
      restart()
    else:
      handle_input(in_list)
    print()

#main code
print("Welcome to <Escape>!")
print("type help for command list.")
print("type tutorial for basic elements for the game.")
input_loop()
