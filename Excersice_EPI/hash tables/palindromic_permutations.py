import collections


def can_form_palindrome(s: str) -> bool:
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


s = 'asdfrrasdffdsadsafvvewewq'
print(can_form_palindrome(s))
