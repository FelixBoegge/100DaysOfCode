def longest_contained_range(A: [int]) -> int:
    unprocessed_entries = set(A)
    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)

    return max_interval_size


A = [102, 10, 5, 99, 98, 97, 3, 101, 11, 6, 100, 4, 104, 103]
print(longest_contained_range(A))
