"""
780. Reaching Points
"""
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        if tx < sx or ty < sy:
            return False

        if tx == sx:
            return (ty - sy) % sx == 0
        if ty == sy:
            return (tx - sx) % sy == 0

        if tx > ty:
            return self.reachingPoints(sx, sy, tx % ty, ty)
        elif tx < ty:
            return self.reachingPoints(sx, sy, tx, ty % tx)
        else:
            # tx should never be equal to ty, unless tx = sx and ty = sy
            return False
