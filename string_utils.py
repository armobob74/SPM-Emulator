def determineStatusCode(string):
    """
    This helps the emulator determine how to respond to a particular string

    returns '@' if the command is expected to make the machine busy
    otherwise returns '`'
    """

    if len(string) > 512:
        return 'O'
    letters = [c for c in string if c.isalpha()]
    letters.sort()
    busy_letters = 'BPDR'
    for busy_letter in busy_letters:
        if busy_letter in letters:
            return '@'
    return '`'


