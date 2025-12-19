def snb(prices): ##brute force solution
    n=len(prices)
    max_profit=0
    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
                p=prices[j]-prices[i]
                max_profit=max(max_profit,p)
    return max_profit



prices=[7,2,1,5,6,4,8]

print(snb(prices))

##optimal solution

def opti(prices):
    n=len(prices)
    max_profit=0
    min_prices=float('inf')
    for i in range(0,n):
        min_prices=min(min_prices,prices[i])
        max_profit=max(max_profit,prices[i]-min_prices)

    return max_profit

print(opti(prices))