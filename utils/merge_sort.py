from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    i = j = k = 0

    while i<len(left) and j<len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1

        k+=1
        
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1

    return arr


if __name__ == '__main__':
    
    test_arr = [1,10,5,4, 8, 13]
    print(merge_sort(test_arr))
        
