import argparse
from ls import get_parser
from typing import Tuple


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of the two numbers.
    """
    return a + b


def sub(a, b):
    """
    Subtract two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The difference between the first and second number.
    """

    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return round(float(a / b), 2)


def get_parser_sub_parser() -> (
    Tuple[argparse.ArgumentParser, argparse._SubParsersAction]
):
    parser = get_parser(
        prog="calc", epil="Thank you for using calc", desc="command line calculator"
    )
    subparsers = parser.add_subparsers(
        title="subcommands", help="Airthmetic operations"
    )

    return parser, subparsers


def create_sub_parser(
    subparsers: argparse._SubParsersAction, arg_template: dict
) -> None:
    add_parser = subparsers.add_parser(
        "add",
        help="add two numbers a and b",
        description="add 2 numbers",
        epilog="Thank you for using Add",
    )
    add_parser.add_argument(**arg_template)
    add_parser.set_defaults(func=add)

    sub_parser = subparsers.add_parser(
        "sub",
        help="subtract two numbers a and b",
        description="subtract 2 numbers",
        epilog="Thank you for using Subtraction",
    )
    sub_parser.add_argument(**arg_template)
    sub_parser.set_defaults(func=sub)

    mul_parser = subparsers.add_parser(
        "mul",
        help="multiple two numbers a and b",
        description="multiply 2 numbers",
        epilog="Thank you for using Multiplication",
    )
    mul_parser.add_argument(**arg_template)
    mul_parser.set_defaults(func=mul)

    div_parser = subparsers.add_parser(
        "div",
        help="divide two numbers a and b",
        description="divide 2 numbers",
        epilog="Thank you for using division",
    )
    div_parser.add_argument(**arg_template)
    div_parser.set_defaults(func=div)


def main() -> None:
    parser, subparsers = get_parser_sub_parser()
    print(type(subparsers))

    arg_template = {
        "dest": "operands",
        "type": float,
        "nargs": 2,
        "metavar": "OPERAND",
        "help": "a numeric value",
        # "epilog":"thank you add",
    }

    create_sub_parser(subparsers, arg_template)

    args = parser.parse_args()

    print(args.func(*args.operands))


if __name__ == "__main__":
    main()
