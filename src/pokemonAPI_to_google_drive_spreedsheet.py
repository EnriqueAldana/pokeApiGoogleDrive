import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from datetime import datetime
from pip._vendor import requests
import getopt
import sys


class Cell:
    def __init__(self, name, url, update):
        self.name = name
        self.url = url
        self.update = update


def get_request(url, parameters):
    response = requests.get(url, parameters)
    print('Response status:' + str(response.status_code))
    pokemons = response.json()['results']
    print("The pokemon records according the parameters: " + str(parameters))
    jprint(pokemons)
    return pokemons


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def update_spreadsheet_at_googel_drive(file_name,sh_name,data):
    print("Accessing at google Drive... ")
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    print("Find a workbook by name called " + sh_name + " and open the first sheet ...")
    sh = client.open(sh_name)
    worksheet = sh.get_worksheet(0)
    pokemon_list = []
    for d in data:
        cell = Cell(d['name'], d['url'], "")
        is_there = looking_value(worksheet, cell)
        if is_there > 0:
            cell.update = str(datetime.now())

        pokemon_list.append(cell)
    i = 0
    for cell in pokemon_list:
        i = i + 1
        print("updating pokemon name as " + cell.name)
        worksheet.update_cell(i, 1, cell.name)
        worksheet.update_cell(i, 2, cell.url)
        worksheet.update_cell(i, 3, cell.update)
    print("The worksheet called " + sh_name + " has been updated")


def looking_value(worksheet, cell):
    ret = -1
    try:
        worksheet.find(str(cell.name))
        ret = 1
    except gspread.exceptions.CellNotFound:
        ret = 0
    return ret


def runProgram(credentials_file_name,spreadsheet_name,url_pokemon_source,offset_value):

    today = datetime.now()
    print('Date of ejecution of this script :  ' + str(today))
    #credentials_file_name = 'PokemonAPIPython-83ebb5088725.json'
    #spreadsheet_name = 'A new PokemonAPI spreadsheet'
    #url_pokemon_source = 'https://pokeapi.co/api/v2/pokemon/'
    #offset_value = 0    # 20
    limit_value = 20     # it is a constant
    parameters = {
        "offset": str(offset_value),
        "limit": str(limit_value)
    }
    # getRequest('https://pokeapi.co/api/v2/pokemon/?offset=' +offset+'&limit=20')
    data = get_request(url_pokemon_source, parameters)
    update_spreadsheet_at_googel_drive(credentials_file_name, spreadsheet_name,data)


def main(argv):
    credentials_file_name = None
    spreadsheet_name = None
    url_pokemon_source = None
    offset_value = None
    arguments = 0
    try:
        # opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        opts, args = getopt.getopt(argv, "h:n:p:f:k:",
                                   ["credentials_file_name=", "spreadsheet_name=", "url_pokemon_source=", "offset_value="])
        arguments = args
    except getopt.GetoptError:
        print(
            "python pokemonAPI_to_google_drive_spreedsheet.py -n 'PokemonAPIPython-83ebb5088725.json'  -p 'A new PokemonAPI spreadsheet' -f 'https://pokeapi.co/api/v2/pokemon/' -k 0")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':  # Requested Help to use it
            print('This is the help to start the script using custom parameters')
            print(' You should enter a command line like this: ')
            print(
                'python pokemonAPI_to_google_drive_spreedsheet.py -n <credentials_file_name>  -p <spreadsheet_name> -f <url_pokemon_source> -k <offset_value>')
            print('Ones example as ')
            print(
                "python pokemonAPI_to_google_drive_spreedsheet.py -n 'PokemonAPIPython-83ebb5088725.json'  -p 'A new PokemonAPI spreadsheet' -f 'https://pokeapi.co/api/v2/pokemon/' -k 0")
            sys.exit()

        elif opt in ("-n", "--credentials_file_name"):
            credentials_file_name = arg

        elif opt in ("-p", "--spreadsheet_name"):
            spreadsheet_name = arg

        elif opt in ("-f", "--url_pokemon_source"):
            url_pokemon_source = arg

        elif opt in ("-k", "--offset_value"):
            offset_value = arg
            # print ('Arguments ', len(arguments))
    if len(arguments) == 0:
        if credentials_file_name == None:
            credentials_file_name = 'PokemonAPIPython-83ebb5088725.json'
        if spreadsheet_name == None:
            spreadsheet_name = 'A new PokemonAPI spreadsheet'
        if url_pokemon_source == None:
            url_pokemon_source = 'https://pokeapi.co/api/v2/pokemon/'
        if offset_value == None:
            offset_value = 0

        print('pokemonAPI_to_google_drive_spreedsheet program has been started ')
        print('Credential file name ', credentials_file_name)
        print('Spreadsheet name ', spreadsheet_name)
        print('Pokemon source url ', url_pokemon_source)
        print('Offset value : %s' % offset_value)
        runProgram(credentials_file_name, spreadsheet_name, url_pokemon_source, offset_value)


# Begin Script
if __name__ == '__main__':
    main(sys.argv[1:])

