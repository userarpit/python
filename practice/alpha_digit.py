_string = "Hello123World456"


def separate_alpha_digit(input: str) -> None:
    _alpha = "".join(filter(str.isalpha, input))
    _digit = "".join(filter(str.isdigit, input))

    return _alpha, _digit


if __name__ == "__main__":
    alpha, digit = separate_alpha_digit(_string)
    print(alpha)
    print(digit)
