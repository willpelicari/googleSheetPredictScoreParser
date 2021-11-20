import gspread
from services.writer import Writer


class CellValue:
    def __init__(self, value, col, row):
        self.value = value
        self.col = col
        self.row = row

    def update(self, sheet):
        Writer.format(Writer, sheet, self.row, self.col, self.value)
    
    def toA1(self):
        return gspread.utils.rowcol_to_a1(self.row, self.col)

    def color(self, sheet, r, g, b):
        Writer.format(Writer, sheet, self.toA1(), r, g, b)