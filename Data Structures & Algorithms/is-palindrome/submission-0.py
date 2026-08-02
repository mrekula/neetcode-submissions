class Solution:
    def isPalindrome(self, s: str) -> bool:

        str_processed=''.join([char.lower() for char  in s if char.isalnum()])
        # for i in range(round(len(str_processed)/2)):
        #     if str_processed[i] != str_processed[len(str_processed)-i-1]:
        #         return False
        # return True

        #return str_processed ==''.join([str_processed[len(str_processed)-i-1] for i in range(len(str_processed))])

        l,r=0, len(s)-1

        while l < r:
            while l <r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r += -1
            if s[l].lower() != s[r].lower():
                return False
            l, r= l+1, r-1
        return True
