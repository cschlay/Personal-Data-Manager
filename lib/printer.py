def format_currency(amount: int) -> str:
    """
    Currencies are stored as integers so we must add a colon so that EESS is returned EE,SS.
    Thus printable as EE,SS €.
    """
    value: str = str(amount)
    if value == '0':
        return '0'
    elif amount < 100:
        return '0,' + value
    else:
        return value[:len(value) - 2] + ',' + value[len(value) - 2:]
