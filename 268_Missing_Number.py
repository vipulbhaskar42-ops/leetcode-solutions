class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=len(nums)
        expected_value=s*(s+1)//2
        actual_value=sum(nums)
        return expected_value-actual_value
       