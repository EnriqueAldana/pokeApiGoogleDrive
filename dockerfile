# first stage
# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .
COPY venv/ .

# command to run on container start
CMD [ "python", "./pokemonAPI_to_google_drive_spreedsheet.py" ]