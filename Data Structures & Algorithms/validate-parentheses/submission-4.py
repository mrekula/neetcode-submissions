class Solution:
    def isValid(self, s: str) -> bool:

        # my_dict= {'(': ')', '{': '}', '[': ']'}
        # l=0
        # r= len(s)-1

        # while l < r:
        #     try: 
        #         if s[r] != my_dict[s[l]]:
        #             return False
        #     except:
        #         return False

        #     l += 1
        #     r -= 1
        # return True

        # prev_len =-1
        # while len(s) != prev_len:
        #     prev_len=len(s)
        #     s = s.replace("()", "").replace("{}", "").replace("[]", "")
        # return True if len(s)==0 else False

        stack=[]
        my_dict= {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in my_dict:
                stack.append(char)
            else:
                if not stack or my_dict[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        return True if not stack else False