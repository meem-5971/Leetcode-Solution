class Solution(object):
    def maxProfit(self, prices):
        mn_price=prices[0]
        mx_profit=0
        for price in prices[1:]:
            if(price < mn_price):
                mn_price=price
            else:
                profit=price-mn_price
                mx_profit=max(profit,mx_profit)

        
        return mx_profit

