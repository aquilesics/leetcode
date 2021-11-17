def binarySearch(array: list[int], target: int) -> int:
    if target in array:
        return array.index(target)

    else:
        return -1    


def binarySearch_2(array: list[int], target: int) -> int:
    right = len(array) -1 
    left = 0
    
    while left <= right:
        pivot = left + (right - left)//2
        if array[pivot] == target:
            return pivot

        if array[pivot] > target:
            right = pivot - 1

        else:
            left = pivot + 1 

    return -1
