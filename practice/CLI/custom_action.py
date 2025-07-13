import argparse
from ls import get_parser

class VerboseStore(argparse.Action):
    def __call__(self, parser, namespace, values, option_string = None):
        # print(type(values))
        values = values.upper()
        setattr(namespace, self.dest, values)


def main() -> None:
    parser = get_parser(prog="Custom Actions", desc="Custom Actions")
    general = parser.add_argument_group("General output")
    general.add_argument("-n", "--name", action=VerboseStore)
    args = parser.parse_args()
    print(args)
    

 
if __name__ == "__main__":
    main()