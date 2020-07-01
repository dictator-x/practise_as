"""
735. Asteroid Collision
"""

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            while stack and stack[-1] > 0 and val < 0:
                if stack[-1] < -val:
                    stack.pop()
                    continue
                elif stack[-1] == -val:
                    stack.pop()
                break
            else:
                stack.append(val)
        return stack
