import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1

    while rounds !=10:
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll: " + str(player1))
        print("Player 2 Roll: " + str(player2))

        if player1 == player2:
                print("DRAW!\n")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("Player 1 wins the round!\n")
        else:
            player2wins = player2wins + 1
            print("Player 2 wins the round!\n")

        rounds = rounds + 1

    if player1wins == player2wins:
            print("DRAW\n")
    elif player1wins > player2wins:
            print("Player 1 wins the game\n")
    else:
            print("Player 2 wins the game!\n")

def dice_roll():
    diceRoll = random.randint (1,6)
    return diceRoll

main()