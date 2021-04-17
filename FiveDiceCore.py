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
                return x+1

        return False

    def two_pair(self):
        slice_list = []
        for x in range(0,6):
            if self.counted[x] == 2:
                slice_list.append(x)

        if len(slice_list) == 2:
            return (slice_list[1]+1)*10+(slice_list[0]+1)

        return False

    def three_of_a_kind(self):
        for x in range(0,6):
            if self.counted[x] == 3:
                return x+1

        return False

    def four_of_a_kind(self):
        for x in range(0,6):
            if self.counted[x] == 4:
                return x+1

        return False


    def five_of_a_kind(self):
        for x in range(0,6):
            if self.counted[x] == 5:
                return x+1

        return False

    def full_house(self):
        has_pair = 0
        has_trips = 0

        for x in range(0,6):
            if self.counted[x] == 2:
                has_pair = x+1
            if self.counted[x] == 3:
                has_trips = x+1
        if has_pair and has_trips:
            return (has_trips*10)+has_pair

        return False

    def straight(self):
        low_straight = [1,1,1,1,1,0]
        high_straight = [0,1,1,1,1,1]

        if self.counted == low_straight:
            return 1

        if self.counted == high_straight:
            return 2

        return False

    def evaluate_power(self):
        if EvaluatePower.five_of_a_kind(self.counted):
            return (7, EvaluatePower.five_of_a_kind(self.counted))

        elif EvaluatePower.four_of_a_kind(self.counted):
            return (6, EvaluatePower.four_of_a_kind(self.counted))

        elif EvaluatePower.full_house(self.counted):
            return (5, EvaluatePower.full_house(self.counted))

        elif EvaluatePower.straight(self.counted):
            return (4, EvaluatePower.straight(self.counted))

        elif EvaluatePower.three_of_a_kind(self.counted):
            return (3, EvaluatePower.three_of_a_kind(self.counted))

        elif EvaluatePower.two_pair(self.counted):
            return (2, EvaluatePower.two_pair(self.counted))

        elif EvaluatePower.pair(self.counted):
            return (1, EvaluatePower.pair(self.counted))
        else:
            return (0, 0)

class WhoWins:
    # player is tuple (hand power) so is dealer
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.winner = self.player_wins()

    def player_wins(self):
        if self.player[0] == self.dealer[0]:
            if self.dealer[1] >= self.player[1]:
                return False
            else:
                return True

        if self.dealer[0] >= self.player[1]:
            return False
        else:
            return True
