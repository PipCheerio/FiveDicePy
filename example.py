# example.py
from FiveDiceCore import Model, Random, CountOccurences, EvaluatePower, WhoWins

# Unit testing example
# Loop infinite to find any bugs


while True:
    # make class inheritence more intuitive

    state = Model(Random.random_hand(), Random.random_hand())

    print({'player': state.player, 'dealer':state.dealer})

    p = CountOccurences(state.player)
    d = CountOccurences(state.dealer)

    p_pow = EvaluatePower(p)
    d_pow = EvaluatePower(d)

    w = (WhoWins(p_pow.power, d_pow.power))
    
    print(w.__dict__)

    input("Press any key to continue")
