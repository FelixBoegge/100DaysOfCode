s = "123"

def permutation(s):
    permutation1(s, "")

def permutation1(s, prefix):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            rem = s[0:i] + s[i+1:]
            permutation1(rem, prefix + s[i])

print(permutation(s))
