from prime import is_prime

def generate_prime_number():
    while True:
        for number in range(2, 1000):
            if is_prime(number):
                return_val = yield number
                if return_val == "exit":
                    return


if __name__ == "__main__":
    total_prime_number = int(input("How many prime number to generate? "))
    # breakpoint()
    number = 0
    prime_gen = generate_prime_number()
    while True:
        prime_number = next(prime_gen)
        print(f"Generated Prime Number: {prime_number}")
        number += 1

        try:
            if number == total_prime_number:
                prime_gen.send("exit")
        except StopIteration:
            print("No more prime numbers to generate.")
            break

