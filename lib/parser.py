def split_string_with_delimiter(string: str, delimiter: str) -> [str]:
    """
    Splits a string based on spaces but keeps the spaces inside the delimiters.
    """

    tokens = string.split()
    result = []

    concatenate: bool = False
    for token in tokens:
        if concatenate:
            if token.endswith(delimiter):
                concatenate = False
                token = token.replace(delimiter, '')
            token = result.pop() + ' ' + token
        elif token.startswith(delimiter):
            concatenate = True
            token = token.replace(delimiter, '')

        result.append(token)

    return result


def currency_to_int(s: str) -> int:
    """
    Just remove a colon.
    """
    return int(s[:len(s)-3] + s[len(s)-2:])
