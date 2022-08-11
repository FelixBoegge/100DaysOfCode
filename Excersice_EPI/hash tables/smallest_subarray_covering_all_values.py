import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_subarray_covering_set(paragraph: [str], keywords) -> Subarray:
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1
        while remaining_to_cover == 0:
            if result == Subarray(start=-1, end=-1) or (right - left) < (result.end - result.start):
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result



paragraph = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
keywords = ('apple', 'dog', 'banana')
print(find_smallest_subarray_covering_set(paragraph, keywords))
