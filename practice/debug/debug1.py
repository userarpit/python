import os
# import pdb


def get_path(filename):
    """
    Splits the given filename into head and tail components, and returns the head.
    
    Args:
        filename (str): The path to be split.

    Returns:
        str: The head component of the filename.
    """
    print()
    a = 10
    # pdb.run("a=10")
    for _ in range(10):
        a += 50
    head, tail = os.path.split(filename)
    b = 7
    return head


def main():
    breakpoint()
    filename = __file__
    print(f"path = {get_path(filename)}")


if __name__ == "__main__":
    main()
