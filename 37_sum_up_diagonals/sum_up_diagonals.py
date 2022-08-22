def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum = 0
    for num in range(len(matrix[0])):
        sum += matrix[num][num]
    indx = 0
    for num in range(len(matrix[0])-1, -1, -1):
        sum += matrix[num][indx]
        indx += 1
    return sum

#can iterate together, since you can count backwards from end in Python
