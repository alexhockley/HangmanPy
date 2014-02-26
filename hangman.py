#Hangman - General hangman functionality class
#Alex Hockley
#Created: Feb 24 2014
#Modified: Feb 25 2014
class Hangman:	
    
    def __init__ (self, w, mg):
        self.word = w #word to guess
        self.guesses = [] #list of guesses
        self.maxGuesses = mg #max num of guesses
        self.availableChars=['a','b','c','d','e','f','g','h', #available guesses
                             'i','j','k','l','m','n','o','p',
                             'q','r','s','t','u','v','w','x',
                             'y','z']
        self.display = [] #display list (string)
        self.generateDisplay() #create the display list

	#Purpose: Generates the display string for the hangman game
    #Returns: Nothing, but self.display is generated	
    def generateDisplay(self):
        for i in range(0,len(self.word)):
            if(self.word[i] != ' '):
                self.display.append( '_')
            else:
                self.display.append( ' ')
       
	#Purpose: Logic for making a guess and modifies the display string	
    #Returns: -2 for invalid guess, -1 for already guessed, 0 for incorrect guess, 1 for success
    def makeGuess(self,guess):
        if(len(guess) > 1):
            return -2
        if(guess not in self.availableChars):
            return -2
        if(guess in self.guesses):
            return -1
        if(guess in self.word):
            for i in range(0,len(self.word)):
                if(self.word[i] == guess):
                    self.display[i] = guess
            self.guesses.append(guess)
            return 1
        else:
            self.guesses.append(guess)
            return 0

	#Purpose: Checks if the game is complete
    #Returns: -1 for loss, 0 for still going, 1 for win
    def isDone(self):
        if(len(self.guesses) >= self.maxGuesses):
            return -1
        else:
            if("".join(self.display) == self.word):
                return 1
            return 0

