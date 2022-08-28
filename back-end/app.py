from flask import Flask
from flask_restful import Resource, Api
from models import db, user, finance_request, borrower, loan_request
from flask_cors import CORS
from flask_bcrypt import Bcrypt


app = Flask(__name__)
api = Api(app)
CORS(app)
bcrypt = Bcrypt(app)

DB_USER = "root"
DB_PASSWORD = ""
DB_ENDPOINT = "127.0.0.1"
DB_NAME = "financing"
SECRET_KEY = "secret_key"

URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_ENDPOINT}:3306"

app.config["SQLALCHEMY_DATABASE_URI"] = f"{URI}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = SECRET_KEY

db.init_app(app)

api.add_resource(user.UserResource, "/user")
api.add_resource(user.UserAuthenticate, "/authenticate")

api.add_resource(finance_request.FinanceRequestResource, "/finance_request/<int:financing_company_id>")
api.add_resource(finance_request.FinanceRequestIDListResource, "/finance_request_id_list")
api.add_resource(finance_request.FinanceRequestListResource, "/finance_request_list")

api.add_resource(borrower.BorrowerResource, "/borrower")

api.add_resource(loan_request.LoanRequestResource, "/loan_request/<int:borrower_id>")
api.add_resource(loan_request.LoanRequestIDListResource, "/loan_request_id_list")
api.add_resource(loan_request.LoanRequestListResource, "/loan_request_list")


@app.route("/")
def root_page():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)