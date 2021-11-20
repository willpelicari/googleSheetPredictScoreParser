import json


class StandingWeek:
    description = None
    total = None
    wins = None
    half_score = None
    full_score = None

    def __init__(self, sum_week, wins, half_score, full_score):
        self.total = sum_week
        self.wins = wins
        self.half_score = half_score
        self.full_score = full_score

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)