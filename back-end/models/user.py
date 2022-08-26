from . import db, finance_request
from flask import Response, request, jsonify
from flask_restful import Resource


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
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
                        password=request.json["password"],
                        role=request.json["role"],
                        loan_repayment_status="No outstanding loan")
        db.session.add(new_user)
        db.session.commit()
        return Response("Success", 201)


    def get(self):
        users = User.query.all()
        return jsonify([user.to_json() for user in users])

    def put(self):
        financing_company_id = request.json["id"]
        loan_repayment_status = request.json["loan_repayment_status"]

        financing_company = User.query.filter_by(id=financing_company_id).first()
        if not financing_company:
            return Response("Invalid company ID", 404)


        financing_company.loan_repayment_status = loan_repayment_status
        db.session.merge(financing_company)
        db.session.commit()
        return Response("Success", 200)

    def delete(self):
        financing_company_id = request.json["id"]
        financing_company = User.query.filter_by(id=financing_company_id).first()
        if not financing_company:
            return Response("Invalid company ID", 404)

        db.session.delete(financing_company)
        db.session.commit()
        return Response("Success", 200)


class UserAuthenticate(Resource):
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        retrieved_user = User.query.filter_by(username=username).first()

        if not retrieved_user:
            return Response("Invalid user", 404)

        if password == retrieved_user.password:
            return Response("Success", 200)
        return Response("Incorrect password", 401)