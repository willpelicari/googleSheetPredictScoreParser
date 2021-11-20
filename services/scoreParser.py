from constants.constants import Constants
from models.player import Player
from models.predictions import Predictions
from sheet_manager import authorize, get_document

class ScoreParser:
    document = None
    def __init__(self, documentName) -> None:
        self.document = get_document(authorize(), documentName)

    def parse(self, players, roundName):
        results = Predictions(self.document.worksheet(Constants.RESULTS_PAGE))

        for playerName in players:
            player = Player(playerName, self.document)
            print("Score {0}:".format(playerName))
            for weekKey, week in enumerate(results.weeks):
                total_week = 0
                for scoreKey, officialScore in enumerate(week.scores):
                    if(officialScore.homeScore.value == ''):
                        continue;
                    playerScore = player.predictions.weeks[weekKey].scores[scoreKey]
                    gotItRight = False
                    log = "\t{0} {1} x {2} {3} - ".format(playerScore.homeTeam.value, playerScore.homeScore.value, playerScore.awayScore.value, playerScore.awayTeam.value)
                    if(playerScore.gotVictoryRight(officialScore)):
                        log += " acertou quem venceu"
                        total_week += 1
                        if(week.name == roundName):
                            playerScore.colorLine(player.predictions.sheet, 0.85, 0.918, 0.827)
                        gotItRight = True
                    else:
                        if(week.name == roundName):
                            playerScore.colorLine(player.predictions.sheet, 0.957, 0.8, 0.8)
                    
                    if(playerScore.homeScore.value == officialScore.homeScore.value):
                        log += " acertou meio-placar!"
                        total_week += 2
                        if(gotItRight):
                            if(week.name == roundName):
                                playerScore.homeScore.color(player.predictions.sheet, 0.204, 0.659, 0.325)
                        else:
                            if(week.name == roundName):
                                playerScore.homeScore.color(player.predictions.sheet, 0.912, 0.263, 0.208)
                    if(playerScore.awayScore.value == officialScore.awayScore.value):
                        log += " acertou meio-placar!"
                        total_week += 2
                        if(gotItRight):
                            if(week.name == roundName):
                                playerScore.awayScore.color(player.predictions.sheet, 0.204, 0.659, 0.325)
                        else:
                            if(week.name == roundName):
                                playerScore.awayScore.color(player.predictions.sheet, 0.912, 0.263, 0.208)
                    print(log)
                # print("{0} -> {1}".format(week.name, total_week))
                player.standing.total_score += total_week
            
            print("{0} - Total Score: {1}".format(playerName, player.standing.total_score))