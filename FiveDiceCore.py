# FiveDiceCore.py
from random import randint

class Model:

    '''
    State is held here (no shit)
    '''

    dealer: list
    player: list

    def __init__(self, dealer, player):
        self.dealer = dealer
        self.player = player

class Random:

    '''
    Simple class to return a list [] of 
    5 random numbers invoked by the static
    method random_number(), to change
    the algorithm in which evaluated the random
    number change random_number to
    return a single int
    '''

    deck = list

    def __init__(self):
        pass

    @staticmethod
    def random_number():
        number = randint(1,6)
        return number

    @staticmethod
    def random_hand():
        hand = []
        for x in range(0,5):
            number = Random.random_number()
            hand.append(number)

        return hand

class CountOccurences:

    def __init__(self, hand):
        self.hand = hand
        self.counted = self.count_occurences()

    def count_occurences(self):
        hand_counted = []
        for x in range(1,7):
            counted = self.hand.count(x)
            hand_counted.append(counted)
        return hand_counted

class EvaluatePower:

    def __init__(self, counted):
        self.counted = counted
        self.power = self.evaluate_power()


    def pair(self):
        for x in range(0,6):
            if self.counted[x] == 2:
                return True

        return False

    def two_pair(self):
        pair_count = 0
        for x in range(0,6):
            if self.counted[x] == 2:
                pair_count += 1
        if pair_count == 2:
            return True

        return False

    def three_of_a_kind(self):
        for x in range(0,6):
            if self.counted[x] == 3:
                return True

        return False

    def four_of_a_kind(self):
        for x in range(0,6):
            if self.counted[x] == 4:
                return True

        return False


    def five_of_a_kind(self):
        for x in range(0,5):
            if self.counted[x] == 5:
                return True

        return False

    def full_house(self):
        has_pair = False
        has_trips = False

        for x in range(0,6):
            if self.counted[x] == 2:
                has_pair = True
            if self.counted[x] == 3:
                has_trips = True
        if has_pair and has_trips:
            return True

        return False

    def straight(self):
        high_straight = [1,1,1,1,1,0]
        low_straight = [0,1,1,1,1,1]

        if self.hand == high_straight:
            return True
        if self.hand == low_straight:
            return True

        return False

    def evaluate_power(self):
        if EvaluatePower.five_of_a_kind(self.counted):
            return 7
        elif EvaluatePower.four_of_a_kind(self.counted):
            return 6
        elif EvaluatePower.full_house(self.counted):
            return 5
        elif EvaluatePower.straight(self.counted):
            return 4
        elif EvaluatePower.three_of_a_kind(self.counted):
            return 3
        elif EvaluatePower.two_pair(self.counted):
            return 2
        elif EvaluatePower.pair(self.counted):
            return 1
        else:
            return 0
