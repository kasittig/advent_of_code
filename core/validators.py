def is_between(value: str, minimum: int, maximum: int) -> bool:
    if not value.isdigit():
        return False
    int_value = int(value)
    return minimum <= int_value <= maximum
