# import argparse
from ls import get_parser


def add_argument(parser) -> None:
    general = parser.add_argument_group("General output")
    general.add_argument("--name", action="store")
    general.add_argument("--pi", action="store_const", const=3.14)
    general.add_argument("--is-valid", action="store_true")
    general.add_argument("--is-invalid", action="store_false")
    general.add_argument("--item", action="append")
    general.add_argument("--repeated", action="append_const", const=42)
    general.add_argument("--add-one", action="count")
    general.add_argument("--add-another", action="count")
    general.add_argument(
    "--version", action="version", version="%(prog)s 0.1.0"
)

def main() -> None:

    parser = get_parser("actions", "action demo", "Thanks for using %(prog)s!", argument_default=None, allow_abbrev=True)
    add_argument(parser)

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
