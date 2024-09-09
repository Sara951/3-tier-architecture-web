from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def data():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='password',
            database='testdb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name, age FROM test_table")
        rows = cursor.fetchall()
        
        # Structure data as a list of dictionaries
        data = [{"name": row[0], "age": row[1]} for row in rows]
        return jsonify(data)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/submit', methods=['POST'])
def submit():
    conn = None
    cursor = None
    try:
        data = request.json
        name = data.get('name')
        age = data.get('age')
        
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='password',
            database='testdb'
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        return jsonify({"message": "Data inserted successfully!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
