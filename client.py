from requests import request

headers = {
    "Content-Type": "application/json"
}
signup_data = {
  "email": "test@axiomzen.co",
  "password": "axiomzen",
  "firstName": "Alex",
  "lastName": "Zimmerman"
}
r = request("POST", "http://127.0.0.1:5000/signup", headers=headers, json=signup_data)
token = r.json()["token"]


login_data = {
  "email": "test@axiomzen.co",
  "password": "axiomzen",
}
r = request("POST", "http://127.0.0.1:5000/login", headers=headers, json=login_data)
token = r.json()["token"]


headers = {
    "Content-Type": "application/json",
    "x-authentication-token": token
}

r = request(
    "GET", 
    "http://127.0.0.1:5000/users", 
    headers=headers, 
)
user = r.json()[0]
assert("password" not in user.keys())
for k in user.keys():
    assert(user[k] == signup_data[k])

r = request(
    "PUT",
    "http://127.0.0.1:5000/users",
    headers=headers, 
    json={
        "firstName": "NewFirstName",
        "lastName": "NewLastName"
    }
)

r = request(
    "GET", 
    "http://127.0.0.1:5000/users", 
    headers=headers, 
)
user = r.json()[0]
assert(user["firstName"] == "NewFirstName")
assert(user["lastName"] == "NewLastName")