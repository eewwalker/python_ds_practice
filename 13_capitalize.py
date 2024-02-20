def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    capital_letter = phrase[0].upper()

    sliced = phrase[1:]

    return capital_letter + sliced
