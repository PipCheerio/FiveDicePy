from random import randint

class Model:
    dealer: list
    player: list

    def __init__(self, dealer, player):
        self.dealer = dealer
        self.player = player

class Random:
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

def EvaluatePower:

    def __init__(self, counted):
        self.counted = counted
        


        

    def pair(self):
        for x in range(0,5):
            if self.hand[x] == 2:
                return True

        return False

    def two_pair(self):
        pair_count = int
        for x in range(0,5):
            if self.hand[x] == 2:
                pair_count += 1
        if pair_count == 2:
            return True

        return False

    def three_of_a_kind(self):
        for x in range(0,5):
            if self.hand[x] == 3:
                return True

        return False

    def four_of_a_kind(self):
        for x in range(0,5):
            if self.hand[x] == 4:
                return True

        return False


    def five_of_a_kind(self):
        for x in range(0,5):
            if self.hand[x] == 5:
                return True

        return False

    def full_house(self):
        has_pair = bool
        has_trips = bool

        for x in range(0,5):
            if self.hand[x] == 2:
                has_pair = True
            if self.hand[x] == 3:
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


state = Model(Random.random_hand(), Random.random_hand())


print(state.player, state.dealer)

p = CountOccurences(state.player)
d = CountOccurences(state.dealer)

print(p.counted, d.counted)

