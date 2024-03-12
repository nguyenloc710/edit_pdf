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


x = "C:/CFM/DE/account-statistic-service-anh-hieu/CarDoctor AutoISM/"
y = "C:/CFM/DE/account-statistic-service-anh-hieu/CarEditPDF-TEST/"
if __name__ == "__main__":
    path_files = get_all_files_in_folder("C:/CFM/DE/account-statistic-service-anh-hieu/CarDoctor AutoISM/VINFAST")
    threading_path_files = []
    count = 1
    for index, path_file in enumerate(path_files):
        print(index, ": ", path_file)
        threading_path_files.append(path_file)
        if count % 10 == 0:
            t1 = threading.Thread(
                target=stamp(threading_path_files[0], "logo.pdf", threading_path_files[0].replace(x, y)), name='t1')
            t2 = threading.Thread(
                target=stamp(threading_path_files[1], "logo.pdf", threading_path_files[1].replace(x, y)), name='t2')
            t3 = threading.Thread(
                target=stamp(threading_path_files[2], "logo.pdf", threading_path_files[2].replace(x, y)), name='t3')
            t4 = threading.Thread(
                target=stamp(threading_path_files[3], "logo.pdf", threading_path_files[3].replace(x, y)), name='t4')
            t5 = threading.Thread(
                target=stamp(threading_path_files[4], "logo.pdf", threading_path_files[4].replace(x, y)), name='t5')
            t6 = threading.Thread(
                target=stamp(threading_path_files[5], "logo.pdf", threading_path_files[5].replace(x, y)), name='t6')
            t7 = threading.Thread(
                target=stamp(threading_path_files[6], "logo.pdf", threading_path_files[6].replace(x, y)), name='t7')
            t8 = threading.Thread(
                target=stamp(threading_path_files[7], "logo.pdf", threading_path_files[7].replace(x, y)), name='t8')
            t9 = threading.Thread(
                target=stamp(threading_path_files[8], "logo.pdf", threading_path_files[8].replace(x, y)), name='t9')
            t10 = threading.Thread(
                target=stamp(threading_path_files[8], "logo.pdf", threading_path_files[8].replace(x, y)), name='t10')
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            t9.start()
            t10.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            t7.join()
            t8.join()
            t9.join()
            t10.join()
            count = 0
            threading_path_files = []
        count += 1
