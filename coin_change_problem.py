"""
Given a target amount n and a list (array) of distinct coin values,
what's the fewest coins needed to make the change amount.

For example:
If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
 - 1+1+1+1+1+1+1+1+1+1
 - 5 + 1+1+1+1+1
 - 5+5
 - 10
With 1 coin being the minimum amount.

Note: Problem is implemented by Dynamic Programming (memoization) technique

Author: Aditya Dubal
Language: Python 2.7
"""


def target_ways(target, coins_list, known_values):
    """
    Function to compute minimum number of ways to get target amount
    Input: target       - amount number
           coins_list   - list of distinct coin values
           known_values - list of cached values
    Return: min_coins   - minimum number of coins required
    """
    min_coins = target

    # Base case: if target is in coins_list
    if target in coins_list:
        known_values[target] = 1
        return 1

    # check for entry in cache
    elif known_values[target] > 0:
        return known_values[target]

    else:
        for coin_value in [each_coin for each_coin in coins_list if each_coin <= target]:

            # Recursive function call with subtracted coin amount
            number_coins = 1 + target_ways(target-coin_value, coins_list, known_values)

            # if new minimum is found then replace
            if number_coins < min_coins:
                min_coins = number_coins
                # store result for future use
                known_values[target] = min_coins

    return min_coins


# Get Input for target amount e.g. 74,83,...
print 'Enter the target amount: '
target_amount = int(raw_input())

# List of distinct coin values
available_coins = [1, 5, 10, 25]

# Cache to store values of known results
known_results = [0] * (target_amount + 1)

print 'Minimum number of ways to get target amount is ', target_ways(target_amount, available_coins, known_results)
