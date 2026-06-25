from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",          # must match service name in docker-compose.yml
        database="flaskdb", # must match POSTGRES_DB
        user="flaskuser",   # must match POSTGRES_USER
        password="flaskpass" # must match POSTGRES_PASSWORD
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT NOW();')
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"Hello from Docker 🚀 — DB time is {result[0]}"

if __name__ == "__main__":
    # This keeps Flask running inside the container
    app.run(host="0.0.0.0", port=5000)
