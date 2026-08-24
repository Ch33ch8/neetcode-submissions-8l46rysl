class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ansdict = {} # val : index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ansdict:
                return [ansdict[diff], i]
            ansdict[num] = i
        return