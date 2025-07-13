import argparse
from pathlib import Path
import datetime


def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name


def get_parser(prog=None, desc=None, epil=None, argument_default=None, allow_abbrev=True):
    parser = argparse.ArgumentParser(
        prog=prog,
        description=desc,
        epilog=epil,
        argument_default=argument_default,
        fromfile_prefix_chars="$",
        allow_abbrev=allow_abbrev,
    )

    return parser


def add_argument(parser) -> None:

    general = parser.add_argument_group("general output")
    general.add_argument("path", nargs="?", default=".", help="take the path to the target directory (default (%(default)s))")
    general.add_argument("--argument-with-a-long-name")

    detailed = parser.add_argument_group("detailed output")
    detailed.add_argument("-l", "--long", action="store_true", help="display detailed directory contents")


def is_directory(target_dir, parser) -> bool:
    if not target_dir.is_dir():
        # print("The target directory does not exists")
        # return False
        parser.exit(10, message="The target directory does not exists")
    return True


def main() -> None:

    parser = get_parser("ls", "List the contents of the directory", "Thanks for using %(prog)s!\n", argument_default=argparse.SUPPRESS, allow_abbrev=False)
    add_argument(parser)

    args = parser.parse_args()
    # print(args)

    target_dir = Path(args.path)
    # print(type(target_dir))

    if is_directory(target_dir, parser):
        for entry in target_dir.iterdir():
            try:
                long = args.long
            except AttributeError:
                long = False

            print(build_output(entry, long=long))


if __name__ == "__main__":
    main()
