from typing import Dict, Iterable, Set

from helpers.pdf_funcs import get_pdf_destinations


def get_pdf_files(files: Iterable[str]) -> Set[str]:
    """
    Returns a set of PDF file names from the given files.

    Args:
        files (Iterable[str]): An iterable of file paths.

    Returns:
        Set[str]: A set of PDF file names.
    """
    return {file for file in files if file.lower().endswith(".pdf")}


def get_non_pdf_file_destinations(
    files: Iterable[str],
    file_schema: Dict[str, str],
) -> Dict[str, Set[str]]:
    """
    Returns a dictionary of non-PDF files and their destination folders.

    Args:
        files (Iterable[str]): An iterable of file paths.
        file_schema (Dict[str, str]): A dictionary of folders and their
            file extensions.

    Returns:
        Dict[str, Set[str]]: A dictionary of non-PDF files and their
            destination folders.
    """
    file_destinations = {folder: set() for folder in file_schema.keys()}

    for file in files:
        file_lower = file.lower()
        for folder, extensions in file_schema.items():
            if file in file_schema.keys():
                continue
            if file_lower.endswith(tuple(extensions.split())):
                file_destinations[folder].add(file)
            else:
                file_destinations["Misc"].add(file)

    return file_destinations


def get_file_destinations(
    files: Iterable[str],
    file_schema: Dict[str, str],
) -> Dict[str, Set[str]]:
    """
    Returns a dictionary mapping destination folders to sets of files.

    Args:
        files (Iterable[str]): An iterable of file paths.
        file_schema (Dict[str, str]): A dictionary of folders and their
            file extensions.

    Returns:
        Dict[str, Set[str]]: A dictionary mapping destination folders
            to sets of files.
    """
    pdf_files = get_pdf_files(files)
    non_pdf_files = set(files) - pdf_files

    file_destinations = get_non_pdf_file_destinations(
        non_pdf_files, file_schema
    )
    file_destinations.update(get_pdf_destinations(pdf_files))

    return file_destinations
