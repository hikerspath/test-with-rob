#class player:
#    v1 = input("player name ")
#    password = "dirty toad"
#    print("welcome", v1)
#    print()
#    password = input("Enter Password")
#    if password == "dirty toad":
#      print("password successful")
#      print()
#    else:
#      print("wrong password")

# https://github.com/J16N/getpass3/blob/master/getpass3.py

# My User
def user:
  player = input("Who are you: ")
  print("Welcome " +player+ "\n")
  return player

# My Password
def auth(person):
  import getpass
  passwd = False
  while passwd == False:
    myPasswd = getpass.getpass("Password: ")
    if myPasswd == "password123":
      print("Finally " +person+ "!")
      passwd = True
    else:
      print("Try again...")

# Default Runtime
user()
auth(player)
