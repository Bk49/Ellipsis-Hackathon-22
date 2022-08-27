from models import db, user, finance_request, borrower, loan_request
from app import app
from flask_bcrypt import Bcrypt


db.init_app(app)
bcrypt = Bcrypt(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    GS_admin = user.User(
        username="GS",
        password=bcrypt.generate_password_hash("admin"),
        role="admin",
        loan_repayment_status="None"
    )

    EZFinance = user.User(
        username="EZFinance",
        password=bcrypt.generate_password_hash("ez123"),
        role="client",
        loan_repayment_status="None"
    )

    db.session.add(GS_admin)
    db.session.add(EZFinance)

    ez_finance_finance_request_1 = finance_request.FinanceRequest(
        financing_company_id=2,
        request_amount=100,
        interest_rate=1,
        paid_amount=0,
        status="No loan"
    )

    ez_finance_finance_request_2 = finance_request.FinanceRequest(
        financing_company_id=2,
        request_amount=200,
        interest_rate=2,
        paid_amount=0,
        status="No loan"
    )

    ez_finance_finance_request_3 = finance_request.FinanceRequest(
        financing_company_id=2,
        request_amount=300,
        interest_rate=2.1,
        paid_amount=0,
        status="No loan"
    )

    db.session.add(ez_finance_finance_request_1)
    db.session.add(ez_finance_finance_request_2)
    db.session.add(ez_finance_finance_request_3)

    db.session.commit()

