class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_cont = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in num_cont:
                return [num_cont[comp], i]
            num_cont[n] = i
        return 
