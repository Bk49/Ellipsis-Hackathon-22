from . import db, finance_request
from flask import Response, request, jsonify
from flask_restful import Resource


class Borrower(db.Model):

    __tablename__ = "borrower"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(50), nullable=False)
    nric = db.Column(db.String(50), nullable=False)
    loan_repayment_status = db.Column(db.String(50), nullable=False)
    loan_request = db.relationship("LoanRequest", backref='borrower', lazy=True, cascade="all,delete")


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "nric": self.nric,
            "loan_repayment_status": self.loan_repayment_status
        }


class BorrowerResource(Resource):
    def post(self):
        new_borrower = Borrower(name=request.json["name"],
                        phone_number=request.json["phone_number"],
                        nric=request.json["nric"],
                        loan_repayment_status="No outstanding loan")
        db.session.add(new_borrower)
        db.session.commit()
        return {
                "status_code": 200,
                "message" : "Success"
            }


    def get(self):
        borrowers = Borrower.query.all()
        return {
                "status_code": 200,
                "borrowers": [borrower.to_json() for borrower in borrowers]
            }

    def put(self):
        borrower_id = request.json["id"]
        loan_repayment_status = request.json["loan_repayment_status"]

        current_borrower = Borrower.query.filter_by(id=borrower_id).first()
        if not current_borrower:
            return {
                    "status_code": 404,
                    "message" : "Invalid borrower ID"
                }


        current_borrower.loan_repayment_status = loan_repayment_status
        db.session.merge(current_borrower)
        db.session.commit()
        return {
                    "status_code": 200,
                    "message" : "Success"
                }

    def delete(self):
        borrower_id = request.json["id"]
        current_borrower = Borrower.query.filter_by(id=borrower_id).first()
        if not current_borrower:
            return {
                    "status_code": 404,
                    "message" : "Invalid borrower ID"
                }

        db.session.delete(current_borrower)
        db.session.commit()
        return {
                    "status_code": 200,
                    "message" : "Success"
                }