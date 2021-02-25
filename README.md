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



# Test the Script using Docker

1. Building the Docker image: Put **docker build -t test-pokemon .** on your console ( include the last point as correct syntaxis.
2. Checking the Docket image generated. Put **docker images** command on your console.
3. Running the Docker image. Put **docker run test-pokemon** command on your console.

## Results:

You will see terminal out`put like this

![alt text](https://github.com/EnriqueAldana/pokeApiGoogleDrive/blob/master/pokemon_console.jpg?raw=true)

You can compare the spreadsheet data on Google Drive at [Here](
https://docs.google.com/spreadsheets/d/1nAjmuSG-h3ALKHr1d94u5eXhJmeLCVUXCADONIHUSq4/edit?usp=sharing)


![alt text](https://github.com/EnriqueAldana/pokeApiGoogleDrive/blob/master/pokemon_spreadsheet_updated.jpg?raw=true)
