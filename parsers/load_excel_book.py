from openpyxl import load_workbook
import os
import sys


def load_excel_book(filepath):
    abspath = os.path.abspath(filepath)
    workbook = load_workbook(filename = abspath)
    print()

    return workbook


