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