class Parachute():
    
    #Initial
    def __init__(self):
        self.lives = 5

    #Draws different parts of the parachute depending on how many lives remain
    def drawParachute(self):
        print("")
        if self.lives > 4:
            print("  _____")
        if self.lives > 3:
            print(" /_____\\")
        if self.lives > 2:
            print(" \\     /")
        if self.lives > 1:
            print("  \\   /")
        if self.lives > 0:
            print("    O")
        if self.lives == 0:
            print("    X")

        print("   /|\\")
        print("   / \\")
        print("\n^^^^^^^^^")

    #Reduces lives if input is not correct
    def updateLives(self, correct):
        if not correct:
            self.lives -= 1