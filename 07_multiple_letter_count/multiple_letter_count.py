def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters = list(phrase)
    output = {}
    for item in letters:
        output[item] = letters.count(item)
    return output

#can iterate through strings in Python
#use dct.get(key,0)+1
