class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                a, b = stack.pop(), stack.pop()
                if token== '+':
                    stack.append(int(b)+ int(a))
                elif token== '-':
                    stack.append(int(b)- int(a))
                elif token== '*':
                    stack.append(int(b) * int(a))
                elif token== '/':
                    stack.append(int(int(b) / int(a)))

                
        return stack.pop()
