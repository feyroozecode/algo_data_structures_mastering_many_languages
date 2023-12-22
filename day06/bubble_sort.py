#  DAY 06 , EXO 1 

# Docs 
# Bubble Sort is not the most efficient sorting algorithm, 
# but it is simple to understand and implement. It's often used for 
# educational purposes or for small datasets due to its simplicity.
def bubble_sort(arr):
    n = len(arr)
    
    # traverse through all array elements
    for i in range(n):
        # Last i elements is already in place, no need to check them 
        for j in range(0 , n - i - 1 ):
            # Swap if th elements found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example Usage
m_array = [64, 22, 25, 12, 22, 11, 91]
bubble_sort(m_array)

print("Sorted arrays : ", m_array)