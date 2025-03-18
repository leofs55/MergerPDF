import os
import PyPDF2 as pdf


class Merger:

    def __init__(self, path_in: str, path_out: str, name_file: str):
        self.PATH_INPUT: str = path_in
        self.PATH_OUTPUT: str = path_out
        self.name_file: str = name_file

    def merge_files(self):
        files = os.listdir(self.PATH_INPUT)
        merge = pdf.PdfMerger()

        if files:
            for file in files:
                merge.append(f"{self.PATH_INPUT}\\{file}")
            merge.write(f"{self.PATH_OUTPUT}/{self.name_file}.pdf")
        merge.close
