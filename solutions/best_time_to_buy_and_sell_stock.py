class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_ptr = 0
        r_ptr = 1
        global_max = 0

        while r_ptr < len(prices):
            if prices[l_ptr] < prices[r_ptr]:
                current = prices[r_ptr] - prices[l_ptr]
                global_max = max(global_max, current)
            else:
                # if r_ptr has moved a lot, this will catch l_ptr up
                l_ptr = r_ptr
            r_ptr += 1
        return global_max
