import argparse  # pragma: no cover

from . import BaseClass  # pragma: no cover
from . import base_function  # pragma: no cover
from . import the_purpose_of_all_this_v2  # pragma: no cover
from . import print_channel_slugs, print_series_slugs


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m plutoalert` and `$ plutoalert `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(
        description="plutoalert.",
        epilog="Enjoy the plutoalert functionality!",
    )
    # This is required positional argument
    parser.add_argument(
        "command",
        type=str,
        help="Try StarTrek, ChannelSlugs or SeriesSlugs",
        default="StarTrek",
    )
    # This is optional named argument
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        help="The Message",
        default="Hello",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()

    print(f"command={args.command}")
    if args.verbose:
        print("Verbose mode is on.")

    if args.command == "StarTrek":
        the_purpose_of_all_this_v2(print_count=args.verbose)
        return
    if args.command == "ChannelSlugs":
        print_channel_slugs(titles_too=args.verbose)
        return
    if args.command == "SeriesSlugs":
        print_series_slugs(titles_too=args.verbose)
        return

    print("Executing main function")
    base = BaseClass()
    print(base.base_method())
    print(base_function())
    print("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
