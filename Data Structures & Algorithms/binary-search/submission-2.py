class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        h = len(nums)

        while h-l >1:
            m= (l+h)//2
            if nums[m] < target:
                l = m
            else:
                h= m
        return h if h < len(nums) and nums[h] ==target else -1
        