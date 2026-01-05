import gmpy2

def calculate_is_prime(n: int) -> bool:
    return bool(gmpy2.is_prime(gmpy2.mpz(n)))
    
def convert_number_to_binary_representation(n: int, max_places: int = 63) -> list[int]:
    s = bin(n)[2:]

    if len(s) > max_places:
        raise ValueError(f"n has more than {max_places} binary digits")

    s = s.zfill(max_places)
    return [int(ch) for ch in s]

def convert_number_to_decimal_representation(n: int, max_places: int = 19) -> list[int]:
    if n < 0:
        raise ValueError("n must be non-negative")

    s = str(n)
    if len(s) > max_places:
        raise ValueError(f"n has more than {max_places} decimal digits")

    s = s.zfill(max_places)
    return [int(ch) for ch in s]