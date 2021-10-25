# Pedestrian Safety Reporting

## Table of Contents

1. [General Info](#general-info)
2. [Licensing](#licensing)
3. [Contributing](#contributing)
4. [Requirements](#requirements)
5. [Installation](#installation)

## General Info

Pedestrian Safety Reporting is a Flask web application. This application allows citizens to report issues that present
hazards or concerns to pedestrians. Early reporting will allow resolving hazards and preventing accidents.

## Licensing

This project is licensed under the GPL-3.0 License. See 'LICENSE' for the complete license.  
This program includes code from the Flask_Blog, used under the following license: Copyright (c) <2018> <CoreyMSchafer>

## Contributing

We welcome contributions from anyone. Please refer to the contribution guidelines and the OSS component use policy on
CONTRIBUTING.md file for details.

## Requirements

Python 3.8+ CLI or your favorite IDE to use with Flask.

## Installation

1- Install Flask  
`$ pip3 install flask`

2- Clone the project repository to your local machine  
`$ git clone https://github.com/AnjaSlama/Pedestrian-Safety-Reporting.git`

3- Move into the project directory
`$ cd Pedestrian-Safety-Reporting`

4- Create and activate a virtual environment

- MAC  
  `$ Python3 -m venv venv`   
  `$ source venv/bin/activate`
- WINDOWS  
  `$ Python3 -m venv venv`  
  `$ venv\Scripts\activate`

5- Install required Python packages  
`$ pip install -r requirements.txt`

6- Run the application

- MAC
  `$ FLASK_CONFIG=development python app.py runserver`
- WINDOWS
  `$ set FLASK_CONFIG=development  
  $ python app.py runserver`







