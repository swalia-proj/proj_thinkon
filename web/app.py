from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",           # match docker-compose service name
        user="root",
        password="rootpass",
        database="thinkon"
    )

@app.route("/")
def index():
    return "Web node running"

@app.route("/users")
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([row[0] for row in result])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
