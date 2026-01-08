def solution(chicken):
    service = 0
    coupon = 0 
    while chicken != 0: # chicken 1999, 199, 19, 1
        coupon += (chicken % 10) # coupon 9, 18, 27, 28
        chicken //= 10 # chicken 199, 19, 1, 0
        service += chicken # service 199, 218, 219, 219
    
    while coupon >= 10:
        r = coupon // 10
        service += r
        coupon %= 10
        coupon += r
    return service