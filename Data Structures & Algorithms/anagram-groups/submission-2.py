class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_dict =collections.defaultdict(list)

        for s in strs:
            counter =[0]*26
            for letter in s:
                counter[ord(letter)-ord('a')] += 1
            result_dict[tuple(counter)].append(s)
        out=[]
        for val in result_dict.values():
            out.append(val)
        return out



        