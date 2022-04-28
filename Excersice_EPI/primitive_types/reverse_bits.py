def reverse_bits(x):
    size = 16
    position = size-1
    y = 0
    while position >= 0:
        y |= (x & 1) << position
        x >> 1
        position -= 1
    return y

rev_cache = []
def build_rev_cache():
    for x in range(2**16):
        rev_cache.append(reverse_bits(x))

def reverse(x: int) -> int:
    build_rev_cache()
    mask_size = 16
    bit_mask = 0xffff
    return (rev_cache[x & bit_mask] << (3* mask_size) |
            rev_cache[(x >> mask_size) & bit_mask] << (2* mask_size) |
            rev_cache[(x >> (2* mask_size)) & bit_mask] << mask_size |
            rev_cache[(x >> (3* mask_size)) & bit_mask])



x = 8
print(bin(x))
print(bin(reverse_bits(x)))
print(bin(reverse(x)))
