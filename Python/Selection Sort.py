def selectionSort(arr):
    n, count = len(arr), 0
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j
                count += 1
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print(count)
    return arr
