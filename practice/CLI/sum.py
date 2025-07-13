import argparse
from ls import get_parser

parser=get_parser()

parser.add_argument("numbers", nargs="+", type=float)
args = parser.parse_args()

print(sum(args.numbers))
