def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    for num in range(len(nums)-2):
        tot = 0
        tot = nums[num]+nums[num+1]+nums[num+2]
    return tot % 2 != 0

#using if with num++ to return true stops function before checking everything
