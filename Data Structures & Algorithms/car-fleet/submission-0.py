class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p,s) for p,s in zip(position, speed)]
        fleets=1
        pair.sort(reverse=True)

        stack=[]

        for i in range(len(pair)):
            time=(target-pair[i][0])/pair[i][1]
            if not stack:
                stack.append(time)
            if time > stack[-1]:
                stack.append(time)
        return len(stack)