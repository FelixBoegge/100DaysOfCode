import math

def check_palindrome(x: int) -> bool:
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x))+1
    MSD_mask = pow(10, (num_digits-1))
    for i in range(num_digits//2):
        if x // MSD_mask != x % 10:
            return False
        x %= MSD_mask
        x //= 10
        MSD_mask //= 100
    return True

x = 234323432
print(check_palindrome(x))
