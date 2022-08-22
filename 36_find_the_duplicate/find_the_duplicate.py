def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    dupe = {}
    dupe.fromkeys(nums)
    for num in nums:
        dupe[num] = nums.count(num)
    for pair in dupe.items():
        if pair[1] > 1:
            return pair[0]
        else:
            return None

#make empty set then iterate across OG list comparing to set,
#if already in set, return, otherwise add to set
