class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # d_ =collections.defaultdict(list)
        # for w in strs:
        #     count =[0]*26
        #     for l in w:
        #         count[ord(l)- ord('a')] += 1
        #     d_[tuple(count)].append(w)
        # return list(d_.values())

        d= {}

        for i, word in enumerate(strs):
            word= ''.join(sorted(word))
            if word in d:
                d[word].append(strs[i])
            else:
                d[word]=[strs[i]]
        return list(d.values())
