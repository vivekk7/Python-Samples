"""Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)"""

choice = 'y'

while (choice == 'y'):
    player1 = raw_input("Player 1: Enter your choice:")
    player2 = raw_input("Player 2: Enter your choice: ")
    if (player1 == "rock" and player2 == "paper"):
        print "Player 2 wins!"
    elif (player1 == "paper" and player2 == "scissors"):
        print "Player 2 wins!"
    elif (player1 == "scissors" and player2 == "rock"):
        print "Player 2 wins!"
    else:
        print "Player 1 wins!"
    choice = raw_input("Do you want to play another game? (y/n): ")
    continue
print "End of the Game"
 

        
