class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # res = set()
        # # i + j + k == 0
        # # i +j == -k
        # for i in range(len(nums)-2):
        #     target = -nums[i]
        #     d = {}
        #     for j in range(i+1, len(nums)):
        #         if target - nums[j] in d:
        #             res.add(tuple(sorted([nums[i],nums[j], target-nums[j]])))
        #         else:
        #             d[nums[j]] = j
        # return [list(val) for val in res]


        nums.sort()
        res = []
        i = 0

        for i, a in enumerate(nums):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1

            while l < r:
                threesum  = a + nums[l] + nums[r]
                if threesum == 0:
                    res.append([a, nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
   

        return res

       


