class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res=defaultdict(list)
        # for word in strs:
        #     sortedS=''.join(sorted(word))
        #     res[sortedS].append(word)

        res=defaultdict(list)
        for word in strs:
            counter=[0]*26
            for letter in word:
                counter[ord(letter)-ord('a')] += 1
            res[tuple(counter)].append(word)   
        return list(res.values())



        