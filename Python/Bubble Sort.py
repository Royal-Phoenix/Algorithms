def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1], swapped = arr[j+1], arr[j], True
                if swapped is False:
                    break
    return arr
