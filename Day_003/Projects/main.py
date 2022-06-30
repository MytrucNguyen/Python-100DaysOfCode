def game():
    print("Welcome to Treasure Island.")
    direction = input("left or right? ")

    if(direction == 'left'):
        action = input("swim or wait? ")
        if(action == 'wait'):
            print("Which Door...")
            color = input("What color? ")
            if(color == 'red'):
                print("Burned by fire.\nGame Over.")
                retry()
            elif(color == 'blue'):
                print('Eaten by beasts.\nGame Over')
                retry()
            elif(color == 'yellow'):
                print("You win!")
                retry()
            else:
                print('Game over')
                retry()
        else: 
            print("Attacted by trout.\nGame Over.")
            retry()

    else: 
        print('Fall into a hole\nGame Over. ')
        retry()

def retry():
    play_again = input("Do you wanna play again? y or n? ")
    if(play_again == 'y'):
        game()
    elif(play_again == 'n'):
        return  

game()