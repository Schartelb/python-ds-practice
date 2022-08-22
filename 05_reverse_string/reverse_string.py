from ctypes.wintypes import WORD


def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    backwards = list(phrase)
    output = ""
    for num in range(len(backwards)-1, -1, -1):
        output += backwards[num]
    return output

    #Python can slice backwards using phrase[-1]... incredibly more efficient
