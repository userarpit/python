# import argparse
from ls import get_parser


def main() -> None:
    parser = get_parser()

    parser.add_argument("--dividend", type=float)
    parser.add_argument("--divisor", type=float)
    parser.add_argument("--cor", nargs=2)

    args = parser.parse_args()

    print(args.dividend / args.divisor)
    
    
    print(args)


if __name__ == "__main__":
    main()


