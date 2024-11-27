import random

from art import logo, vs
from game_data import data

print(logo)

# nameofkey3 = randomitemfromthelist3.get('name')
# followercountofkey3 = randomitemfromthelist3.get('follower_count')
# descriptionofkey3 = randomitemfromthelist3.get('description')
# countryofkey3 = randomitemfromthelist3.get('country')

a = 0

import os 

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear') 

while 1<2:

  randomitemfromthelist1 = random.choice(data)

  while 1<2:
    randomitemfromthelist2 = random.choice(data)
    if randomitemfromthelist2 != randomitemfromthelist1:
      break

  while 1<2:
    randomitemfromthelist3 = random.choice(data)
    if randomitemfromthelist3 != randomitemfromthelist2 and randomitemfromthelist3 != randomitemfromthelist1:
      break

  nameofkey1 = randomitemfromthelist1.get('name')
  followercountofkey1 = randomitemfromthelist1.get('follower_count')
  descriptionofkey1 = randomitemfromthelist1.get('description')
  countryofkey1 = randomitemfromthelist1.get('country')

  nameofkey2 = randomitemfromthelist2.get('name')
  followercountofkey2 = randomitemfromthelist2.get('follower_count')
  descriptionofkey2 = randomitemfromthelist2.get('description')
  countryofkey2 = randomitemfromthelist2.get('country')
  
  print("Compare A: " + nameofkey1 + ", a " + descriptionofkey1 + ", from " + countryofkey1 + ".")
  print(vs)
  print("Against B: " + nameofkey2 + ", a " + descriptionofkey2 + ", from " + countryofkey2 + ".")
  print("Who has more followers? Type 'A' or 'B': ")
  batdau = input()
  if batdau == "A" or batdau == "a":    
    if followercountofkey1 > followercountofkey2:
      a = a + 1
      print("You're right! Current score: " + str(a))
      print("let's continue!")
      print(" Press any button to continue! ")
      input()
      clear_screen() 
    else:
      print("Sorry, that's wrong. Final score: " + str(a))
      print("Please start the game again if you still wanna play!")
      print("  ")
      break
  elif batdau == "B" or batdau == "b":
    if followercountofkey2 > followercountofkey1:
      a = a + 1
      print("You're right! Current score: " + str(a))
      print("let's continue!")
      print(" Press any button to continue! ")
      input()
      clear_screen() 
    else:
      print("Sorry, that's wrong. Final score: " + str(a))
      print("Please start the game again if you still wanna play!")
      print("  ")
      break
  else:
    print("please (press any button)) re-entry!!")
    input()
    clear_screen() 
