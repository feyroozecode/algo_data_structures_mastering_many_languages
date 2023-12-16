# Day 03 => Algo 1 -> Simple Binary Search
# Binary Search 
def binary_search(arr, target):
    low, high = 0, len(arr) -1
    
    while low <= high :
        mid = (low + high ) // 2
        
        if arr [mid] == target:
            return mid
        
        elif arr[mid] < target:
          low = mid + 1
        else :
            high = mid -1
        
    return -1

 # Test
 
mArray = [ 4, 5, 7 , 9 , 2 , 12]
x = int(input("Enter the array you wan to search : "))

result = binary_search(mArray, x)

if result != -1:
    print("Element is present at index : "+ str(result))
else:
    print(f"{x} Not found  on array")
    