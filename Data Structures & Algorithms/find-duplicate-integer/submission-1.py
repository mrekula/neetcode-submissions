class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # hashset=set()

        # for num in nums:
        #     if num in hashset:
        #         return num
        #     hashset.add(num)

        check = [0]*len(nums)

        for num in nums:
            if check[num-1] < 0:
                return num
            check[num-1] = -1*num
            print(check)







        
        