class Solution:
    def findMinMoves(self, machines) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1

        target = total // n
        moves, balance = 0, 0

        for dresses in machines:
            balance += dresses - target
            moves = max(moves, abs(balance), dresses - target)

        return moves