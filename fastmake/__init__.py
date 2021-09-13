import os, sys
from pathlib import Path
from typing import Type
from fastmake.utils.files import get_source_files_list
from fastmake.utils.cli import parse_cli_arguments, show_cli_options
from fastmake.utils.logger import Logger

ROOT_PATH = Path().cwd()


def generate_build_command(
    compiler: str,
    flags: str,
    options: dict,
) -> str:
    executable = options['executable']
    source_files = options['source_files']
    header_files = options['header_files']
    compiler_flags = ''

    if flags == 'ENABLED':
        compiler_flags += ' '.join(['-w', '-Wall', '-ansi', '-pedantic'])

    return f"{compiler} {source_files} {header_files} {compiler_flags} -o {executable}"


def execute(
    target: str,
    compiler: str = 'gcc',
    flags: str = 'ENABLED',
    executable: str = 'main',
    show_build_command=False,
):

    SOURCE_FILES_PATH = ROOT_PATH / Path(target)

    source_files, header_files = get_source_files_list(str(SOURCE_FILES_PATH))

    source_files = " ".join(source_files)
    header_files = " ".join(header_files)

    build_command = generate_build_command(
        compiler,
        flags,
        {
            'source_files': source_files,
            'header_files': header_files,
            'executable': executable,
        },
    )

    if show_build_command:
        print(build_command)

    Logger.info(f"Generating executable '{executable}'")
    os.system(build_command)
    Logger.success("Build succeeded")


def run():
    args = sys.argv[1:]

    if '-h' in args:
        show_cli_options()
        return

    parsed_arguments = parse_cli_arguments(args)

    try:
        execute(**parsed_arguments)
    except TypeError as error:
        Logger.error(
            "Please provide a target folder\n" "$ fastmake -t $YOUR_PROGRAM_FOLDER\n"
        )
    except Exception as error:
        print(type(error))
        print(error)
