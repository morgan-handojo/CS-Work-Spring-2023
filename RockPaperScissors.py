# File: Project1.py

# Course Name: CS303E
#
# Date: 2/24/2023
# Description of Program: rock paper scissors game using multiple functions
import random

# makes random machine choice
def machinePlay():
    """The machine chooses one of the three moves randomly."""
    play = random.choice(['1', '2', '3'])
    return play

# determines who wins the round, play1 = user input, play2 = machine
def defeats(play1, play2):
    if play1 == '1':
        if play2 == '2':
            return False
        else:
            return True

    elif play1 == '2':
        if play2 == '1':
            return True
        else:
            return False

    else:
        if play2 == '1':
            return False
        else:
            return True

# changes output for printing match result statements
def playName(what):
    if what == '1':
        return 'rock'
    elif what == '2':
        return 'paper'
    else:
        return 'scissors'

# prints final results
def printStats(total, userwin, userloss, draws):
    if total == 0:
        return "No games were completed."
    else:
        winperc = str(format((userwin / total) * 100, ".1f"))
        lossperc = str(format((userloss / total) * 100, ".1f"))
        drawperc = str(format((draws / total) * 100, ".1f"))

        return "Game statistics: " + "\n    Games played: " + str(total) + "\n    You won:      " + str(userwin) + " (" + winperc + "%)\n" \
        + "    You lost:     " + str(userloss) + " (" + lossperc + "%)" + "\n    No winner:    " + str(draws) + " (" + drawperc + "%)"



def main():
    WELCOME_MESSAGE = "Welcome to a game of Rock, Paper, Scissors!\n"
    GOODBYE_MESSAGE = "Thanks for playing. Goodbye!"


    total = 0
    userwin = 0
    userloss = 0
    draws = 0

    print(WELCOME_MESSAGE)

    usermove = input("Choose your play:\n    Enter 1 for rock;\n    Enter 2 for paper;\n    Enter 3 for scissors;\n    Enter 4 to exit: ")

    while usermove:
        # exit
        if usermove == '4':
            print(printStats(total, userwin, userloss, draws))
            print(GOODBYE_MESSAGE)
            break

        # user has a play
        elif usermove == '1' or usermove == '2' or usermove == '3':
            total += 1
            machplay = machinePlay()

            # if draw
            if usermove == machplay:
                draws += 1
                print("You played ", playName(usermove), "; your opponent played ", playName(machplay), "\nThere's no winner. Try again!", sep="")
                print()

            # if not draw
            else:
                result = defeats(usermove, machplay)

                # if player win
                if result:
                    userwin += 1
                    print("You played ", playName(usermove), "; your opponent played ", playName(machplay),
                          "\nCongratulations, you won!", sep="")
                    print()

                # if player loss
                else:
                    userloss += 1
                    print("You played ", playName(usermove), "; your opponent played ", playName(machplay),
                          "\nSorry, you lost!", sep="")
                    print()

            # new user input regardless of draw, win, loss
            usermove = input(
                "Choose your play:\n    Enter 1 for rock;\n    Enter 2 for paper;\n    Enter 3 for scissors;\n    Enter 4 to exit: ")

            # filters illegal input and asks for new one
        else:
            print("Illegal play entered. Try again!")
            usermove = input(
                "Choose your play:\n    Enter 1 for rock;\n    Enter 2 for paper;\n    Enter 3 for scissors;\n    Enter 4 to exit: ")


main()
