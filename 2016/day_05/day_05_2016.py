import hashlib


def calculate_matching_hash(hash_root, zeros, lowest_value=0):
    password = []
    while len(password) < 8:
        text_to_hash = f"{hash_root}{lowest_value}"
        h = hashlib.md5(text_to_hash.encode("utf-8")).hexdigest()
        if h.startswith("0" * zeros):
            password.append(h[5])
        lowest_value += 1
    return "".join(c for c in password)


def positional_passowrd(hash_root, zeros, lowest_value=0):
    password = ["_"] * 8
    while any(c == "_" for c in password):
        text_to_hash = f"{hash_root}{lowest_value}"
        h = hashlib.md5(text_to_hash.encode("utf-8")).hexdigest()
        if h.startswith("0" * zeros):
            try:
                pos = int(h[5])
                if pos in range(8) and password[pos] == "_":
                    password[pos] = h[6]
            except ValueError:
                ...
        lowest_value += 1
    return "".join(c for c in password)


if __name__ == "__main__":

    hash_root = "wtnhxymk"

    print(f"PART 01: The password is: {calculate_matching_hash(hash_root, 5)}")
    print(f"PART 02: The password is: {positional_passowrd(hash_root, 5)}")
