class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in ans_dict:
                return [ans_dict[diff], index]
            ans_dict[num] = index