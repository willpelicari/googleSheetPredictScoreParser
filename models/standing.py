import json
from models.standingWeek import StandingWeek


class Standing:
    __referenceCell = None
    sum_wins = 0
    sum_half_score = 0
    sum_full_score = 0
    total_score = 0

    weeks = []

    def __init__(self, given_name, standing_sheet):
        self.__referenceCell = standing_sheet.find(given_name)

        #Main Line
        main_line = standing_sheet.row_values(self.__referenceCell.row)
        main_line.pop(0)
        self.total_score = main_line.pop(-1)
        self.sum_full_score = main_line.pop(-1)
        self.sum_half_score = main_line.pop(-1)
        self.sum_wins = main_line.pop(-1)

        self.total_score = 0

        #Weeks
        wins_line = standing_sheet.row_values(self.__referenceCell.row + 1)
        half_score_line = standing_sheet.row_values(self.__referenceCell.row + 2)
        full_score_line = standing_sheet.row_values(self.__referenceCell.row + 3)
        wins_line.pop(0)
        half_score_line.pop(0)
        full_score_line.pop(0)

        for idx, wins in enumerate(wins_line):
            if(idx < len(wins_line)):
                self.weeks.append(StandingWeek(main_line[idx], wins, half_score_line[idx], full_score_line[idx]))

        self.weeks.pop()

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)
