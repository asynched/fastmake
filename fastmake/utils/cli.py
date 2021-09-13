from fastmake.utils.logger import Logger
from fastmake.utils.colors import Colors as Colors


def parse_cli_arguments(args: list) -> dict:
    FLAGS_MAP = {
        't': 'target',
        'c': 'compiler',
        'f': 'flags',
        'e': 'executable',
        'h': 'help',
    }

    options = {}

    for i in range(0, len(args), 2):
        key, value = args[i : i + 2]

        options[FLAGS_MAP[key[1:]]] = value

    return options


def print_logo():
    print(
        f"""
{Colors.RED}███████╗ █████╗ ███████╗████████╗███╗   ███╗ █████╗ ██╗  ██╗███████╗{Colors.RESET}
{Colors.MAGENTA}██╔════╝██╔══██╗██╔════╝╚══██╔══╝████╗ ████║██╔══██╗██║ ██╔╝██╔════╝{Colors.RESET}
{Colors.YELLOW}█████╗  ███████║███████╗   ██║   ██╔████╔██║███████║█████╔╝ █████╗{Colors.RESET} 
{Colors.GREEN}██╔══╝  ██╔══██║╚════██║   ██║   ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝{Colors.RESET}
{Colors.CYAN}██║     ██║  ██║███████║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗{Colors.RESET}
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
        """
    )


def show_cli_options():
    print_logo()

    Logger.base(
        Colors.BG_YELLOW,
        "TARGET",
        "Root folder of your project (where all you're files are stored)\n"
        "> Flag: -t\n"
        "> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER\n",
    )

    Logger.base(
        Colors.BG_GREEN,
        "COMPILER",
        "Chosen compiler to compile your program (optional, defaults to gcc)\n"
        "> Flag: -c\n"
        "> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER -c gcc # Use the GCC compiler\n",
    )

    Logger.base(
        Colors.BG_GREEN,
        "FLAGS",
        "Add additional flags to the build command (optional, defaults to ENABLED)\n",
        "> Flag: -f\n"
        "> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER -f -- # Disables the additional flags\n",
    )

    Logger.base(
        Colors.BG_GREEN,
        "EXECUTABLE",
        "Add a name to your generated executable (optional, defaults to 'main')\n"
        "> Flag: -e\n"
        "> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER -e my_program.exe # Renames the executable to 'my_program.exe'",
    )
