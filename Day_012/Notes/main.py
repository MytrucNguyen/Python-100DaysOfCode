print("~~~~~~~~~~~~~~~~~~ Day Twelve ~~~~~~~~~~~~~~~~~\n")
# Scope
print("~~~~~~~~~~~~~~~~~~ Example One ~~~~~~~~~~~~~~~~")
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # 2

increase_enemies()
print(f"enemies outside function: {enemies}") # 1
print("~~~~~~~~~~~~~~~~~~ Local Scope ~~~~~~~~~~~~~~~~")
# Exist in function 
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# printing 'potion_strength' outside the scope will cause an error 'not define'

print("~~~~~~~~~~~~~~~~~~ Global Scope ~~~~~~~~~~~~~~~")
# Difference is where you define/create your variable 
player_health = 10

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion()
print(player_health)

print("~~~~~~~~~~~~~ Modifying Global Scope ~~~~~~~~~~")
enemies = 1

def increase_enemies():
    global enemies # But not recommended because it can cause confusion, increasing error 
    # Don't modify global scope
    enemies += 1
    print(f"enemies inside function: {enemies}") 

increase_enemies()
print(f"enemies outside function: {enemies}") 

print("~~~~~~~~~~ Better Modifying Global Scope ~~~~~~")
enemies = 1

def increase_enemies():
    global enemies # But not recommended because it can cause confusion, increasing error 
    # Don't modify global scope
    print(f"enemies inside function: {enemies}") 
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}") 

print("~~~~~~~~~~~~~~~~~ Global Constants ~~~~~~~~~~~~")
# Global constants are variables which you define and never plan on changing 
# E.g.
pi = 3.14159

print("~~~~~~~~~~~~~~~~~~ Block Scope ~~~~~~~~~~~~~~~~")
print("There is none in python")
# Note: if you create a variable within a function, then it's only avaiable within that function
# But if you create a variable within an if block or a while loop or a for loop or anything that has the indentation
# and the colon, then that does NOT count as creating a separate local scope 
