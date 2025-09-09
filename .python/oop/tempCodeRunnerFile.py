 return left + mid + right
    for i in range(len(lst)):
        if i < len(left):
            lst[i] = left[i]
        elif i < len(left) + len(mid):
            lst[i] = mid[i - len(left) + 1]
        else:
            lst[i] = right[i - len(left) - len(right) + 2]
    return quick_sort(lst)