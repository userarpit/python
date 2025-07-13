import json


def decode_complex(data: dict) -> complex:
    if "__complex__" in data:
        # print(data)
        return complex(data["real"], data["imaginary"])
    return data


if __name__ == "__main__":
    with open("../data/input_data.json") as complex_data:
        data = complex_data.read()
        # print(data)
        complex_data_str = json.loads(data, object_hook=decode_complex)

    print(type(complex_data_str))
    print(complex_data_str)
