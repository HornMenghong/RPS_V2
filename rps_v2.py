import random

# running the program
run = True
while run:
    choices = ['rock','paper','scissors']
    computerScore = 0
    userScore = 0
    toWin = 2
    play = True
    lastChoice = "" #last player choice
    lastWin = "" # last computer choice that win
    firstChoice = 0 #checking for computer first choice
    behavior = "" #checking for computer behavior

    print("================================")
    print("Welcome to Rock, Paper, Scissors")
    print("================================")
    print("(1). Start the game")
    print("(2). Quit the game")
    print("(3). Choose the computer move")

    # Check user decisions
    start = input("Choose what to do : ")
    if start == "3":
        print("(A).Default,   (B).Last Player's picked, (C).Last move that win")
        behavior = input("Choose the behavior of the computer: ").lower()
    elif start == "2":
        run = False
    elif start == "1":
        print("Starting the game")

    while play:
        while(computerScore < toWin and userScore < toWin):
            user = input("Input rock, paper, or scissors: ").lower()
            computer = random.choice(choices)
            # Choosing the behavior of bot
            if behavior == "b":
                if (firstChoice != 0):
                    computer =  lastChoice
            elif behavior == "c":
                if (firstChoice != 0):
                    computer =  lastWin
            print(f"The computer chose {computer}")

            # Comparing user and computer's choice
            if(computer == user):
                print("Tie")
            elif(user == 'rock' and (computer == 'scissors' or computer == 'scissor')) or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
                print("You won that hand!")
                userScore += 1
                firstChoice += 1
            else:
                print("You lost that hand!")
                computerScore += 1
                lastWin = computer
                firstChoice += 1
            print("Score is player:", userScore, "computer:", computerScore)
            lastChoice = user

        # Result
        if(userScore == toWin):
            print("You win!")
        else:
            print("The computer won :(")
        
        # Checking for play again
        playAgain = input("Do you want to play again? [Y]es [N]o: ").lower()
        if playAgain == 'y':
            computerScore = 0
            userScore = 0
            firstChoice = 0
        else:
            play = False