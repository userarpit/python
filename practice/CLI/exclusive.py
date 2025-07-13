# import argparse
from ls import get_parser

parser = get_parser()
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-s", "--silent", action="store_true")

args = parser.parse_args()


print(args.verbose)
print(args.silent)
