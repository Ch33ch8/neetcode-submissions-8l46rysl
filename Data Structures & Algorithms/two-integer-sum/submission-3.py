class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_cont = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_cont:
                return [num_cont[complement], index]
            num_cont[num] = index
        return []