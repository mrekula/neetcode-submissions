class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict={}

        for i in nums:
            count_dict[i]= 1+count_dict.get(i,0)

        # bucket=[[] for i in range(len(nums)+1)]

        # for num,freq in count_dict.items():
        #     bucket[freq].append(num)

        # res=[]
        # for i in range(len(bucket)-1, 0, -1):

        #     for num in bucket[i]:
        #         res.append(num)
        #         if len(res)==k:
        #             return res
        heap=[]
        for num,freq in count_dict.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [ num for freq,num in heap]










       
        # print(count_dict)
        
        # val=sorted(count_dict.values())[-k:]
        # print('val:',val)
        # return [k for (k,v) in count_dict.items() if v in val]

        


        