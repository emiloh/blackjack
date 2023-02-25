#! /usr/env/python3

import sys

games = int(sys.argv[1])
print(games)
hands = sys.argv[2]
hands = hands.strip("[]").split(",")
for i in range(0, len(hands) - 2, 3):
    print(hands[i], hands[i+1], hands[i+2])
