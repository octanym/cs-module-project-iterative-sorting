# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):  # O(n)
        smallest_index = i  # O(1)
        # interview the remaining values in arr for candidacy as smallest index
        for j in range(i + 1, len(arr)):  # O(n)
            if arr[j] < arr[smallest_index]:  # O(1)
                # update the index for the smallest_index thus far, while we continue investigating the rest of the array for smaller indices
                smallest_index = j  # O(1)
        # after j has finished its investigation for smaller values, swap i with smallest_index
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]  # O(1)
    return arr

# O(n²)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(len(arr)):  # O(n)
        N = len(arr) - i  # O(1)
        for j in range(N - 1):  # O(n)
            if arr[j] > arr[j + 1]:  # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1)
    return arr

# O(n²)


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
