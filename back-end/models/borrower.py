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
        return Response("Success", 201)


    def get(self):
        borrowers = Borrower.query.all()
        return jsonify([borrower.to_json() for borrower in borrowers])

    def put(self):
        borrower_id = request.json["id"]
        loan_repayment_status = request.json["loan_repayment_status"]

        borrower = Borrower.query.filter_by(id=borrower_id).first()
        if not borrower:
            return Response("Invalid borrower ID", 404)


        borrower.loan_repayment_status = loan_repayment_status
        db.session.merge(borrower)
        db.session.commit()
        return Response("Success", 200)

    def delete(self):
        borrower_id = request.json["id"]
        borrower = Borrower.query.filter_by(id=borrower_id).first()
        if not borrower:
            return Response("Invalid borrower ID", 404)

        db.session.delete(borrower)
        db.session.commit()
        return Response("Success", 200)