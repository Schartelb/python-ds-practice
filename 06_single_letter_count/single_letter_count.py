def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    countword = list(word)
    return countword.count(letter)

#concatenate 13 and 14 and make lowercase
#return word.lower().count(letter.lower())
