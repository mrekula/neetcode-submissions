class Solution:
    def isValid(self, s: str) -> bool:

        dict_my = {'(': ')', '{' :'}', '[' :']'}
        stack =[]

        for sym in s:
            if sym in dict_my:
                stack.append(sym)
            else:
                if len(stack) > 0:
                    out = stack.pop()
                    if dict_my[out] != sym:
                        return False
                else:
                    return False
        return True if len(stack) ==0 else False

        