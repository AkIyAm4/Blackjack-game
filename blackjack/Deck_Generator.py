import random

class Shuffling:
    def __init__(self):
        self.cards = [r + s for s in ["♠", "♥", "♦", "♣"]
                      for r in ["A", "K", "Q", "J"] + [str(n) for n in range(10, 1, -1)]]

    def random(self):
        random.shuffle(self.cards)
        return self.cards

    def riffle(self):
        for _ in range(7):
            cut = random.randint(23, 29)
            left = self.cards[:cut]
            right = self.cards[cut:]
            shuffled = []
            for a, b in zip(left, right):
                shuffled.append(a)
                shuffled.append(b)
            shuffled.extend(left[len(right):])
            shuffled.extend(right[len(left):])
            self.cards[:] = shuffled
        return self.cards

    def overhand(self):
        # Overhand shuffle for later
        pass

class Deck:
    def __init__(self, shuffle_method="random"):
        shuffler = Shuffling()
        if shuffle_method == "riffle":
            self.cards = shuffler.riffle()
        else:
            self.cards = shuffler.random()

    def draw(self):
        return self.cards.pop()

    def deck_regen(self, shuffle_method="random"):
        if len(self.cards) < 11:
            self.__init__(shuffle_method)

if __name__ == "__main__":
    cards = Deck().cards
    count = 0
    for card in cards:
        print(card, end=" ")
        count += 1
        if count % 13 == 0:
            print()
            
