"""
913. Cat and Mouse
"""
from typing import List

# Using BFS find from ending to beginning.
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE_TURN, CAT_TURN = 1, 2
        MOUSE_WIN, CAT_WIN = 1, 2

        # All ending cases:
        # Cat win.
        # (CAT_TURN, UNKNOWN) ---- cat catch mouse ---> (MOUSE_TURN, CAT_WIN): can be reverse
        # (MOUSE_TURN, UNKNOWN) ---- mouse meet cat ---> (CAT_TURN, CAT_WIN)

        # Mouse win.
        # (MOUSE_TURN, UNKNOWN) ---- mouse find 0 ---> (CAT_TURN, MOUSE_WIN)
        # (CAT_TURN, MOUSE_WIN) ---- mouse find 0 in previous ---> (CAT_TURN, MOUSE_WIN)

        # Reverse above, find begin from result.
        # Total number of states. [MOUST_POINT, CAT_POINT, TURN]
        # 1: mouse turn, 2: cat turn. We do not use 0.
        dp = [ [ [0] * 3 for _ in range(len(graph)) ] for _ in range(len(graph)) ]
        queue = []
        # Find all ending states.
        # Cat can not be in 0
        for i in range(1, len(graph)):
            for j in range(1, 3):
                # Cat wins.
                dp[i][i][j] = CAT_WIN
                queue.append((i, i, j))
                # Mouse wins.
                dp[0][i][j] = MOUSE_WIN
                queue.append((0, i, j))

        # Defind a method to find all previous states.
        def findAllPreviousStates(cur_state):
            ret = []
            mouse, cat, turn = cur_state
            # If current turn is mouse, then previous will be cat.
            # previose states will only contain all possible of previous
            # locations.
            # Vice verse when current turn is cat
            if turn == MOUSE_TURN:
                for pre_cat in graph[cat]:
                    # previous state should
                    # Cat can not be in 0
                    if pre_cat == 0: continue
                    ret.append((mouse, pre_cat, CAT_TURN))
            else:
                for pre_mouse in graph[mouse]:
                    ret.append((pre_mouse, cat, MOUSE_TURN))
            return ret

        def allNeighboursWin(pre_state):
            mouse, cat, turn = pre_state
            if turn == MOUSE_TURN:
                for nextMouse in graph[mouse]:
                    if dp[nextMouse][cat][CAT_TURN] != CAT_WIN:
                        return False
            else:
                for nextCat in graph[cat]:
                    # Cat can not be in 0
                    if nextCat == 0:
                        continue

                    if dp[mouse][nextCat][MOUSE_TURN] != MOUSE_WIN:
                        return False
            return True

        # Doing BFS search.
        while queue:
            mouse, cat, turn = queue.pop(0)
            # find all possible parent states.
            for pre_state in findAllPreviousStates((mouse, cat, turn)):
                pre_mouse, pre_cat, pre_turn = pre_state

                # If previous state is calculated, then continue
                if dp[pre_mouse][pre_cat][pre_turn] != 0: continue

                # search case:
                # sound case
                # current: (MOUSE_TURN, CAT_WIN) -> pre: (CAT_TURN, CAT_WIN) -> prepre: (MOUSE_TURN, X)
                # current: (CAT_TURN, MOUSE_WIN) -> pre: (MOUSE_TURN, MOUSE_WIN) -> prepre: (CAT_TURN, X)

                # not sound case: because previous status depend on your opponents.
                # I do not think you opponents will want you win.
                # current: (MOUSE_TURN, MOUSE_WIN) !-> pre: (CAT_TURN, CAT_WIN)
                # current: (CAT_TURN, CAT_WIN) !-> pre: (MOUSE_TURN, MOUSE_WIN)
                if turn == MOUSE_TURN and dp[mouse][cat][turn] == CAT_WIN:
                    dp[pre_mouse][pre_cat][CAT_TURN] = CAT_WIN
                    queue.append(pre_state)
                elif turn == CAT_TURN and dp[mouse][cat][turn] == MOUSE_WIN:
                    dp[pre_mouse][pre_cat][MOUSE_TURN] = MOUSE_WIN
                    queue.append(pre_state)
                #TODO: Do not understand.
                elif allNeighboursWin(pre_state):
                    if pre_turn == MOUSE_TURN:
                        dp[pre_mouse][pre_cat][MOUSE_TURN] = CAT_WIN
                    else:
                        dp[pre_mouse][pre_cat][CAT_TURN] = MOUSE_WIN
                    queue.append(pre_state)

        return dp[1][2][1]
