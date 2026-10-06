class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hasmaps = set()

        for i in (nums):
            
            if i in hasmaps:
                return True
            hasmaps.add(i)
        return False
        
        