class Hangman:	
    
    def __init__ (self, w, mg):
        self.word = w
        self.guesses = []
        self.maxGuesses = mg
        self.availableChars=['a','b','c','d','e','f','g','h',
                             'i','j','k','l','m','n','o','p',
                             'q','r','s','t','u','v','w','x',
                             'y','z']
        self.display = []
        self.generateDisplay()

    def generateDisplay(self):
        for i in range(0,len(self.word)):
            if(self.word[i] != ' '):
                self.display.append( '_')
            else:
                self.display.append( ' ')
       
		
    # -2 for invalid guess, -1 for already guessed, 0 for incorrect guess, 1 for success
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

    #-1 for loss, 0 for still going, 1 for win
    def isDone(self):
        if(len(self.guesses) >= self.maxGuesses):
            return -1
        else:
            if("".join(self.display) == self.word):
                return 1
            return 0

