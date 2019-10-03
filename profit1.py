def get_max_profit(price):
    min_price=price[0]
    max_profit=0

    for i in price:
        min_price=min(min_price,i)

        profit=i-min_price

        max_profit=max(max_profit,profit)
    return max_profit

s=[10,7,5,8,9,11]
print(get_max_profit(s))