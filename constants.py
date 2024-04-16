import os
import winreg


DOWNLOAD_PATH = ""
FOLDERS_TO_CREATE = {
    "Images": "jpg jpeg png gif bmp svg tiff heic",
    "Survey Scans": "pdf",
    "Compressed": "zip rar 7z tar gz",
    "Misc": "*",
    "Word Docs": "doc docx",
    "PDFs": "pdf",
    "CAD Files": "dwg dxf ini bak dwl dwl2",
    "ASCII Files": "asc",
    "Python Files": "py pyw ipynb json",
}


def get_download_path() -> str:
    """
    Returns the default dowloads path for windows.

    Args:
        None

    Returns:
        str: The default downloads path for windows.
    """
    if os.name == "nt":
        sub_key = (
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        )
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    return os.path.join(os.path.expanduser("~"), "Downloads")


def create_required_folders(
    download_path: str, folders_to_create: dict
) -> None:
    """
    Creates the destination folder if it doesn't exist.

    Args:
        download_path (str): The path to the downloads folder.
        folders_to_create (dict): A dictionary of folders to create.

    Returns:
        None
    """

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for folder in folders_to_create.keys():
        if not os.path.exists(os.path.join(download_path, folder)):
            os.mkdir(os.path.join(download_path, folder))


DOWNLOAD_PATH = get_download_path()
create_required_folders(DOWNLOAD_PATH, FOLDERS_TO_CREATE)
