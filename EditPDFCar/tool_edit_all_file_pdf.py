import os
import threading
from pathlib import Path
from typing import Union, Literal, List

from PyPDF2 import PdfWriter, PdfReader


def create_directory(path):
    directory = Path(path)
    if not directory.is_dir():
        directory.mkdir(parents=True)


def stamp(
        content_pdf: Path,
        stamp_pdf: Path,
        pdf_result: Path,
        page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    create_directory(Path(pdf_result).parent)  # Create the directory if it doesn't exist
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[0]

    writer = PdfWriter()

    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        content_page.mergeTranslatedPage(image_page,
                                         (float(content_page.mediaBox[2]) - (float(content_page.mediaBox[2]) * 0.35)),
                                         (float(content_page.mediaBox[3]) - (float(content_page.mediaBox[3]) * 0.33)))
        writer.add_page(content_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)


def get_all_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file).replace("\\", "/"))
    return file_paths

if __name__ == "__main__":
    path_files = get_all_files_in_folder("C:/CFM/DE/account-statistic-service-anh-hieu/CarDoctor AutoISM")
    for index, path_file in enumerate(path_files):
        print(index)
        stamp(path_file, "logo.pdf",
              path_file.replace("C:/CFM/DE/account-statistic-service-anh-hieu/CarDoctor AutoISM/",
                                "C:/CFM/DE/account-statistic-service-anh-hieu/CarEditPDF/"))
