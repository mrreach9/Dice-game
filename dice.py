def dice():
    import random as r
    dice1 = [1,2,3,4,5,6]
    player1 = r.choice(dice1)
    player2 = r.choice(dice1)
    key = str(input("Enter r to start: "))
    print("player1: ",player1)
    print("player2: ",player2)
    if(key=="r"):
        if(player1>player2):
            print("Player1 wins.")
            key2 = str(input("Play again? [yes]/[no]"))
            if(key2=="yes"):
                dice()
            else:
                print("Bye!")
        elif(player1<player2):
            print("player 2 wins.")
            key2 = str(input("play again?[yes]/[no]"))
            if(key2=="yes"):
                dice()
            else:
                print("Bye!")
            
        else:
            print("Tie")
            key2 = str(input("Play again?[yes]/[no]"))
            if(key2=="yes"):
                dice2()
            else:
                print("Bye!")
    else:
        print("You entered the wrong key.")
        dice()
dice()
        
