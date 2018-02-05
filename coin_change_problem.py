"""
Author: Aditya Dubal
Language: Python 2.7
"""


def target_ways(target, coins_list, known_values):
    """
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)
    
    OUTPUT: Minimum number of coins needed to make the target.
    """
    # Default output to target
    min_coins = target

    # Base case: if target is in coins_list
    if target in coins_list:
        known_values[target] = 1
        return 1

    # Return a known result if it happens to be greater than 1
    elif known_values[target] > 0:
        return known_values[target]

    else:
        # for every coin value that is <= than target
        for coin_value in [each_coin for each_coin in coins_list if each_coin <= target]:

            # Recursive function call with subtracted coin amount
            number_coins = 1 + target_ways(target-coin_value, coins_list, known_values)

            # Reset Minimum if we have a new minimum
            if number_coins < min_coins:
                min_coins = number_coins
                # Reset the known result
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
