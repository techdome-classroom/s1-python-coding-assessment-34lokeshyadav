def decode_message(s: str, p: str) -> bool:
    """
    Returns True if the decoder key unlocks the message, False otherwise.
    """
    i, j = 0, 0  # indices for message and key respectively
    while i < len(s) and j < len(p):
        if p[j] == '*':  # star symbol, skip to next key character
            j += 1
            while i < len(s) and (j == len(p) or p[j] != s[i]):
                i += 1
        elif p[j] == '?':  # question mark, match any single character
            i += 1
            j += 1
        elif p[j] == s[i]:  # exact match
            i += 1
            j += 1
        else:  # no match, return False
            return False
    # if we've reached the end of both the message and the key, it's a match
    return i == len(s) and j == len(p)