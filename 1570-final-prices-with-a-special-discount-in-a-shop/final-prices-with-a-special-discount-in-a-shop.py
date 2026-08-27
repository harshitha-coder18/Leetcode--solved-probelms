class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<= prices[i]:
                    price=prices[i]-prices[j]
                    ans.append(price)
                    break
            else:
                ans.append(prices[i])
        return ans
                

        