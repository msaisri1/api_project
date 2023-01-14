from flask import Flask, request, jsonify
from flask import Flask, request, jsonify,make_response
import requests
from models import Employee,db,User
from schemas import emp_schema, emps_schema,user_schema
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt_identity

from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_bcrypt import Bcrypt
import json



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@\
#     localhost:5432/saisri'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)


# Set up JWT
app.config["JWT_SECRET_KEY"] = "my-secret-key"
jwt = JWTManager(app)





@app.route('/api/v1/save_all_employees', methods=['GET'])
def save_all_employees():
    response = requests.get('https://608c328d9f42b20017c3d8f9.mockapi.io/api/v1/employees', verify = False)
    employees = response.json()
    print(employees)
    employees = [{k: str(v) if k == 'payments' else v for k, v in d.items()} for d in employees]
    result = emps_schema.load(employees, many=True)
    print(result)
    for each in result:
        emp_obj = Employee(**each)
        db.session.add(emp_obj)
    db.session.commit()
    return jsonify({'result':result,'message': 'Employees added to database'})


@app.route('/api/v1/all_employees', methods=['GET'])
#@swag_from('swagger.yml')
#@jwt_required()
def get_all_employees():
    all_employees = Employee.query.all()
    result = emps_schema.dump(all_employees)
    return jsonify(result)



@app.route('/api/v1/all_employee_by_id/<int:id>', methods=['GET'])
#@jwt_required()
def get_employee_by_id(id):
    employee = Employee.query.get(id)
    if employee is None:
        return jsonify({'message': 'Employee not found'}), 404
    result = emp_schema.dump(employee)
    return jsonify(result)


@app.route('/api/v1/delete_employee/<int:id>', methods=['DELETE'])
#@jwt_required()
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee is None:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'})


@app.route('/api/v1/update_employee/<int:id>', methods=['PUT'])
#@jwt_required
def update_employee(id):
    employee = Employee.query.get(id)
    if employee is None:
        return jsonify({'message': 'Employee not found'}), 404
    data = request.get_json()
    result = emp_schema.load(data, partial=True)
    employee.name = result['name']
    employee.createdAt = result['createdAt']
    employee.avatar = result['avatar']
    db.session.commit()
    return emp_schema.dump(result)




# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Hash the password
    hashed_password = generate_password_hash(data['password'])
    # Save the user to the database
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    return jsonify({'message': "successfully registered"}), 201
    db.session.commit()
   


# Route to login a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Get the user from the database
    user = User.query.filter_by(username=data['username']).first()
    # Check if the user exists and the password is correct
    if user and check_password_hash(user.password, data['password']):
        # Create an access token for the user
        access_token = create_access_token(identity=data['username'])
        return jsonify({'message': 'Logged in', 'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


# Protected route
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': 'Access granted', 'current_user': current_user}), 200






if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)