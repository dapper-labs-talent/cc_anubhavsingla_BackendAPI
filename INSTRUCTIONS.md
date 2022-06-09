# Start postgreSQL
```sh
docker pull postgres
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```

# Install python dependencies
```sh
cd cc_anubhavsingla_BackendAPI
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install sqlalchemy
pip install psycopg2-binary
pip install Flask
pip install requests
pip install PyJWT
```

# Run server
```sh
cd cc_anubhavsingla_BackendAPI
export FLASK_APP=server
flask run
```

# Run test client
```sh
cd cc_anubhavsingla_BackendAPI
python client.py
```

