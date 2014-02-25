#!usr/bin/python
import hangman

game = new Hangman("test")

while((status = game.isDone()) != 1)
    if(status == -1)
        print "You lose"
        break
    guess = raw_input("Enter your guess: ")
    
    guessStatus = game.makeGuess(guess)
    
    print game.display

    if(guessStatus == -2)
        print "Invalid guess, try again"
    elif(guessStatus == -1)
        print "You have already guessed that"
    elif(guessStatus == 0)
        print "That guess was wrong"
    
    print "\n ---------------------- \n"
