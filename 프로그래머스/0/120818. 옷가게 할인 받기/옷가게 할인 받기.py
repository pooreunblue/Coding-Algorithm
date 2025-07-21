def solution(price):
    discount_list = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}
    for discount_price, discount_rate in discount_list.items():
        if price >= discount_price:
            return int(price * discount_rate)