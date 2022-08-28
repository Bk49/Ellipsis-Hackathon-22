from . import db, finance_request
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    loan_repayment_status = db.Column(db.String(50), nullable=False)
    finance_request = db.relationship("FinanceRequest", backref='user', lazy=True, cascade="all,delete")


    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }


class UserResource(Resource):
    def post(self):
        new_user = User(username=request.json["username"],
                        password=bcrypt.generate_password_hash(request.json["password"]),
                        role=request.json["role"],
                        loan_repayment_status="No outstanding loan")
        db.session.add(new_user)
        db.session.commit()
        return {
                "status_code": 201,
                "message": "Success"
            }


    def get(self):
        users = User.query.all()
        return {
                "status_code": 200,
                "users": [user.to_json() for user in users]
            }

    def put(self):
        financing_company_id = request.json["id"]
        loan_repayment_status = request.json["loan_repayment_status"]

        financing_company = User.query.filter_by(id=financing_company_id).first()
        if not financing_company:
            return {
                "status_code": 404,
                "message": "Invalid company ID"
            }


        financing_company.loan_repayment_status = loan_repayment_status
        db.session.merge(financing_company)
        db.session.commit()
        return {
                "status_code": 200,
                "message": "Success"
            }

    def delete(self):
        financing_company_id = request.json["id"]
        financing_company = User.query.filter_by(id=financing_company_id).first()
        if not financing_company:
            return {
                "status_code": 404,
                "message": "Invalid company ID"
            }

        db.session.delete(financing_company)
        db.session.commit()
        return {
                "status_code": 200,
                "message": "Success"
            }


class UserAuthenticate(Resource):
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        retrieved_user = User.query.filter_by(username=username).first()

        if not retrieved_user:
            return {
                "status_code": 404,
                "message": "Invalid user"
            }

        if bcrypt.check_password_hash(retrieved_user.password, password):
            return {
                "status_code": 200,
                "role": retrieved_user.role,
                "id": retrieved_user.id
            }
        return {
                "status_code": 401,
                "message": "Incorrect password"
            }