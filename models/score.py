from models.cellValue import CellValue
from services.writer import Writer

class Score:
    def __init__(self, home_team, home_score, away_score, away_team):
        self.homeTeam = home_team
        self.homeScore = home_score
        self.x = CellValue("x", home_score.col+1, home_score.row+1)
        self.awayTeam = away_team
        self.awayScore = away_score

    def gotVictoryRight(self, officialScore):
        return (
            (int(officialScore.homeScore.value) == int(officialScore.awayScore.value)) & (int(self.homeScore.value) == int(self.awayScore.value)) | #draw
            (int(officialScore.homeScore.value) > int(officialScore.awayScore.value)) & (int(self.homeScore.value) > int(self.awayScore.value)) | #homeWin
            (int(officialScore.homeScore.value) < int(officialScore.awayScore.value)) & (int(self.homeScore.value) < int(self.awayScore.value)) #awayWin
            )

    def colorLine(self, sheet, r, g, b):
        Writer.formatCellRange(Writer, sheet, self.homeTeam.toA1(), self.awayTeam.toA1(), r, g, b)