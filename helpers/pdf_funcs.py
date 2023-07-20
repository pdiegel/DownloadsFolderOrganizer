import re
from typing import Dict, Iterable, Set


def is_survey_scan(pdf: str) -> bool:
    """
    Returns True if the pdf is a valid survey scan. A valid survey scan
    is a pdf with a filename that begins with exactly 8 digits.

    Args:
        pdf (str): The pdf to check.

    Returns:
        bool: True if the pdf is a valid survey scan.
    """
    return bool(re.match(r"^\d{8}[^0-9]", pdf))


def get_pdf_destinations(pdfs: Iterable[str]) -> Dict[str, Set[str]]:
    """
    Returns a dictionary of pdfs and their destination folders.

    Args:
        pdfs (Iterable[str]): An iterable of pdfs.

    Returns:
        Dict[str, Set[str]]: A dictionary of pdfs and their destination folders.
    """
    pdf_destinations = {"Survey Scans": set(), "PDFs": set()}

    for pdf in pdfs:
        if is_survey_scan(pdf):
            pdf_destinations["Survey Scans"].add(pdf)
        else:
            pdf_destinations["PDFs"].add(pdf)

    return pdf_destinations
