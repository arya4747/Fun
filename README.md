# Stone-Paper-Scissors Game 🪨📄✂️

A simple Python implementation of the classic Stone-Paper-Scissors game against the computer.

## How to Play
- Stone (s) beats Scissors (z)
- Paper (p) beats Stone (s)
- Scissors (z) beats Paper (p)

## Game Rules
1. The computer randomly selects Stone (1), Paper (-1), or Scissors (0)
2. You enter your choice:
   - `s` for Stone
   - `p` for Paper
   - `z` for Scissors
3. The winner is determined based on the game rules

## Code Structure
```python
computer = random.choice([1,-1,0])  # Computer's random choice
uDict = {"s":1, "p":-1, "z":0}     # User input mapping
cdict = {1:"Stone", -1:"Paper", 0:"Scissors"}  # Choice display
