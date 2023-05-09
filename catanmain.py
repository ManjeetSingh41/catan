

# Settlers of Catan

# Define global variables
player1Name = ""
player2Name = ""
player3Name = ""
player4Name = ""
player1Score = 0
player2Score = 0
player3Score = 0
player4Score = 0

# Ask for the names of the 4 players
player1Name = input("Player 1, please enter your name: ")
player2Name = input("Player 2, please enter your name: ")
player3Name = input("Player 3, please enter your name: ")
player4Name = input("Player 4, please enter your name: ")

# Place the 19 Hex tiles on the board
# Place the 6 Harbor tiles on the board

# Place 2 settlements and 1 road per player
player1Settlement1 = input(player1Name + ", please place your first settlement: ")
player1Road1 = input(player1Name + ", please place your first road: ")
player2Settlement1 = input(player2Name + ", please place your first settlement: ")
player2Road1 = input(player2Name + ", please place your first road: ")
player3Settlement1 = input(player3Name + ", please place your first settlement: ")
player3Road1 = input(player3Name + ", please place your first road: ")
player4Settlement1 = input(player4Name + ", please place your first settlement: ")
player4Road1 = input(player4Name + ", please place your first road: ")

player1Settlement2 = input(player1Name + ", please place your second settlement: ")
player1Road2 = input(player1Name + ", please place your second road: ")
player2Settlement2 = input(player2Name + ", please place your second settlement: ")
player2Road2 = input(player2Name + ", please place your second road: ")
player3Settlement2 = input(player3Name + ", please place your second settlement: ")
player3Road2 = input(player3Name + ", please place your second road: ")
player4Settlement2 = input(player4Name + ", please place your second settlement: ")
player4Road2 = input(player4Name + ", please place your second road: ")

# Roll the dice
while player1Score < 10 and player2Score < 10 and player3Score < 10 and player4Score < 10:
    diceRoll = int(input("Player 1, please roll the dice: "))

    # Collect resources
    if diceRoll == 1:
        player1Score += 1
        print(player1Name + " collects 1 brick, 1 lumber and 1 wool.")
    elif diceRoll == 2:
        player1Score += 1
        print(player1Name + " collects 1 ore and 1 wheat.")
    elif diceRoll == 3:
        player1Score += 1
        print(player1Name + " collects 1 wool and 1 ore.")
    elif diceRoll == 4:
        player1Score += 1
        print(player1Name + " collects 1 brick and 1 lumber.")
    elif diceRoll == 5:
        player1Score += 1
        print(player1Name + " collects 1 grain and 1 brick.")
    elif diceRoll == 6:
        player1Score += 1
        print(player1Name + " collects 1 lumber and 1 grain.")

    # Trade resources
    tradeInput = input("Do you want to trade resources? (yes/no): ")
    if tradeInput == "yes":
        tradeInput2 = input("What do you want to trade? (brick/lumber/wool/ore/grain): ")
        if tradeInput2 == "brick":
            print(player1Name + " trades 1 brick and 1 wool for 1 lumber.")
        elif tradeInput2 == "lumber":
            print(player1Name + " trades 1 ore and 1 wheat for 1 brick.")
        elif tradeInput2 == "wool":
            print(player1Name + " trades 1 brick and 1 lumber for 1 ore.")
        elif tradeInput2 == "ore":
            print(player1Name + " trades 1 wool and 1 grain for 1 wheat.")
        elif tradeInput2 == "grain":
            print(player1Name + " trades 1 lumber and 1 wool for 1 grain.")

    # Build
    buildInput = input("Do you want to build a settlement or a road? (settlement/road): ")
    if buildInput == "settlement":
        print(player1Name + " builds a settlement on the Hex tile with the number " + str(diceRoll) + ".")
    elif buildInput == "road":
        print(player1Name + " builds a road on the Hex tile with the number " + str(diceRoll) + ".")

    # Player 2 turn
    diceRoll2 = int(input("Player 2, please roll the dice: "))

    # Collect resources
    if diceRoll2 == 1:
        player2Score += 1
        print(player2Name + " collects 1 brick, 1 lumber and 1 wool.")
    elif diceRoll2 == 2:
        player2Score += 1
        print(player2Name + " collects 1 ore and 1 wheat.")
    elif diceRoll2 == 3:
        player2Score += 1
        print(player2Name + " collects 1 wool and 1 ore.")
    elif diceRoll2 == 4:
        player2Score += 1
        print(player2Name + " collects 1 brick and 1 lumber.")
    elif diceRoll2 == 5:
        player2Score += 1
        print(player2Name + " collects 1 grain and 1 brick.")
    elif diceRoll2 == 6:
        player2Score += 1
        print(player2Name + " collects 1 lumber and 1 grain.")

    # Trade resources
    tradeInput = input("Do you want to trade resources? (yes/no): ")
    if tradeInput == "yes":
        tradeInput2 = input("What do you want to trade? (brick/lumber/wool/ore/grain): ")
        if tradeInput2 == "brick":
            print(player2Name + " trades 1 brick and 1 wool for 1 lumber.")
        elif tradeInput2 == "lumber":
            print(player2Name + " trades 1 ore and 1 wheat for 1 brick.")
        elif tradeInput2 == "wool":
            print(player2Name + " trades 1 brick and 1 lumber for 1 ore.")
        elif tradeInput2 == "ore":
            print(player2Name + " trades 1 wool and 1 grain for 1 wheat.")
        elif tradeInput2 == "grain":
            print(player2Name + " trades 1 lumber and 1 wool for 1 grain.")

    # Build
    buildInput = input("Do you want to build a settlement or a road? (settlement/road): ")
    if buildInput == "settlement":
        print(player2Name + " builds a settlement on the Hex tile with the number " + str(diceRoll2) + ".")
    elif buildInput == "road":
        print(player2Name + " builds a road on the Hex tile with the number " + str(diceRoll2) + ".")

    # Player 3 turn
    diceRoll3 = int(input("Player 3, please roll the dice: "))

    # Collect resources
    if diceRoll3 == 1:
        player3Score += 1
        print(player3Name + " collects 1 brick, 1 lumber and 1 wool.")
    elif diceRoll3 == 2:
        player3Score += 1
        print(player3Name + " collects 1 ore and 1 wheat.")
    elif diceRoll3 == 3:
        player3Score += 1
        print(player3Name + " collects 1 wool and 1 ore.")
    elif diceRoll3 == 4:
        player3Score += 1
        print(player3Name + " collects 1 brick and 1 lumber.")
    elif diceRoll3 == 5:
        player3Score += 1
        print(player3Name + " collects 1 grain and 1 brick.")
    elif diceRoll3 == 6:
        player3Score += 1
        print(player3Name + " collects 1 lumber and 1 grain.")

    # Trade resources
    tradeInput = input("Do you want to trade resources? (yes/no): ")
    if tradeInput == "yes":
        tradeInput2 = input("What do you want to trade? (brick/lumber/wool/ore/grain): ")
        if tradeInput2 == "brick":
            print(player3Name + " trades 1 brick and 1 wool for 1 lumber.")
        elif tradeInput2 == "lumber":
            print(player3Name + " trades 1 ore and 1 wheat for 1 brick.")
        elif tradeInput2 == "wool":
            print(player3Name + " trades 1 brick and 1 lumber for 1 ore.")
        elif tradeInput2 == "ore":
            print(player3Name + " trades 1 wool and 1 grain for 1 wheat.")
        elif tradeInput2 == "grain":
            print(player3Name + " trades 1 lumber and 1 wool for 1 grain.")

    # Build
    buildInput = input("Do you want to build a settlement or a road? (settlement/road): ")
    if buildInput == "settlement":
        print(player3Name + " builds a settlement on the Hex tile with the number " + str(diceRoll3) + ".")
    elif buildInput == "road":
        print(player3Name + " builds a road on the Hex tile with the number " + str(diceRoll3) + ".")

    # Player 4 turn
    diceRoll4 = int(input("Player 4, please roll the dice: "))

    # Collect resources
    if diceRoll4 == 1:
        player4Score += 1
        print(player4Name + " collects 1 brick, 1 lumber and 1 wool.")
    elif diceRoll4 == 2:
        player4Score += 1
        print(player4Name + " collects 1 ore and 1 wheat.")
    elif diceRoll4 == 3:
        player4Score += 1
        print(player4Name + " collects 1 wool and 1 ore.")
    elif diceRoll4 == 4:
        player4Score += 1
        print(player4Name + " collects 1 brick and 1 lumber.")
    elif diceRoll4 == 5:
        player4Score += 1
        print(player4Name + " collects 1 grain and 1 brick.")
    elif diceRoll4 == 6:
        player4Score += 1
        print(player4Name + " collects 1 lumber and 1 grain.")

    # Trade resources
    tradeInput = input("Do you want to trade resources? (yes/no): ")
    if tradeInput == "yes":
        tradeInput2 = input("What do you want to trade? (brick/lumber/wool/ore/grain): ")
        if tradeInput2 == "brick":
            print(player4Name + " trades 1 brick and 1 wool for 1 lumber.")
        elif tradeInput2 == "lumber":
            print(player4Name + " trades 1 ore and 1 wheat for 1 brick.")
        elif tradeInput2 == "wool":
            print(player4Name + " trades 1 brick and 1 lumber for 1 ore.")
        elif tradeInput2 == "ore":
            print(player4Name + " trades 1 wool and 1 grain for 1 wheat.")
        elif tradeInput2 == "grain":
            print(player4Name + " trades 1 lumber and 1 wool for 1 grain.")

    # Build
    buildInput = input("Do you want to build a settlement or a road? (settlement/road): ")
    if buildInput == "settlement":
        print(player4Name + " builds a settlement on the Hex tile with the number " + str(diceRoll4) + ".")
    elif buildInput == "road":
        print(player4Name + " builds a road on the Hex tile with the number " + str(diceRoll4) + ".")

# Determine the winner
if player1Score == 10:
    print(player1Name + " has earned 10 victory points and wins the game!")
elif player2Score == 10:
    print(player2Name + " has earned 10 victory points and wins the game!")
elif player3Score == 10:
    print(player3Name + " has earned 10 victory points and wins the game!")
elif player4Score == 10:
    print(player4Name + " has earned 10 victory points and wins the game!")
