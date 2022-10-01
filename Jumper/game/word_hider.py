
import random

class WordHider:

    #Initial
    def __init__(self):
        self._word = ""
        self._letters = {}
        
    #Picks a random word
    def get_word(self):
        words = ["award", "block", "apple", "grass", "horse", "fight", "earth",\
                "dream", "metal", "phone", "party", "plant", "match", "music",\
                "order", "plane", "knife", "rugby", "skill", "river", "smith",\
                "round", "smoke", "sheep", "trust", "water", "youth", "taste",\
                "thing", "layer", "field", "guide", "cream", "chief", "chair",\
                "beach", "river", "dance", "cycle", "brain", "crown", "crime",\
                "motor", "stuff", "board", "error", "floor", "force", "judge"]
        
        choice = random.randint(0, 49)
        self._word = words[choice]
        return self._word

    #Turns word into letter list
    def get_letters(self, word):
        letters_list = list(word)
        self._letters = {1: letters_list[0], 2: letters_list[1], 3: letters_list[2], 4: letters_list[3], 5: letters_list[4]}
        return self._letters

