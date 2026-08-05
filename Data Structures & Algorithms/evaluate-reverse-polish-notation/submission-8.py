class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for i in range(len(tokens)):
            if tokens[i] in ('+','-','*','/'):

                curr = int(stack.pop())
                prev = int(stack.pop())

                if tokens[i] =='+':
                    stack.append(curr+prev)
                elif tokens[i]=='-':
                    stack.append(prev- curr)
                elif tokens[i]=='*':
                    stack.append(curr * prev)
                else:
                    stack.append(float(prev/curr))
                print(stack)
            else:
                stack.append(tokens[i])
        return int(stack[-1])


                



