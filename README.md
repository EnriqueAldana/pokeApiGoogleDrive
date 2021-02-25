# pokeApiGoogleDrive
Pokemon API exercise

Description
The project consists of extracting Pokemons from the API and sending them to a Google Drive Spreadsheet using a Bash / Python / Node script. 

The core functionality for this challenge is:
1. You must store the list of Pokemons on a Google Drive Spreadsheet, each data point must be in its own cell and each pokemon must be in its own row. Pokemons will be provided by the Pokedex API (https://pokeapi.co/).
2. If a Pokemon already exists in your Spreadsheet, it must be updated and there must be a cell where you specify the date and time where the script was run.
3. The script must accept pagination or offset and only retrieve 20 records per page. 
4. It is not necessary to include the images of each pokemon.
5. The script must have an easy way to be executed and to build.

Some optional functionality you can implement:
1. The script could accept an optional parameter to set the pagination options. 
2. The script could accept a --help argument.
3. The script could be executed in Docker.
Some of the things we will review from your challenge:
1. Working Software. We will first review if your application is working as it is specified in this challenge.
2. Code cleanness. We expect you to write clean code that is understandable and maintainable.


Videos

Code
https://youtu.be/5ZkAkNaSmdc

Working
https://youtu.be/-L5D1w4GwhI



Test the Script using Docker

1. Building the Docker image: Put docker build -t test-pokemon . on your console ( include the last point as correct syntaxis.
2. Checking the Docket image generated. Put docker images command on your console.
3. Running the Docker image. Put docker run test-pokemon command on your console.

Results:

You will see terminal out`put like this

enrique@Mac-mini-de-Enrique pokeApiGoogleDrive % docker run test-pokemon
pokemonAPI_to_google_drive_spreedsheet program has been started 
Credential file name  PokemonAPIPython-83ebb5088725.json
Spreadsheet name  A new PokemonAPI spreadsheet
Pokemon source url  https://pokeapi.co/api/v2/pokemon/
Offset value : 0
Date of ejecution of this script :  2021-02-25 21:55:45.442344
Response status:200
The pokemon records according the parameters: {'offset': '0', 'limit': '20'}
[
    {
        "name": "bulbasaur",
        "url": "https://pokeapi.co/api/v2/pokemon/1/"
    },
    {
        "name": "ivysaur",
        "url": "https://pokeapi.co/api/v2/pokemon/2/"
    },
    {
        "name": "venusaur",
        "url": "https://pokeapi.co/api/v2/pokemon/3/"
    },
    {
        "name": "charmander",
        "url": "https://pokeapi.co/api/v2/pokemon/4/"
    },
    {
        "name": "charmeleon",
        "url": "https://pokeapi.co/api/v2/pokemon/5/"
    },
    {
        "name": "charizard",
        "url": "https://pokeapi.co/api/v2/pokemon/6/"
    },
    {
        "name": "squirtle",
        "url": "https://pokeapi.co/api/v2/pokemon/7/"
    },
    {
        "name": "wartortle",
        "url": "https://pokeapi.co/api/v2/pokemon/8/"
    },
    {
        "name": "blastoise",
        "url": "https://pokeapi.co/api/v2/pokemon/9/"
    },
    {
        "name": "caterpie",
        "url": "https://pokeapi.co/api/v2/pokemon/10/"
    },
    {
        "name": "metapod",
        "url": "https://pokeapi.co/api/v2/pokemon/11/"
    },
    {
        "name": "butterfree",
        "url": "https://pokeapi.co/api/v2/pokemon/12/"
    },
    {
        "name": "weedle",
        "url": "https://pokeapi.co/api/v2/pokemon/13/"
    },
    {
        "name": "kakuna",
        "url": "https://pokeapi.co/api/v2/pokemon/14/"
    },
    {
        "name": "beedrill",
        "url": "https://pokeapi.co/api/v2/pokemon/15/"
    },
    {
        "name": "pidgey",
        "url": "https://pokeapi.co/api/v2/pokemon/16/"
    },
    {
        "name": "pidgeotto",
        "url": "https://pokeapi.co/api/v2/pokemon/17/"
    },
    {
        "name": "pidgeot",
        "url": "https://pokeapi.co/api/v2/pokemon/18/"
    },
    {
        "name": "rattata",
        "url": "https://pokeapi.co/api/v2/pokemon/19/"
    },
    {
        "name": "raticate",
        "url": "https://pokeapi.co/api/v2/pokemon/20/"
    }
]
Accessing at google Drive... 
Find a workbook by name called A new PokemonAPI spreadsheet and open the first sheet ...
updating pokemon name as bulbasaur
updating pokemon name as ivysaur
updating pokemon name as venusaur
updating pokemon name as charmander
updating pokemon name as charmeleon
updating pokemon name as charizard
updating pokemon name as squirtle
updating pokemon name as wartortle
updating pokemon name as blastoise
updating pokemon name as caterpie
updating pokemon name as metapod
updating pokemon name as butterfree
updating pokemon name as weedle
updating pokemon name as kakuna
updating pokemon name as beedrill
updating pokemon name as pidgey
updating pokemon name as pidgeotto
updating pokemon name as pidgeot
updating pokemon name as rattata
updating pokemon name as raticate
The worksheet called A new PokemonAPI spreadsheet has been updated


You can compare the spreadsheet data on Google Drive at:
https://docs.google.com/spreadsheets/d/1nAjmuSG-h3ALKHr1d94u5eXhJmeLCVUXCADONIHUSq4/edit?usp=sharing

