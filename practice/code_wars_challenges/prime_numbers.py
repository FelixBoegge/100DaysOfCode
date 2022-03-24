def is_prime(num):
    if num < 2 or num in [4,8]:
        return False
    for n in range(3, abs(num//2)+1, 2):
        if abs(num) % n == 0:
            return False
    return True

num = 19

print(is_prime(num))
