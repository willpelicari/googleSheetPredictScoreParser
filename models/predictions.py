from models.cellValue import CellValue
from constants.cellsCoordinates import getWeeksCoordinates
from models.score import Score
from models.week import Week

class Predictions:
    sheet = None
    weeks = None

    def __init__(self, sheet):
        self.sheet = sheet
        values = sheet.get_all_values()
        self.weeks = []
        pivot_row = None
        pivot_col = None
        for week in getWeeksCoordinates():
            newWeek = Week(week)

            if(pivot_row is None):
                pivot_row = 2
                pivot_col = 0
            elif(pivot_col == 12):
                pivot_col = 0
                pivot_row += 18
            elif(pivot_col == 6):
                pivot_col = 12
            elif(pivot_col == 0):
                pivot_col = 6

            for row in range(16):
                home_team = CellValue(values[pivot_row + row][pivot_col], pivot_col + 1, pivot_row + row + 1)
                home_score = CellValue(values[pivot_row + row][pivot_col+1], pivot_col + 2, pivot_row + row + 1)
                away_score = CellValue(values[pivot_row + row][pivot_col+3], pivot_col + 4, pivot_row + row + 1)
                away_team = CellValue(values[pivot_row + row][pivot_col+4], pivot_col + 5, pivot_row + row + 1)

                if(home_team.value == '' or away_team.value == ''):
                    break

                newWeek.scores.append(Score(home_team, home_score, away_score, away_team))

            if(len(newWeek.scores) > 0):
                self.weeks.append(newWeek)