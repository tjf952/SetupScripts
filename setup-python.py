#!/usr/bin/env python3

"""Python file generator.

This module sets up python files given command line arguments.

Usage:
    Executed from command line.

        $ python3 make-python.py <args>

Arguments:
    name: Required argument to set the name of the output file.
    -c <int>: Optional argument to generate n template classes.
    -f <int>: Optional argument to generate m template functions.
    -m: Optional boolean argument to remove default main function
"""

import argparse

header_docstring = f"""#!/usr/bin/env python3

\"\"\"_title_

_description_

Usage: $ python3 _name_ <_args_>

Arguments:
    -_param_ <type>: _description_
\"\"\"

### Import Statements ###

import os

print(f\"Hello {{os.getlogin()}}\")
"""

class_template = """class _name_():
    \"\"\"_title_

    _description_
    \"\"\"

    def __init__(self, _param_: type):
        \"\"\"_description_

        Args:
            _param_ (type): _description_
        \"\"\"
        self.attr = _param_

    def example_method(self, _param_: type) -> type:
        \"\"\"_description_

        Args:
            _param_ (type): _description_

        Returns:
            type: _description_
        \"\"\"
        self.attr = _param_
        return self.attr

    def __special__(self):
        \"\"\"_description_

        Returns:
            type: _description_
        \"\"\"
        return self.attr
"""

function_template = """def _name_(_param_: type) -> type:
    \"\"\"_description_

    Args:
        _param_ (type): _description_

    Returns:
        type: _description_
    \"\"\"
    return _param_
"""

main_template = """if __name__ == "__main__":
    print(\"This is a template python file.\")
"""


def arg_parser() -> list:
    """Argument Parser"""
    parser = argparse.ArgumentParser(description="Generates template python file.")
    parser.add_argument(
        "name", metavar="name", type=str, help="Name of the output file."
    )
    parser.add_argument("-c", type=int, help="Number of classes.")
    parser.add_argument("-f", type=int, help="Number of functions.")
    parser.add_argument(
        "-m", action="store_false", help="Removes default main function."
    )

    args = parser.parse_args()

    return args


def generate_object(name: str, object_type: int) -> str:
    """Class template.

    Args:
        name (str): Adds the name for the class
        object_type (int): 1 for class else 0 for function.

    Returns:
        str: Templated string with unique name.
    """
    template = class_template if object_type else function_template

    return template.replace("_name_", name)


def generate(name: str, u_class: int = 0, u_func: int = 0, u_main: bool = True) -> str:
    """Generator.

    Args:
        name (str): Required argument to set the name of the output file.
        u_class (int, optional): Set to n to generate template classes. Defaults to 0.
        u_func (int, optional): Set to m to generate template functions. Defaults to 0.
        u_main (int, optional): Set to False to remove main function. Defaults to True.

    Returns:
        str: Completed template with n classes and m functions.
    """
    template = header_docstring.replace("_name_", name)

    if u_class:
        template += "\n\n###Classes ###\n"
        for i, task in enumerate(range(u_class)):
            template += "\n\n"
            template += generate_object(f"Class{i+1}", 1)

    if u_func:
        template += "\n\n### Functions ###\n"
        for i, task in enumerate(range(u_func)):
            template += "\n\n"
            template += generate_object(f"Class{i+1}", 0)

    if u_main:
        template += f"\n\n{main_template}"

    return template


if __name__ == "__main__":
    args = arg_parser()
    if not args.name.endswith(".py"):
        args.name = f"{args.name}.py"
    print(f"Arguments: {args}")
    template = generate(args.name, args.c, args.f, args.m)
    with open(args.name, "w") as f:
        f.write(template)
