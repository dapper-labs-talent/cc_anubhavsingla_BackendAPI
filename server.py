from flask import Flask, request
import json
import jwt
from database import Database

app = Flask(__name__)
SECRET = "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"
DB = Database()

@app.route("/signup", methods=["POST"])
def signup():
    user = json.loads(request.data)
    payload = {"email": user["email"], "password": user["password"]}
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    DB.add_user(user)
    return {"token": token}

@app.route("/login", methods=["POST"])
def login():
    user_cred = json.loads(request.data)
    user_cred = DB.verify_user(user_cred)
    token = jwt.encode(user_cred, SECRET, algorithm="HS256")
    return {"token": token}

@app.route("/users", methods=["GET", "PUT"])
def users():
    token = request.headers["x-authentication-token"]
    user_cred = jwt.decode(token, SECRET, algorithms=["HS256"])
    user_cred = DB.verify_user(user_cred)
    if request.method == "PUT":
        new_user = json.loads(request.data)
        DB.update_user(user_cred, new_user)
        return ""
    else:
        all_users = DB.get_all_users()
        return json.dumps(all_users)
