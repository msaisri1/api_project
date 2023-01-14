import json
import pytest
from models import Employee,db
from flask import Flask
from schemas import emp_schema, emps_schema
from main import app,db



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# def test_save_all_employees(client):
#     response = client.get('/api/v1/save_all_employees',content_type='application/json')
#     data = json.loads(response.get_data(as_text=True))
#     assert response.status_code == 200
#     assert data['message'] == 'Employees added to database'
#     assert data['result'] is not None


def test_get_all_employees(client):
    response = client.get('/api/v1/all_employees',content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data is not None
    

def test_get_employee_by_id(client):
    response = client.get('/api/v1/all_employee_by_id/1',content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data is not None


def test_delete_employee(client):
    response = client.delete('/api/v1/delete_employee/60',content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == 'Employee deleted'


def test_update_employee(client):
    employee = {
        "name": "John Smith",
        "createdAt": "2022-10-10T08:40:51.620Z",
        "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/craigdennis/128.jpg",
    }
    response = client.put('/api/v1/update_employee/61',data=json.dumps(employee),content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    #assert 'Employee not found' in data['message']