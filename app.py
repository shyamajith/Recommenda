from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# API to store user data
@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        name = data['name']
        age = data['age']
        favorite_author = data['favorite_author']
        favorite_language = data['favorite_language']
        genres = ",".join(data['genres'])  # Convert list to comma-separated string

        # Insert into SQLite database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, age, favorite_author, favorite_language, genres)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, age, favorite_author, favorite_language, genres))
        
        conn.commit()
        conn.close()

        return jsonify({"message": "User data saved successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    user_list = [
        {"id": row[0], 
         "name": row[1], 
         "age": row[2], 
         "favorite_author": row[3], 
         "favorite_language": row[4], 
         "genres": row[5].split(",")
        }
        for row in users
    ]
    
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(debug=True)
