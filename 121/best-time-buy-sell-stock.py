## array prices.  Prices[i] --> price of stock on day i
## Want to max profit, buy and sell on different day

## maximize price[i] - price[j] 
## i < j 

## brute force, compare all values to each other


## 7 1 5 3 6 4

## 7 


## looking for the lowest value followed by the highest

def maxProfit(prices:list[int]) -> int:
    buy: int = 0
    sell: int = 1
    max_v: int = 0
    while sell < len(prices):
        if prices[buy] > prices[sell]:
            buy = sell
            sell += 1
        else:
            max_v = max(max_v, prices[sell] - prices[buy])
            sell +=1
            
    return max_v
        
print(maxProfit([7, 1, 5, 3, 6, 4]), 5)
