heap = [2, 66, 30, 5, 9, 10]
n = len(heap)


def min_heapify(heap, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and heap[smallest] > heap[left]:
        smallest = left
    if right < n and heap[smallest] > heap[right]:
        smallest = right
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, n, smallest)


# build min heap
for i in range(n//2 -1, -1, -1):
    min_heapify(heap, n, i)

# Display
print("Min heap is: ", heap)
