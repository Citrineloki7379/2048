import Actions

decision=str(input("Press Y to play 2048 and press N to quit: "))
while decision.upper()=="Y":
    gameboard=Actions.GameGrid()
    play=Actions.GamePlay( gameboard)
    play.initialise()
    print("final score")###
    print(str(play.GameGrid.score))
    decision=str(input("Press Y to play 2048 and press N to quit: "))
#print(str(play.panel.boxes))