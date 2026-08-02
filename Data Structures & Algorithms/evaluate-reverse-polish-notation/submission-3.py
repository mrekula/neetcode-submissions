class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        r=0
        while r < len(tokens):
            if tokens[r] in '+-*/' and stack:
                b= int(stack.pop())
                a= int(stack.pop())
                if tokens[r]== '+':
                    num = a + b
                elif tokens[r]=='-':
                    num = a-b
                elif tokens[r]=='*':
                    num = a*b
                elif tokens[r]=='/':
                    num = int(a/b)
                stack.append(num)

            else:
                stack.append(tokens[r])
            r += 1
        return int(stack[-1])


            


        