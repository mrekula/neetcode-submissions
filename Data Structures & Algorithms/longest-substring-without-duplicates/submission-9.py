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

        l, r = 0,0
        max_len = float('-inf')
        valid_window ={}
        for r in range(len(s)):        
            while s[r] in valid_window:
                valid_window[s[l]] -= 1
                if valid_window[s[l]] == 0:
                    del valid_window[s[l]]
                l += 1
            valid_window[s[r]] = 1
            max_len = max(max_len, r-l+1)
        return 0 if max_len  < 0 else max_len
        
            








            
        