
from constants.constants import Constants
from services.scoreParser import ScoreParser

#Update their score
ScoreParser(Constants.SHEET_NAME).parse(Constants.PLAYERS, "Semana 10")
