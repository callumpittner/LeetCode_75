class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        run_sum = []
        if len(nums) < 1:
            return 0
        for idx, num in enumerate(nums):
            if idx == 0 :
                run_sum.append(num)
            else:
                run_sum.append(run_sum[idx-1]+num)

        return run_sum
