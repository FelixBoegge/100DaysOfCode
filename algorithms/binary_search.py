
def linear_search(nums_list, target):
    for i in range(len(nums_list)):
        if nums_list[i] == target:
            return i
    return -1

def binary_search(nums_list, target):
    left_index = 0
    right_index = len(nums_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_num = nums_list[mid_index]
        if mid_num == target:
            return mid_index
        if mid_num < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursive(nums_list, target, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index + right_index) // 2
    mid_num = nums_list[mid_index]
    if mid_num == target:
        return mid_index
    if mid_num < target:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursive(nums_list, target, left_index, right_index)


def find_occ(nums_list, target):
    index = binary_search_recursive(nums_list, target, 0, len(nums_list))
    indices = [index]
    i = index - 1
    while i >= 0:
        if nums_list[i] == target:
            indices.append(i)
        else:
            break
        i = i - 1
    i = index + 1
    while i < len(nums_list):
        if nums_list[i] == target:
            indices.append(i)
        else:
            break
        i = i + 1
    return sorted(indices)


if __name__ == '__main__':
    nums_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    target = 34


    index = linear_search(nums_list, target)
    print(f"Number found at index {index} using linear search")

    index2 = binary_search(nums_list, target)
    print(f"Number found at index {index2} using binary search")

    index3 = binary_search_recursive(nums_list, target, 0, len(nums_list)-1)
    print(f"Number found at index {index3} using binary search recursively")

    index4 = find_occ(nums_list, target)
    print(f"Number found at indices {index4}")
