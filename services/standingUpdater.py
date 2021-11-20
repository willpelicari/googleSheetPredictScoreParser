from gspread import authorize
from models.player import Player
from sheet_manager import get_document


class StandingUpdater:
    document = None

    def __init__(self,documentName) -> None:
        self.document = get_document(authorize(), documentName)

    def update(self, players, roundName):
        for playerName in players:
            player = Player(playerName, self.document)