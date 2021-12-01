def is_between(value: str, minimum: int, maximum: int) -> bool:
    if not value.isdigit():
        return False
    value = int(value)
    return minimum <= value <= maximum
