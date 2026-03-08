"""
Coin Change (DP)
Minimum number of coins to make amount; unlimited supply of each coin.
"""

def coin_change(coins: list[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != float("inf") else -1


def coin_change_ways(coins: list[int], amount: int) -> int:
    """Number of ways to make amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))   # 3 (5+5+1)
    print(coin_change([2], 3))           # -1
    print(coin_change_ways([1, 2, 5], 5))  # 4
