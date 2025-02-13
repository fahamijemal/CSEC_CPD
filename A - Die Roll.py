from math import gcd
 
Y, W = map(int, input().split())
 
max_roll = max(Y, W)
 
winning_outcomes = 6 - max_roll + 1
 
g = gcd(winning_outcomes, 6)
print(f"{winning_outcomes // g}/{6 // g}")
