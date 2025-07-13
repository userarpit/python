import json


def complex_encoder(z: complex) -> tuple:
    print(z.__class__)
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name
        raise TypeError(f"Object of type {type_name} is not JSON serializable")


# breakpoint()
json_str = json.dumps(12+12j, default=complex_encoder)
print(json_str)
