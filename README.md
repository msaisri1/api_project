# api_project

# Install the below libraries

python -m venv .venv
.\.venv\Scripts\Activate.ps1 

pip install -r requirements.txt

python -m pip install flask-sqlalchemy

# To build docker image
docker build -t saisri/api-project:0.0.1.RELEASE .

# To run docker image (creating docker container)
docker run -p 5000:5000 {docker_image_ID}


# A Micro service app to fetch crypto currency market updates

Fetching crypto currency market from below site.
https://608c328d9f42b20017c3d8f9.mockapi.io/api/v1/employees

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install request.

```bash
pip install request 
```
## Employee API

This is a simple API for managing employees built using Flask. The API has the following endpoints:

- `GET /api/v1/all_employees`: Retrieves a list of all employees
- `GET /api/v1/all_employee_by_id/<int:id>`: Retrieves a specific employee by ID
- `POST /api/v1/save_all_employees`: Retrieves employees from the mock api and save in the database
- `PUT /api/v1/update_employee/<int:id>`: Update a specific employee by ID
- `DELETE /api/v1/delete_employee/<int:id>`: Delete a specific employee by ID 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requriement.txt .

```bash
aniso8601==8.1.0
flask-marshmallow==0.14.0
Flask-RESTful==0.3.8
marshmallow==3.10.0
marshmallow-sqlalchemy==0.24.1
PyMySQL==0.10.1
pytz==2020.4
six==1.15.0
SQLAlchemy==1.3.22
passlib==1.7.1
Flask-HTTPAuth==3.2.3
flask-bcrypt
flask-jwt-extended
flask-swagger-ui
requests
```

## Testing
file name test_main.py

```python
import pytest

```

## Run

python app.py
python -m pytest
