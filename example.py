# example.py
from FiveDiceCore import Model, Random, CountOccurences, EvaluatePower

state = Model(Random.random_hand(), Random.random_hand())


print(state.player, state.dealer)

p = CountOccurences(state.player)
d = CountOccurences(state.dealer)

print(p.counted, d.counted)

p_pow = EvaluatePower(p)
d_pow = EvaluatePower(d)

print(p_pow.power, d_pow.power)
