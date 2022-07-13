# Class is a blueprint
# class NameOfCClass:
# Naming = PascalCase 
# snack_case everywhere else
# Attribute is a variable that's associated with an object

# Not the best method
class User:
    pass

user_1 = User()
user_1.id = "001"
user_1.username = "u1"

print(user_1.username)

# Better method
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
    
    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User("001", "u1")
user_2 = User("002", "u2")

print(user_1.username)
print(user_1.follower)

user_1.follow(user_2)
print(f"{user_1.username} has {user_1.follower} followers")
print(f"{user_1.username} follows {user_1.following} account")

print(f"{user_2.username} follows {user_2.following} account")
print(f"{user_2.username} has {user_2.follower} follower")