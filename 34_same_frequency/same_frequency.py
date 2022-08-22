def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    dict1 = {char: 0 for char in str(num1)}
    for key in dict1.keys():
        dict1[key] = str(num1).count(key)
    dict2 = {char: 0 for char in str(num2)}
    for key in dict2.keys():
        dict2[key] = str(num2).count(key)
    return dict1 == dict2

#written as function for counting frequency using str() to iterate
#function called on either value, and checked if true
