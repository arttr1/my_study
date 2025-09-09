def sect_sort(arr, start, lenght = None):
    if lenght != None:
        end = start + lenght
    else: end = len(arr)

    new_arr = arr[start:end]
    
    return new_arr

a = [1, 2, 5, 7, 4, 6, 3, 9, 8]
a1 = [9, 7, 4, 2, 5, 3, 1, 8, 6]

print(sect_sort(a, 2))
print(sect_sort(a1, 2, 5))