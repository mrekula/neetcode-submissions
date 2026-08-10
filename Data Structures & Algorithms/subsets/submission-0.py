class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res =[[]]

        for num in nums:
            temp =[]
            for subset in res:
                temp.append(subset + [num])
                # print(temp)
            res.extend(temp)
        return res