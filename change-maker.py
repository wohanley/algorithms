import sys

# This algorithm takes as input a list of coin denominations and
# a total amount to produce. It works by building a list C of solutions to
# the problem for all amounts 0..amount from the bottom up. Any solution to
# the problem can be defined in terms of solutions to these subproblems:
# 
# change(x) = 1 + C(amount-denoms[i])
# 
# where i is the value that minimizes C(amount-denoms[i]). Checking for this
# minimum is the expensive step of this algorithm, at O(denoms.length). Since
# this must be done amount times, once for each subsolution, the total
# complexity of this algorithm is O(denoms.length * amount).

def change(denoms, amount):
    mins = [0]
    for i in range(1, amount+1):
        min_coins = sys.maxsize
        for j in range(len(denoms)):
            if denoms[j] <= i:
                if mins[i-denoms[j]] < min_coins:
                    min_coins = mins[i-denoms[j]]+1
        mins.append(min_coins)
    return mins
