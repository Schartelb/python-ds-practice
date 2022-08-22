def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = [char for char in s if char in "AaEeIiOoUu"]
    s2 = list(s)
    num = len(vowels)-1
    for count in range(len(s)-1):
        if s2[count] in "AaEeIiOoUu":
            print(s2[count], s[count], vowels[num])
            s2[count] = vowels[num]
            num -= 1
    return "".join(s2)
