class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memory = [float('inf')] * (amount+1)

        memory[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    memory[i] = min(memory[i], 1 + memory[i - coin])
        print(memory)
        return memory[-1] if memory[-1] != float('inf') else -1
        

        