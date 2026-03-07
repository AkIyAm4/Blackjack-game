# Blackjack

A python project based on a card game called ***blackjack*** or ***21***.

## Notes:

This project's logic might be complete but there are tons of other things that still needs to be improved and added to make the game realistic as much as possible.

## 🃏 Blackjack Rules

Blackjack is a classic card game where players try to get as close as possible to **21** without going over.

---

### 🎯 Objective
- Beat the dealer by having a hand value **closer to 21** than the dealer’s hand.  
- If your hand goes **over 21**, you **bust** and automatically lose.

---

### 🂡 Card Values
| Card Type       | Value                  |
|-----------------|------------------------|
| Number cards    | Face value (2–10)      |
| Face cards (J,Q,K) | 10 points each      |
| Ace (A)         | 1 **or** 11 (whichever benefits the hand) |

---

### 🔄 Gameplay

1. **Starting the Game**
   - Each player is dealt **two cards** face up.  
   - The dealer receives **two cards** (one face up, one face down).  

2. **Player’s Turn**
   - **Hit** → Take another card.  
   - **Stand** → Keep your current hand.  
   - **Double Down** → Double your bet and take **one final card**.  
   - **Split** → If you have two cards of the same value, split them into two separate hands.  

3. **Dealer’s Turn**
   - Dealer reveals their hidden card.  
   - Dealer must **hit** until reaching **17 or higher**.  

---

### 🏆 Winning
- ✅ You win if your hand is closer to **21** than the dealer’s.  
- ✅ You win if the dealer **busts** (goes over 21).  
- ❌ You lose if you **bust**.  
- 🤝 If you and the dealer have the same value → It’s a **push** (tie).  

---

## Upcoming Features:
- Betting system
- +1 Shuffling Method - Overhand Shuffle
- Smarter dealer (Machine Learning Applied)
- A more user friendly interface using a python library called [***Pygame***](https://www.pygame.org)
- Database: For game history and possibly a leaderboard with the use of [***SQLite***](https://www.sqlite.org)
