from tictactoe import*

def lobby():
    print("1. 3*3")
    print("2. 5*5")
    lobby1 = input()
    if (lobby1 == "1"):
        game_start()
    else:
        print("나중에 오세요")
            
lobby()



