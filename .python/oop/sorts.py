lst = [6, 2, 5, 3, 7, 4, 1]
# lst = [2, 0, 1, 2, 3, 2, 1, -1, 0, 3,-1, 0,-2, -2 ,1, 2, -3, 1, -3, 3,-3]
# lst = [1, 0, 0, 2, 1, 2, 0, 3, 4, 4, 3, 3, 0, 1]

# ================================================================
# def bubble_sort(a):
#     for i in range(len(a)):
#         for j in range(len(a) - i - 1):

#             if (a[j] > a[j+1]): a[j], a[j+1] = a[j+1], a[j]

#     return a

# print(bubble_sort(lst))
# ================================================================
# def shaker_sort(a):
#     left = 0
#     right = len(a) - 1

#     while(left <= right):
#         for i in range(left, right):
#             if (a[i] > a[i+1]): a[i], a[i+1] = a[i+1], a[i]
#         left+=1
#         for i in range(right, left-1, -1):
#             if (a[i-1]>a[i]): a[i-1], a[i] = a[i], a[i-1]
#         right-=1
#     return a

# print(shaker_sort(lst))
# ================================================================

# def gnome_sort(list):
#     index = 0
    
#     while index < len(list):
#         if index == 0: index += 1
#         if list[index] >= list[index - 1]:
#             index += 1
#         else:
#             list[index], list[index - 1] = list[index - 1], list[index]
#             index -= 1

    
#     #return list

# gnome_sort(lst)
# print(lst)
# ==================================================================

# def insertionSort(lst):
#     for i in range(1, len(lst)):
#         num = lst[i]
#         j = i - 1
#         while j > -1 and num <lst[j]:
#             lst[j+1] = lst[j]
#             j -= 1
#         lst[j + 1] = num
#     return lst
# print(insertionSort(lst)) 
    
# ==================================================================

# def shellSort(lst):
#     n = len(lst)
#     gap = len(lst)//2
#     while gap > 0:
#         for i in range(gap, n):
#             num = lst[i]
#             j = i
#             while j >= gap and num < lst[j - gap]:
#                 lst[j] = lst[j - gap]
#                 j -= gap
#             lst[j] = num
#         gap //= 2
#     return lst

# shellSort(lst)
# print(lst)

# ==================================================================

# def selectionSort(lst):
#     for i in range(len(lst)-1):

#         min_in = i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[min_in]: min_in = j

#         lst[i], lst[min_in] = lst[min_in], lst[i]

#     return lst
# selectionSort(lst) 
# print(lst)

# # =================================================================

# def merge_sort(lst):
#     if len(lst) < 2: return lst #возвращаем список если длина 1

#     else: 
#         n = len(lst) // 2 #middle of the list 
#         left, right = merge_sort(lst[:n]), merge_sort(lst[n:])
#         # divide list into two
#         # left = [0, 1,...,n-1]; right = [n, n+1, ... len(list)-1]
#         l = r = 0
#         # go through lists until reach the end of one of them
#         while l < len(left) and r < len(right):
#             if left[l] <= right[r]:
#                 lst[l + r] = left[l]
#                 l += 1
#             elif left[l] > right[r]: 
#                 lst[l + r] = right[r]
#                 r += 1


#         # add to answer-list numbers which remained in left or right list
#         while l < len(left):
#             lst[l + r] = left[l]
#             l += 1
#         while r < len(right):
#             lst[l + r] = right[r]
#             r += 1
#     return lst

# print(merge_sort(lst))
# ==============================================================================


# def count_sort(lst):
#     counts = [0]*(max(lst)-min(lst)+1)

#     for i in lst:
#         counts[i - min(lst)] += 1
#     j = 0
#     for i in range(len(lst)):
#         while counts[j] == 0: j += 1
#         lst[i] = j + min(lst)
#         counts[j] -= 1
#     return lst 
# print(count_sort(lst))
# ==============================================================================

# def quick_sort(lst):
    
#     if len(lst) < 2: return lst #base case, when array consist of 1 number
    
#     pivot = lst[len(lst) // 2]
#     left = [x for x in lst if x < pivot] #list of numbers less then pivot
#     right = [x for x in lst if x > pivot] #list of numbers bigger then pivot
#     mid = [x for x in lst if x == pivot] #list of numbers equal pivot

#     # return quick_sort(left) + mid + quick_sort(right)

#     # call quick_sort function to sort left and right lists 
#     left = quick_sort(left)
#     right = quick_sort(right)


#     # overwriting the original list 
#     j = 0
#     for i in left:
#         lst[j] = i
#         j += 1
#     for i in mid:
#         lst[j] = i
#         j += 1
#     for i in right:
#         lst[j] = i
#         j += 1 
#     return (lst)

# print(quick_sort(lst))
# ===============================================================================


# def stalin_sort(lst):
#     for i in range (1, len(lst)):
#         if lst[i] < lst[i - 1]: 
#             del[lst[i]]
#             return stalin_sort(lst)
#     return lst
# print(stalin_sort(lst))
# ==============================================================================


#thanos sort with deleting one of list parts
# from random import random
# def thanosSort(lst):
#     list_sorted_flag = all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))

#     if not list_sorted_flag:
#         if len(lst) < 2: return lst

#         elif random() < 0.5:
#             return thanosSort(lst[:len(lst)//2])
#         else: return thanosSort(lst[len(lst)//2:])
#     return lst
# print(thanosSort(lst))
# ===========================================================================

# bucket sort 
# def bucketSort(lst):
#     bucket = [[] for i in range(len(lst))]


