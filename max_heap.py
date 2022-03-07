heap = [2, 66, 30, 5, 9, 10]
n = len(heap)


def max_heapify(heap, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and heap[largest] < heap[left]:
        largest = left
    if right < n and heap[largest] < heap[right]:
        largest = right
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, n, largest)


# build max heap
for i in range(n//2 -1, -1, -1):
    max_heapify(heap, n, i)

# Display
print("Max heap is: ", heap)
