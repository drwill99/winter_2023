"""
File: text_adventure_game.py
Author: Dallin Williams

Purpose: Use if statements to create a text-based adventure with user inputs.
"""

weapon = False

def strangeCreature():
  actions = ["fight","flee"]
  global weapon
  print("A hooded figure rushes you. You can either FLEE or FIGHT. What would you like to do? ")
  userInput = ""
  while userInput not in actions:
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You kill the hooded figure with the knife you found earlier. You escape through the opening the hooded figure was guarding.")
        print()
        print("YOU ESCAPED")
        quit()
      else:
        print("The figure laughs as he dodges your feeble punch and cuts your stomach open with a knife he was concealing in his robes.")
        print()
        print("YOU DIED")
        quit()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option. ")
      
def showSkeletons():
  directions = ["backward","forward"]
  global weapon
  print("You see human bones cemented into a wall as you walk into the room. You're certain someone is watching you. You can go LEFT, FORWARD, or BACKWARD. ")
  userInput = ""
  while userInput not in directions:
    userInput = input()
    if userInput == "left":
      print("You enter a large room with a stone altar in middle. On the altar is a rusty knife. You pick it up and turn around when...")
      weapon = True
      strangeCreature()
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option. ")
      

def hauntedRoom():
  directions = ["right","left","backwards"]
  print("You can barely hear voices, but you can't make out what they're saying. You can go RIGHT, LEFT, or BACKWARDs. ")
  userInput = ""
  while userInput not in directions:
    userInput = input()
    if userInput == "right":
      print("Multiple men dressed in robes emerge from seemingly solid walls. The first knife enters your ribcage before you can cry out.")
      print()
      print("YOU DIED")
      quit()
    elif userInput == "left":
      print("You see daylight shining through a crack. You slam yourself into the wall until the crack widens and you fall through. You're outside. ")
      print()
      print("YOU ESCAPED")
      quit()
    elif userInput == "backwards":
      introScene()
    else:
      print("Please enter a valid option.")

def cameraScene():
  directions = ["forward","backward"]
  print("You see a broken camera laying on the ground. There are blood spatters on it. Someone did not want to be photographed. You can go FORWARDS or BACKWARDS. ")
  userInput = ""
  while userInput not in directions:
    userInput = input()
    if userInput == "forwards":
      print("You see daylight shining through a crack. You slam yourself into the wall until the crack widens and you fall through. You're outside. ")
      print()
      print("YOU ESCAPED")
      quit()
    elif userInput == "backwards":
      showShadowFigure()
    else:
      print("Please enter a valid option.")
      
def showShadowFigure():
  directions = ["right","backward"]
  print("You see a hooded robed figure approaching, but you don't think he's seen you yet. You can flee RIGHT, LEFT, or BACKWARDS. ")
  userInput = ""
  while userInput not in directions:
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      print("This portion of the tunnel is collapsed, you cannot continue this way. ")
      showShadowFigure()
    elif userInput == "backwards":
      introScene()
    else:
      print("Please enter a valid option.")


def introScene():
  directions = ["left","right","forward"]
  print("You are at a crossroads, and you can choose to go down any of the four hallways. You can go LEFT, RIGHT, FORWARDS, or BACKWARDS. ")
  userInput = ""
  while userInput not in directions:
    userInput = input()
    if userInput == "left":
      showShadowFigure()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "forwards":
      hauntedRoom()
    elif userInput == "backwards":
      print("There is a locked gate blocking your path, you cannot continue this way. ")
      introScene()
    else: 
      print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print()
    print("While investigating rumors of a cult, you decide to explore nearby catacombs where sightings of robed men have been reported.\n")
    print("However, during your exploration, you fall into a hole in the ground.\n")
    print("You find yourself trapped in the catacombs, with the night coming quick.\n")
    print("Let's start with your name: ")
    name = input()
    print(f"Good luck, {name.capitalize()}.")
    introScene()