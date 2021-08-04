# This line allows to use external functions from the Math Library
import math

def intro():
  print("Hi I am WALL- E (Waste Allocation Load Lifter - Earth-Class). I am a waste-collector drone programmed to haul the garbage plaguing Earth in the distant future.")
  print()

def dispose_trash():
  # TODO: Print name of program
  
  # This line declares a variable called weight that stores the value that the user gives when ran
  weight = int(input("What is the weight of your trash (in lbs)? "))
  # This code checks if weight is greater than 100lbs.
  if weight >= 100:
    # TODO: Print a message to tell the user than their item is too heavy for WALL-E to decompose!
    print("")
  # This code is ran only if the weight less than 100 lbs
  else:
    # User gets the width of the item
    width = int(input("Please enter the width of the item: "))
    # TODO: gets the height of the item
    
    print("Compacting Trash...")
    # TODO: Compute the dimensions of the trash item
    
    # TODO: Compute the weight of the trash after it is decomposed (see formula in slides)
    
    # TODO: Print a message to the user to let them know that item has been decomposed and what is the final weight of the item after decomposed.
    
def control_system():
  # TODO: print name of program

  c = int(input("How far is the object from the ground?"))
  b = int(input("How far is WALL-E’s eye level to object’s position?"))
  # TODO: compute the distance from WALL-E and item

  # TODO: print out computed distance in a personalized message


def charge_level():
  # Prints name of program
  print("Welcome to the Charge Level Program.")
  # Asks the user for charge level and stores it in a variable called percentage
  percentage = int(input("What is your charge level?"))

  # TODO: Write the conditionals to check the percentage and print out a message:
  #   - if the battery percentage is less than 10, then print "BEEP BEEP! You are low in battery."
  #   - if the battery percentage is more than 90, print "You are fully charged."
  #   - if battery percentage is anything in between 10-90 then print "Battery Level Moderate."
  

if __name__ == "__main__":
  intro()
  choice = str(input("What would you like to do today?"))
  if choice == "check charge":
    charge_level()
  elif choice == "dispose trash":
    dispose_trash()
  elif choice == "get distance":
    control_system()
