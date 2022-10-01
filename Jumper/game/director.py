from cgi import test
from re import L
from game.word_hider import WordHider
from game.PlayerGuess import PlayerGuess
from game.parachute import Parachute

class Director:

    #initial
    def __init__(self):
        self._wordhider = WordHider()
        self._playerguess = PlayerGuess()
        self._parachute = Parachute()
        self._is_playing = True
        self._guessed_letter = []
        self._correct_letter = True
        
    #Game Loop
    def start_game(self):
        while self._is_playing == True:
            self._get_inputs()
            self._do_updates()
            self._isgameover()
            self._do_outputs()

    #Gets the user input and checks if it's valid
    def _get_inputs(self):
        repeat = True
        word = self._wordhider.get_word
        self._parachute.drawParachute()
        while repeat:
            self._guessed_letter = input(f"\nSelect a letter (type 'quit' to end the game): ").lower()
            if self._guessed_letter in self._playerguess._wrongletters:
                print("You have already guessed that letter. Please try again.")
                continue
            if self._guessed_letter in self._playerguess._underscores:
                print("You have already guessed that letter. Please try again.")
                continue
            if self._guessed_letter.isnumeric():
                print("Please guess a letter or type 'quit' to end the game.")
                continue
            if self._guessed_letter == 'quit':
                break
            if len(self._guessed_letter) > 1:
                print("Please guess a letter or type 'quit' to end the game.")
            else:
                repeat = False
        self._correct_letter = self._playerguess.is_letter_in_word(self._guessed_letter)

    #Gamestate Updates
    def _do_updates(self):
        self._playerguess.update_underscores(self._guessed_letter)
        self._playerguess.update_wrong_letters(self._guessed_letter, self._correct_letter)
        self._parachute.updateLives(self._correct_letter)
    
    #Checks if a game ending condition is met
    def _isgameover(self):
        self._is_playing = self._playerguess.over(self._guessed_letter, self._playerguess._underscores, self._parachute.lives)


    #Console outputs
    def _do_outputs(self):

        print(f"These are the correct guesses so far: ", ' '.join(self._playerguess._underscores)) 
        if self._parachute.lives == 0:
            self._parachute.drawParachute()

   


    

        