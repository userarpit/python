import argparse
from ls import get_parser




def main() -> None:
    parser = get_parser()

    parser.add_argument("--weekday", type=int, choices=range(1, 8), default=1)
    args = parser.parse_args()

    print(args)

if __name__ == "__main__":
    main()