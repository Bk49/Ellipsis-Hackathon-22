from flask_restful import Resource
from flask import request, Response, jsonify
from . import db, borrower


class LoanRequest(db.Model):

    __tablename__ = "loan_request"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    borrower_id = db.Column(db.Integer, db.ForeignKey("borrower.id"))
    request_amount = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    paid_amount = db.Column(db.Float)
    house_valuation = db.Column(db.Float)
    status = db.Column(db.String(10))

    def to_json(self):
        return {
            "id": self.id,
            "financing_company_id": self.financing_company_id,
            "request_amount" : self.request_amount,
            "interest_rate" : self.interest_rate,
            "paid_amount" : self.paid_amount,
            "house_valuation" : self.house_valuation,
            "status": self.status
        }


class LoanRequestResource(Resource):
    def post(self, borrower_id):
        request_amount = request.json["request_amount"]
        interest_rate = request.json["interest_rate"]
        house_valuation = request.json["house_valuation"]

        current_borrower = borrower.Borrower.query.filter_by(id=borrower_id).first()

        if not current_borrower:
            return Response("Invalid borrower ID", 404)

        new_loan_request = LoanRequest(borrower_id=borrower_id,
                                       request_amount=request_amount,
                                       interest_rate=interest_rate,
                                       house_valuation=house_valuation,
                                       paid_amount=0,
                                       status="Pending")

        db.session.add(new_loan_request)
        db.session.commit()

        return Response("Success", 200)

    def get(self, borrower_id):
        current_borrower = borrower.Borrower.query.filter_by(id=borrower_id)
        if not current_borrower:
            return Response("Invalid borrower ID", 404)

        loan_requests = LoanRequest.query.filter_by(borrower_id=borrower_id).all()
        return [loan_request.to_json() for loan_request in loan_requests]

    def put(self, borrower_id):
        loan_request_id = request.json["loan_request_id"]
        status = request.json["status"]
        paid_amount = request.json["paid_amount"]

        current_borrower = user.User.query.filter_by(id=borrower_id).first()
        if not current_borrower:
            return Response("Invalid borrower ID", 404)

        loan_request = LoanRequest.query.filter_by(id=loan_request_id).first()
        if not loan_request:
            return Response("Invalid loan request ID", 404)

        loan_request.status = status
        loan_request.paid_amount = paid_amount
        db.session.merge(loan_request)
        db.session.commit()
        return Response("Success", 200)

    def delete(self, borrower_id):
        loan_request_id = request.json["loan_request_id"]

        current_borrower = borrower.Borrower.query.filter_by(id=borrower_id).first()
        if not borrower:
            return Response("Invalid borrower ID", 404)

        loan_request = LoanRequest.query.filter_by(id=loan_request_id).first()
        if not loan_request:
            return Response("Invalid loan request ID", 404)

        db.session.delete(loan_request)
        db.session.commit()
        return Response("Success", 200)


class LoanRequestIDListResource(Resource):
    def get(self):
        loan_request_id_list = request.json["id_list"]

        loan_requests = []
        for id in loan_request_id_list:
            loan_requests.append(LoanRequest.query.filter_by(id=id).first())

        return [loan_request.to_json() for loan_request in loan_requests]

    def delete(self):
        loan_request_id_list = request.json["id_list"]

        loan_requests = []
        for id in loan_request_id_list:
            loan_request = LoanRequest.query.filter_by(id=id).first()
            db.session.delete(loan_request)
            db.session.commit()
        return Response("Success", 200)


class LoanRequestListResource(Resource):
    def get(self):
        loan_requests = LoanRequest.query.all()
        return [loan_request.to_json() for loan_request in loan_requests]
