import logging
import os

from constants import DOWNLOAD_PATH, FOLDERS_TO_CREATE
from helpers.download_checker import DownloadChecker
from helpers.file_funcs import get_file_destinations


def move_file(
    source: str,
    destination: str,
    download_checker: DownloadChecker = None,
) -> None:
    """
    Moves a file from one location to another.

    Args:
        source (str): The source file.
        destination (str): The destination file.
        download_checker (DownloadChecker, optional): A DownloadChecker
            object. Defaults to None.
    """

    if download_checker is not None and download_checker.is_being_downloaded(
        source
    ):
        logging.info(f"{source} is being downloaded; skipping move.")
        return

    if os.path.exists(destination):
        os.remove(destination)

    if os.path.exists(source):
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        try:
            os.rename(source, destination)
        except Exception as e:
            logging.error(f"Error moving {source} to {destination}: {e}")


def main() -> None:
    """
    Moves files from the downloads folder to their respective folders.
    """

    files_in_download_path = os.listdir(DOWNLOAD_PATH)
    download_checker = DownloadChecker(DOWNLOAD_PATH, files_in_download_path)
    logging.info(f"Files to move: {files_in_download_path}")

    file_destinations: dict[str, list[str]] = get_file_destinations(
        files_in_download_path, FOLDERS_TO_CREATE
    )
    logging.info(f"File Destinations: {file_destinations}")

    for folder, files in file_destinations.items():
        folder_destination = os.path.join(DOWNLOAD_PATH, folder)

        for file in files:
            source = os.path.join(DOWNLOAD_PATH, file)
            file_destination = os.path.join(folder_destination, file)
            move_file(source, file_destination, download_checker)
            logging.info(f"Moved {file} to {file_destination}")


if __name__ == "__main__":
    logging.basicConfig(filename="logs.txt", level=logging.INFO)
    main()
