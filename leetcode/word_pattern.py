def wordPattern(pattern: str, s: str) -> bool:
    words = {}
    if len(pattern) != len(s.split(' ')):
        return False
    for i, p in enumerate(pattern):
        word = s.split(' ')[i]
        if p in words:
            if words[p] != word:
                return False
        else:
            if word in words.values():
                return False
            else:
                words[p] = word
    return True

pattern = 'abba'
s = 'dog cat cat dog'
print(wordPattern(pattern, s))
