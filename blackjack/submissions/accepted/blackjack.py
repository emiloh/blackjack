#! /usr/bin/env python3
games = int(input())

for i in range(games):

    sum = 0
    sum2 = 0
    cards = input().split()
    for c in cards:
        if c == "A":
            sum += 11
            sum2 += 1
        elif c == "J":
            sum += 10
            sum2 += 10
        elif c == "Q":
            sum += 10
            sum2 += 10
        elif c == "K":
            sum += 10
            sum2 += 10
        else:
            sum += int(c)
            sum2 += int(c)
    if sum == 21 or sum2 == 21:
        print("BLACKJACK")
    elif sum > 21 and sum2 > 21:
        print("LOST")
    elif sum > 21 and sum2 < 21:
        print(sum2)
    elif sum < 21 and sum2 > 21:
        print(sum)
    else:
        print(max(sum, sum2))
