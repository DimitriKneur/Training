class quizz():
    
    def __init__(self, lives):
    
        self.lives = lives

    def begin(self):
        print("Welcome to our fabulous quizz !")
        print("You have", self.lives, "lives remaining.")

    def wrong(self):
        print("Hell nah")
        self.lives = self.lives - 1
        print("You have", self.lives, "lives remaining.")
        
    def remain(self):   
        return self.lives
        
    def status(self):    
        if self.lives == 0:
            return "dead"
        else:
            return "alive"
        
    def endgame(self):
        if self.lives == 0:
            print("Game. OVER. You. LOSER.")
        else:
            print("Congrats, you completed the quizz without dying !")