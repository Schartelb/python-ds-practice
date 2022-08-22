def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    check = phrase.replace(" ", "")
    check = check.lower()
    backwards = list(check)
    output = ""
    for num in range(len(backwards)-1, -1, -1):
        output += backwards[num]
    return check == output
