#TODO: import your games library into this folder
import games

#TODO: create a list of available games
available_games = ["EO2", "GTN"]
#TODO: create a function to display the list of available available games
    #HINT: use a loop
def display_games():
    for g in available_games:
        print(g)
#TODO: write a function to evaluate the player's choice of game
def eval_choice():
    player_choice = input("What game do you want to play?")
    if player_choice == "EO2":
        games.evenorodd()
    if player_choice == "GTN":
        games.guess_the_num()


    #TODO: ask the player which game they wish to play
    #TODO: run that particular game by calling the respective game with the dot notation

#TODO: define a main function to run the games
def main():
    repeat = True
    while repeat:
        display_games()
        eval_choice()
        play_again = input("Do you want to play again? (Y/N) ")
        if play_again == "Y":
            repeat = True
        else:
            repeat = False

if __name__ == "__main__":
    main()



#TODO: call the main function appropriately
