import argparse

parser = argparse.ArgumentParser()

# parser.add_argument("--veggies", nargs="+")
# parser.add_argument("--fruits", nargs="*")
parser.add_argument("fruits", action="store")
parser.add_argument("remaindervalues", nargs=argparse.REMAINDER)

args = parser.parse_args()

print(args)
