class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_list = len(nums)
        has_duplicate = set(nums)
        if original_list == len(has_duplicate):
            return False
        else:

            return True
        