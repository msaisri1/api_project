from flask_marshmallow import Marshmallow,fields


ma = Marshmallow()


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ("id", "createdAt", "name", "avatar", "payments")


emp_schema = EmployeeSchema()
emps_schema = EmployeeSchema(many=True)



class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)