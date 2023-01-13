#Non-Constructible Change
#Time Complexity: O(nlogn) || Space Complexity: O(1)
def nonConstructibleChange(coins):
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if currentChangeCreated + 1 < coin:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1
            