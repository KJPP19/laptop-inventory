# laptop-inventory
OJT laptop inventory project (Questronix)

## Requirements
1. Python 3.9
2. django
3. djangorestframework
4. drf_yasg (swagger documentation)
5. mysqlclient

## Installation
1. Clone the repository
2. Navigate project directory using '**cd your-repository**'.
3. Create a new virtual environment '**python3 -m venv venv**'.
4. Activate virtual environment '**source venv/bin/activate**'
5. Install dependencies using '**pip install -r requirements.txt**'

## Usage
1. Create superuser using '**python3 manage.py createsuperuser**'
2. Start server using '**python3 manage.py runserver**'
3. Use '**Postman**' or other tools to interact with the endpoints
4. Access swagger documentation after starting the server using '**'your-localhost'/swagger/**'
5. Logfile is generated automatically after starting the server