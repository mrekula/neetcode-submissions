class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=collections.defaultdict(list)
        for word in strs:
            counter=[0]*26
            for i in word:
                counter[ord(i)-ord('a')]+= 1
            result[tuple(counter)].append(word)
        # print(result.values())
        return [i for i in result.values()]



        