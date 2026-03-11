class BetTracker:
    def __init__(self):
        self.history = [] # list of {"bet": amount, "result": "win"/"loss"/"tie"}
        self.streak = 0 # current consecutive win streak which will be used in machine learning later.

    def update(self, bet_amount, result):
        self.history.append({"bet": bet_amount, "result": result})
        if result == "win":
            self.streak += 1
        else:
            self.streak = 0
