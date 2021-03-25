
def sports_list():
  sports = ["Soccer", "Basketball", "Running"]
  print(sports[0:3])

def sports_type():
  sport=input("Please Select a sport: ")
  if sport == "Basketball":
     shoe_list = ["Lebron 18", "Curry 8", "PG5"]
     print(shoe_list[0:3])
  elif sport == "Soccer":
     shoe_list = ["CR7", "Dragon Predator+", "Predator Mutator+ x Human Race"]
     print(shoe_list[0:3])
  elif sport == "Running":
     shoe_list = ["Ultraboost 21", "Hovr Phantom", "Air Zoom Pegasus 37"]
     print(shoe_list[0:3])
  else:
     print("Unknown")

  choose_basketball_shoe(shoe_list)

def choose_basketball_shoe(shoe_list):
  print(shoe_list)
  basketballshoe=input("Please select your shoe: ")
  if basketballshoe == "Lebron 18":
     print("Lebron 18 is cool")
  elif basketballshoe == "Curry 8":
     print("Curry 8 is cool")
  elif basketballshoe == "PG5":
     print("PG5 is cool")
  else: 
     print("next")
  print("Looking for another shoe?")
  choose_basketball_shoe(shoe_list);


message = "What sport do you play?"
print(message)
sports_list();
sports_type();

import sqlite3

