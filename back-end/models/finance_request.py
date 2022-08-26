from flask_restful import Resource
from flask import request, Response, jsonify
from . import db, user


class FinanceRequest(db.Model):

    __tablename__ = "finance_request"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    financing_company_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    request_amount = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    paid_amount = db.Column(db.Float)
    status = db.Column(db.String(10))

    def to_json(self):
        return {
            "id": self.id,
            "financing_company_id": self.financing_company_id,
            "request_amount" : self.request_amount,
            "interest_rate" : self.interest_rate,
            "paid_amount" : self.paid_amount,
            "status": self.status
        }


class FinanceRequestResource(Resource):
    def post(self, financing_company_id):
        request_amount = request.json["request_amount"]
        interest_rate = request.json["interest_rate"]

        financing_company = user.User.query.filter_by(id=financing_company_id).first()

        if not financing_company:
            return Response("Invalid company ID", 404)

        new_finance_request = FinanceRequest(financing_company_id=financing_company_id,
                                            request_amount=request_amount,
                                            interest_rate=interest_rate,
                                            paid_amount=0,
                                            status="Pending")

        db.session.add(new_finance_request)
        db.session.commit()

        return Response("Success", 200)

    def get(self, financing_company_id):
        financing_company = user.User.query.filter_by(id=financing_company_id)
        if not financing_company:
            return Response("Invalid company ID", 404)

        finance_requests = FinanceRequest.query.filter_by(financing_company_id=financing_company_id).all()
        return [finance_request.to_json() for finance_request in finance_requests]

    def put(self, financing_company_id):
        finance_request_id = request.json["finance_request_id"]
        status = request.json["status"]
        paid_amount = request.json["paid_amount"]

        financing_company = user.User.query.filter_by(id=financing_company_id).first()
        if not financing_company:
            return Response("Invalid company ID", 404)

        finance_request = FinanceRequest.query.filter_by(id=finance_request_id).first()
        if not finance_request:
            return Response("Invalid finance request ID", 404)

        finance_request.status = status
        finance_request.paid_amount = paid_amount
        db.session.merge(finance_request)
        db.session.commit()
        return Response("Success", 200)

    def delete(self, financing_company_id):
        finance_request_id = request.json["finance_request_id"]

        financing_company = user.User.query.filter_by(id=financing_company_id).first()
        if not financing_company:
            return Response("Invalid company ID", 404)

        finance_request = FinanceRequest.query.filter_by(id=finance_request_id).first()
        if not finance_request:
            return Response("Invalid finance request ID", 404)

        db.session.delete(finance_request)
        db.session.commit()
        return Response("Success", 200)


class FinanceRequestIDListResource(Resource):
    def get(self):
        finance_request_id_list = request.json["id_list"]

        finance_requests = []
        for id in finance_request_id_list:
            finance_requests.append(FinanceRequest.query.filter_by(id=id).first())

        return [finance_request.to_json() for finance_request in finance_requests]

    def delete(self):
        finance_request_id_list = request.json["id_list"]

        finance_requests = []
        for id in finance_request_id_list:
            finance_request = FinanceRequest.query.filter_by(id=id).first()
            db.session.delete(finance_request)
            db.session.commit()
        return Response("Success", 200)


class FinanceRequestListResource(Resource):
    def get(self):
        finance_requests = FinanceRequest.query.all()
        return [finance_request.to_json() for finance_request in finance_requests]
