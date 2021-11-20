import time
from gspread_formatting import *

class Writer:
    counter_cooldown = 0

    def formatCellRange(self, sheet, begin, end, red, green, blue):
        # return
        fmt = CellFormat(backgroundColor=Color(red, green, blue))
        format_cell_range(sheet, "{0}:{1}".format(begin, end), fmt)
        self.cooldown(self)

    def format(self, sheet, cell, red, green, blue):
        # return
        sheet.format("{0}:{1}".format(cell, cell), 
        {
            "backgroundColor": {
            "red": red,
            "green": green,
            "blue": blue
        }})
        self.cooldown(self)

    def updateCell(self, sheet, row, col, value):
        sheet.update_cell(row, col, value)
        self.cooldown(self)

    def cooldown(self):
        if(self.counter_cooldown == 60):
            self.counter_cooldown = 0
            print("Cooling down. waiting 60s")
            time.sleep(60)
            print("Resuming work!")
        else:
            self.counter_cooldown += 1
            # print("cooldown counter: {0} out of 60".format(self.counter_cooldown))