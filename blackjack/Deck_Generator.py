import random

def shuffling_choice():
    print("===== Shuffling Methods =====")
    print("1. Random Shuffle")
    print("2. Riffle Shuffle")
    print("3. Overhand Shuffle")
    while True:
        choice = int(input("Choose a shuffling method: "))

        deck = Shuffling()

        if choice == 1:
            deck.random()
            return deck.cards

        elif choice == 2:
            deck.riffle()
            return deck.cards

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

class Deck:
    def __init__(self):
        self.cards = shuffling_choice()

    def draw(self):
        return self.cards.pop()

    def deck_regen(self): # NEEDS FIXING
        if len(self.cards) < 11:
            print("\nRegenerating the deck, please wait...")
            self.__init__()
            print("\nRegeneration done.")
