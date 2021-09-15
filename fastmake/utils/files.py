import os
from fastmake.utils.lists import flat


def filter_source_files(
    files: list,
    root_path: str = None,
    prefix: str = '.c',
) -> list:
    return list(
        map(
            lambda file: f'{root_path}/{file}',
            filter(lambda file: file.endswith(prefix), files),
        )
    )


def filter_directories(entries: list) -> list:
    return list(filter(lambda entry: not '.' in entry, entries))


def get_raw_source_files(
    source_dir: str,
    source_files: list,
    header_files: list,
    filetype: str,
):
    directory_entries = os.listdir(source_dir)
    directories = filter_directories(directory_entries)

    source_files.append(
        filter_source_files(
            directory_entries, source_dir, '.c' if filetype == 'c' else '.cpp'
        )
    )
    header_files.append(
        filter_source_files(
            directory_entries, source_dir, '.h' if filetype == 'c' else '.hh'
        )
    )

    for directory in directories:
        get_raw_source_files(
            source_dir + '/' + directory, source_files, header_files, filetype
        )


def get_source_files_list(source_dir: str, filetype: str) -> tuple:
    source_files = []
    header_files = []

    get_raw_source_files(
        source_dir,
        source_files,
        header_files,
        filetype=filetype,
    )

    source_files = flat(source_files)
    header_files = flat(header_files)

    return source_files, header_files
