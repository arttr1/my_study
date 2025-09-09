lst = [2, 0, 1, 2, 3, 2, 1, -1, 0, 3,-1, 0,-2, -2 ,1, 2, -3, 1, -3, 3,-3]
# def gnomeSort(a):
#     size = len(a)
#     i = 0
#     j = 1
#     while i < size-1:
#         if a[i] <= a[i+1]: 
#             i = j
#             j = j + 1
#         else:
#             a[i], a[i+1] = a[i + 1],a[i]
#             i = i - 1
#             if i < 0:
#                 i = j
#                 j = j + 1
#     return a




def insertionSort(lst):
    for i in range (len(lst)-1):
        j = i
        num = lst[i+1]
        while num < lst[j] and j>=0:
            lst[j+1] = lst[j]
            j -= 1
        if j != i: lst[j+1] = num

    return lst

print(insertionSort(lst))


# def selection(lst):
#     for i in range(len(lst)-1):
#         ind = i
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[ind]:
#                 ind = j
#         if ind != i: lst[i], lst[ind] = lst[ind], lst[i]
#     return lst

# lst = [6, 2, 5, 3, 7, 4, 1]
# # print(selection(lst))

# def merge_list(left, right):
#     merged = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i+=1
#         else:
#             merged.append(right[j])
#             j += 1
#     #добавляем оставшиеся элементы 
#     merged += left[i:]
#     merged += right[j:]
#     return merged

# def merge_sort(lst):
#     if len(lst) <= 1: return lst

#     middle = len(lst)//2
#     left = lst[:middle]
#     right = lst[middle:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     return merge_list(left, right)

# print(merge_sort(lst))

# косой кривой способ
# def count_sort(lst):
#     mini = min(lst)
#     maxi = max(lst)
#     counts = [0]*maxi
#     res = []
#     for i in lst:
#         counts[i] += 1
#     for i in range(mini, len(lst)):
#         for j in range(counts[i]):
#             if i <= maxi:
#                 res.append(i)
#     return res

# print(count_sort(lst))


# insertion sort
# Insertion sort in Python


# quick sort
