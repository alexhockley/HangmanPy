#!usr/bin/python
import hangman

game = hangman.Hangman("test",5)

#loops until game is done
while True:
    status = game.isDone() #checks if done
    if (status == 1):
	    print "You win"
	    break
    if(status == -1):
        print "You lose"
        break

    print "".join(game.display)#prints the display list as a string

    guess = raw_input("Enter your guess: ")
    
    guessStatus = game.makeGuess(guess)
    

    if(guessStatus == -2):
        print "Invalid guess, try again"
    elif(guessStatus == -1):
        print "You have already guessed that"
    elif(guessStatus == 0):
        print "That guess was wrong"
    
    print "\n ****************** \n"
 
