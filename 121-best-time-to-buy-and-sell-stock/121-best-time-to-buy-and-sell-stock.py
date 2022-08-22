class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        if len(prices)>=2:
            num = prices[0]
            for i in range(1,len(prices)):
                if prices[i]-num > max:
                    max = prices[i]-num
                #elif prices[i]-num == max:
                else:
                    num = min(num,prices[i])
                print(num)
            return max
        else:
            return 0