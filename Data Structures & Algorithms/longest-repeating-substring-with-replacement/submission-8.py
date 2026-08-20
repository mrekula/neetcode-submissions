class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        '''
        l, r = 0, 0

        for r in range():
            add s[r]
            while condition is not  met:
                remove l from window
                l +=1
            max( existing _max, r-l+1)
        return max
            
        '''
        l   = 0
        max_len = 0
        valid_window = {}
        max_freq = 0



        for r in range(len(s)):
            
            valid_window[s[r]] = 1 + valid_window.get(s[r],0)
            if valid_window[s[r]] > max_freq:
                max_freq = valid_window[s[r]]


            while r-l+1-max_freq > k:
                valid_window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len

        # def is_valid(window):
        #     if sum(window.values()) - max(window.values()) <= k:
        #         return True
        #     return False
        # for r in range(len(s)):
        #     valid_window[s[r]] = 1 + valid_window.get(s[r],0)
        #     while valid_window and not is_valid(valid_window):
        #         valid_window[s[l]] -= 1
        #         if valid_window[s[l]] == 0:
        #             del valid_window[s[l]]
        #         l += 1
        #     max_len = max(max_len, r-l+1)
        # return max_len

            


