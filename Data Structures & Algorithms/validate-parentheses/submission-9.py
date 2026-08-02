class Solution:
    def isValid(self, s: str) -> bool:

        # stack =[]
        # map = {'(': ')', '{': '}','[': ']'}

        # for l in s:
        #     if l in map:
        #         stack.append(l)
        #     else:
        #         if stack and map[stack[-1]] ==l:
        #             stack.pop()
        #         else:
        #             return False
        # return True if not stack else False

        while '{}' in s or '()' in s or '[]' in s:
            s=s.replace('{}','')
            s=s.replace('[]','')
            s=s.replace('()','')
        return s==''


        