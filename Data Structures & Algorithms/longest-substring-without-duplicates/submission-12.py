class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        condition
        
        for r in range():
            add s[r] into window
            while condition not valid:
                rmeove s[l] from window
                l += 1
            max(curr_len, existing_le)
    
        '''

        l = 0
        window = {}
        res = 0

        for r in range(len(s)):
            if s[r] in window:
                l = max(l, window[s[r]] + 1)
                # window[s[l]] -= 1
                # if window[s[l]] == 0:
                #     del window[s[l]]
                # l += 1

            window[s[r]] = r
            res = max(res, r-l+1)
        return res




        
            








            
        