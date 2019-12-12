"""
   Heap Sort
   
   Approach:
        0. the same as selection sort, select the maximum one by one
        1. build binary heap (max heap) of array with length n
        2. since the max is the first, swap first and last element
        3. heapify the array with length n-1 (don't heapify the last elemtn)
        4. repeat 2~3 until done
        5. the array is now in ascending order
        

"""

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

# Driver code to test above
if __name__ == '__main__':
    arr = [ 12, 11, 13, 5, 6, 7]
    print ("Unsorted array:", arr)
    heapSort(arr)
    print ("Sorted array is", arr)
