class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            newBottles = empty // numExchange
            empty = empty % numExchange
            empty = empty + newBottles
            total = total + newBottles

        return total