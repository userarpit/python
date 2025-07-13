def repeater_generator(item, times):
    """
    A generator that repeats an item a specified number of times.

    :param item: The item to be repeated.
    :param times: The number of times to repeat the item.
    """
    for _ in range(times):
        yield item

# Example usage:
if __name__ == "__main__":
    for value in repeater_generator("Hello", 5):
        print(value)