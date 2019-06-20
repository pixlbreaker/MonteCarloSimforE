import random

class FairRoulette():

    '''
    The basics for a fair Roulette Game. 
    Taken from the Monte Carlo youtube Video https://www.youtube.com/watch?v=OgO1gpXSUzU
    '''
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1
    
    '''
    Spins the ball
    '''
    def spin(self):
        self.ball = random.choice(self.pockets)
    
    '''
    Places a bet on the given pocket with a given amount.
    Returns the won amount
    '''
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return self.pocketOdds * amt
        else:
            return -amt
    
    '''
    String stuff
    '''
    def __str__(self):
        return 'Fair Roulette'