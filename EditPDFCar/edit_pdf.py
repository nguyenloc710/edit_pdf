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
    # create_directory(Path(pdf_result).parent)  # Create the directory if it doesn't exist
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


stamp("2.pdf", "logo.pdf",
      "21.pdf")
