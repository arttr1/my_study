def spiral_matrix(n):

    
    matrix = [[0 for _ in range(n)] for _ in range(n)] #генератор матрицы n*n
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while num <= n * n:
        # заполнение верхнего слоя
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # заполнение правого слоя
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # заполнение нижнего слоя
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # заполнение левого слоя
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    # вывод
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

n = int(input('/// '))
spiral_matrix(n)
