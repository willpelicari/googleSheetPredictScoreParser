import json
from constants.constants import Constants
from models.predictions import Predictions

from models.standing import Standing

class Player:
    standing = None
    predictions = None

    def __init__(self, given_name, file):
        self.standing = Standing(given_name, file.worksheet(Constants.SUMMARY_PAGE))
        self.predictions = Predictions(file.worksheet(given_name))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)
