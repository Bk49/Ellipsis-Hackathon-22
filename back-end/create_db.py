from models import db, user, finance_request, borrower, loan_request
from app import app

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    GS_admin = user.User(
        username="GS",
        password="admin",
        role="admin",
        loan_repayment_status="None"
    )

    db.session.add(GS_admin)
    db.session.commit()