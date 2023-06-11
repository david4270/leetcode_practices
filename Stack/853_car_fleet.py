class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # reverse sorted by position = sorted by remaining position
        # (remaining) time should be inserted in increasing order
        for pos, spd in reversed(sorted(zip(position, speed))):
            rem = target - pos
            time = rem/spd
                
            if not stack:
                stack.append(time)
            if time > stack[-1]:
                stack.append(time)
        return len(stack)