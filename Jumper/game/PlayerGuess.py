from game.word_hider import WordHider

class PlayerGuess:

    #Initial
    def __init__(self):
        self._is_playing = True
        self._wordhider = WordHider() 
        self._word = self._wordhider.get_word()
        self._underscores = ["_"] * len(self._word)
        self._wrongletters = []
        
    #Checks if the letter is in the given word
    def is_letter_in_word(self, letter):
        if letter in self._word:
            return True
        return False

    #Replaces underscores with letters
    def update_underscores(self, letter):

        for i in range(len(self._word)):
            if letter == self._word[i]:
                self._underscores[i] = self._word[i]

    #Gameover Conditions
    def over(self, guessed, underscore, lives):
        if "_" not in underscore:
            self._is_playing = False
            print(f"End of the road!\nYou Won!")
        if guessed.lower() == "quit":
            print("You have ended the game!")
            self._is_playing = False
        if lives == 0:
             print("You died, game over!")
             self._is_playing = False
        return self._is_playing
      
    #Adds incorrect letters to the list
    def update_wrong_letters(self, letter, correct):
        if letter != 'quit':
            if not correct:
                self._wrongletters.append(letter)
        print(f"These are the incorrect guesses: ", ', '.join(self._wrongletters)) 
        
        
        

    

