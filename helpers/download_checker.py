import os
from typing import Dict, Tuple, List


class DownloadChecker:
    def __init__(self, download_folder: str, initial_files: List[str] = None):
        # File path -> (file size, last modified time)
        if not os.path.isdir(download_folder):
            raise ValueError(f"{download_folder} is not a directory")

        self.download_folder = download_folder
        self.file_info: Dict[str, Tuple[int, float]] = {}

        if initial_files is not None:
            for file in initial_files:
                file_path = self.get_full_file_path(file)
                self.file_info[file] = (
                    os.path.getsize(file_path),
                    os.path.getmtime(file_path),
                )

    def is_being_downloaded(self, file: str) -> bool:
        """
        Returns True if the file is being downloaded. A file is being
        downloaded if its size or last modified time has changed.

        Args:
            file (str): the file to check.

        Returns:
            bool: True if the file is being downloaded.
        """
        file_name = file.split("\\")[-1]

        if file_name not in self.file_info.keys():
            print("File not in existing files.")
            return False

        if not os.path.exists(file):
            print("File does not exist.")
            return False

        file_size = os.path.getsize(file)
        file_modified_time = os.path.getmtime(file)

        previous_file_size = self.file_info[file_name][0]
        previous_file_modified_time = self.file_info[file_name][1]

        file_size_changed = file_size != previous_file_size
        file_modified_time_changed = (
            file_modified_time != previous_file_modified_time
        )

        if file_size_changed or file_modified_time_changed:
            self.file_info[file_name] = (file_size, file_modified_time)
            return True

    def get_full_file_path(self, file: str) -> str:
        """
        Returns the full file path.

        Args:
            file (str): The file to get the full file path for.

        Returns:
            str: The full file path.
        """
        return os.path.join(self.download_folder, file)
