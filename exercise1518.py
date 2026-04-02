class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            total_bottles += empty_bottles // numExchange
            empty_bottles = empty_bottles // numExchange + empty_bottles % numExchange
        return total_bottles
