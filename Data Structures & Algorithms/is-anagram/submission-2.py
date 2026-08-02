class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)

        dict_s, dict_t ={}, {}
        for letter in s:
            dict_s[letter]=dict_s.get(letter,0)+1
        for letter in t:
            dict_t[letter]=dict_t.get(letter,0)+1
        print(dict_s, dict_t)
        return dict_s==dict_t



        
        
        