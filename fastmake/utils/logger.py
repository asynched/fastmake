from fastmake.utils.colors import Colors


class Logger:
    def base(background: str, prefix, *args):
        print(
            background + Colors.BLACK + f"[{prefix}]" + Colors.RESET,
            *args,
        )

    def info(*args):
        print(
            Colors.BG_YELLOW + Colors.BLACK + "[INFO]" + Colors.RESET,
            *args,
        )

    def error(*args):
        print(
            Colors.BG_RED + Colors.BLACK + "[ERROR]" + Colors.RESET,
            *args,
        )

    def success(*args):
        print(
            Colors.BG_GREEN + Colors.BLACK + "[SUCCESS]" + Colors.RESET,
            *args,
        )
