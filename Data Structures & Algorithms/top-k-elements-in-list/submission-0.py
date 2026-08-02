class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict={}
        freq=[[] for i in range(len(nums)+1)]

        for i in nums:
            count_dict[i]= 1+count_dict.get(i,0)

        for num, count in count_dict.items():
            freq[count].append(num)
        res=[]

        for i in range(len(freq)-1, 0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        # print(count_dict)
        
        # val=sorted(count_dict.values())[-k:]
        # print('val:',val)
        # return [k for (k,v) in count_dict.items() if v in val]

        


        