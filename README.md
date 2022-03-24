# flask_server_boilerplate

This is boiler plate with basic structure setup for REST api using flask framework and docker container

Files List

wsgi.py - This file is for running flask app on server

app.ini - This file is for threds management for multiple server

Dockerfile - for creating docker container and installing all requirements

req.txt - All flask library to run run application will be added here

manage.py - main app life to run flask server

app folder - all application folder and files contain here

- init.py - this file contains all controller deatils
- main folder
  - init.py - this file create flask application
  - config.py - All server and database connection also logger creation
  - controller folder - All API controller and routes
  - mode - Database fields
  - services - all function and programm to run api
  - utils - API velidation and serilisation
