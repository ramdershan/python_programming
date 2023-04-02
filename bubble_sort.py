def bubble_sort(data: list) -> None:

    n = len(data)
    count = 0

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            count+=1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break
    print('Count of comparison is ', count)    


numbers = [1,2,3,4,6,5,7]
print ('Sorting...')
bubble_sort(numbers)
print('sorted array ==', numbers)