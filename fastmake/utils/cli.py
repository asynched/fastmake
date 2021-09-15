from fastmake.utils.logger import Logger
from fastmake.utils.colors import Colors


def parse_cli_arguments(args: list) -> dict:
    FLAGS_MAP = {
        't': 'target',
        'c': 'compiler',
        'f': 'flags',
        'e': 'executable',
        'h': 'help',
        'ft': 'filetype',
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
        'TARGET',
        'Root folder of your project (where all your files are stored)\n'
        '-> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER\n'
        '-> Flag: -t\n',
    )

    Logger.base(
        Colors.BG_GREEN,
        'COMPILER',
        'Chosen compiler to compile your program (optional, defaults to gcc)\n'
        '-> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER -c gcc # Use the GCC compiler\n'
        '-> Flag: -c\n',
    )

    Logger.base(
        Colors.BG_GREEN,
        'FLAGS',
        'Add additional flags to the build command (optional, defaults to ENABLED)\n'
        '-> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER -f -- # Disables the additional flags\n'
        '-> Flag: -f\n',
    )

    Logger.base(
        Colors.BG_GREEN,
        'EXECUTABLE',
        'Add a name to your generated executable (optional, defaults to "main")\n'
        '-> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER -e my_program.exe # Renames the executable to "my_program.exe"\n'
        '-> Flag: -e\n',
    )

    Logger.base(
        Colors.BG_GREEN,
        'FILE TYPE',
        'Add a file type to your specific project (.cpp for example, defaults to .c)\n'
        '-> Example: $ fastmake -t $YOUR_PROGRAM_FOLDER -e my_program.exe -ft cpp # Sets the file type to .cpp files\n'
        '-> Flag: -ft\n',
    )
