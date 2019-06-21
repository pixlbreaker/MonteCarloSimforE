import Roulette


'''
Given the game, number of spins and the bet on the pocket returns what the net gain/loss is
'''
def playRoulette(game, numSpins, pocket, bet, toPrint):
    totPockets = 0
    for i in range(numSpins):
        game.spin()
        totPockets += game.betPocket(pocket, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting', pocket, '=', str(100*totPockets/numSpins) + '%\n')
    return (totPockets/numSpins)

game = Roulette.FairRoulette()
eugame = Roulette.EuRoulette()
amgame = Roulette.AmRoulette()

for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(game, numSpins, 2, 1, True)

for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(eugame, numSpins, 2, 1, True)

for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(amgame, numSpins, 2, 1, True)