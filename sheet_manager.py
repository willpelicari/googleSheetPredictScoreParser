import gspread
from oauth2client.service_account import ServiceAccountCredentials
from models.player import Player
import gspread

def authorize():
    scope = ['https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file']
    file_name = 'client_key.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    return gspread.authorize(creds)

def get_document(credential, file_name):
    sheet = credential.open(file_name)
    return sheet

def parse_standings(sheet, player_line) -> Player:
    return sheet.find("Adalba")
    # main_line = sheet.row_values(player_line)
    # player = Player()
    # player.name = main_line.pop(0)
    # player.total_score = main_line.pop(-1)
    # player.full_score = main_line.pop(-1)
    # player.half_score = main_line.pop(-1)
    # player.wins = main_line.pop(-1)
    # player.weeks = main_line
    # return player