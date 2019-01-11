# Questioner-API
API endpoints for Questioner- an application to crowd-source questions for a meetup.

[![Build Status](https://travis-ci.org/yunismohamed/Questioner-API.svg?branch=develop)](https://travis-ci.org/yunismohamed/Questioner-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/1d7f1df20f65e92518c3/maintainability)](https://codeclimate.com/github/yunismohamed/Questioner-API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/yunismohamed/Questioner-API/badge.svg)](https://coveralls.io/github/yunismohamed/Questioner-API)


## Here is a list of endpoints
| Method        |       Endpoint                              |         Description                           |
| ------------- |       -------------                         |         -------------                         |
| `GET`         | `/api/v1/meetups/upcoming`                  |   Gets all meetups records                    |
| `GET`         | `/api/v1/meetups/<meetup-id>`               |   Get a specific meetup record                |
| `POST`        | `/api/v1/meetups`                           |   Create a meetup record                      |
| `POST`        | `/api/v1/questions`                         |   Create a question record                    |
| `POST`        | `/api/v1/users/registration`                |   Register a user                             |
| `POST`        | `/api/v1/users/login`                       |   Sign in a User                              |
| `POST`        | `/api/v1/meetups/<meetup-id/rsvps>`         |   User respond to a meetup                    |
| `PATCH`       | `/api/v1/questions/<questions-id>/upvote`   |   vote on a meetup question                   |
| `PATCH`       | `/api/v1/questions/<questions-id/downvote`  |   vote on a meetup question                   |

# Setting up your system

Make sure you already have Python3, Pip and Virtualenv installed in your system.

# How to get started

Start by making a directory where we will work on. Simply Open your terminal and then:

```
mkdir Questioner-API
```

Afterwhich we go into the directory:

```
cd Questioner-API
```
## Create a Python Virtual Environment for our Project

Since we are using Python 3, create a virtual environment by typing:

```
virtualenv -p python3 venv
```

Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:

```
source venv/bin/activate
```

## Clone and Configure a Flask Project

Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:

```
git clone https://github.com/yunismohamed/Questioner-API.git
```

Next, install the requirements by typing:

```
pip install -r requirements.txt
```

## How to run the app

On the terminal type:

```
export  FLASK_ENV=development
```

```
export FLASK_APP=run.py
```

```
flask run
```

## Unit Testing
To test the endpoints ensure that the following tools are available the follow steps below
   ### Tools:
     `Postman`
   ### Steps:
    1. Fire up postman
    2. Send either `GET` or `POST` request to the specific endpoint  

### Commands
  The application was tested using `pytest`. To run the tests on the bash terminal use

     `pytest`

## Heroku Hosting
The Questioner-API is hosted on Heroku
Link : `https://adc-questioner-app.herokuapp.com`