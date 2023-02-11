from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flaskext.mysql import MySQL

import openai

app = Flask(__name__)
app.config['SECRET_KEY'] = "ThisIsMySecret"


CORS(app, origins=['http://localhost:3000'])

# Configure MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'chatgpt'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

# Configure the OpenAI API key
openai.api_key = "your_openai_api_key"


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')

    try:
        # Connect to the database
        conn = mysql.connect()
        cursor = conn.cursor()

        # Save the user's sign up information to the database
        sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, password, email))
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

    # Save the user's information in the session
    session['username'] = username
    session['email'] = email

    return jsonify({"success": True, "error": None})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # check if user is in session
        username = request.args.get("username")
        if 'username' in session and username in session['username']:
            return jsonify({"username": username, "error": None})
        return jsonify({"username": None, "error": None})

    username = request.json.get('username')
    password = request.json.get('password')

    # TODO: Add code here to check the username and password against the database
    # Return error if it doesn't match

    # TODO: If the username and password are correct, set the username in the session

    return


# TODO: Create logout api
# you should retrieve the username from the request, pop it from the session if it's in the session
# then return a result
@app.route("/logout", methods=["POST"])
def logout():
    return

@app.route("/chat", methods=["POST"])
def chat():
    # Get the inputs from the request
    user_id = request.json["user_id"]
    question = request.json["question"]

    # Use OpenAI's language generation API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='You: ' + question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Remove the "You: " prefix from the response
    response = response.replace("You: ", "")

    # TODO save the chat history into database

    # Return the response as JSON
    return jsonify({"response": response})


# TODO: Create chat_history API that returns chat history for the specified user
@app.route("/chat_history", methods=["POST"])
def chat_history():
    return



if __name__ == "__main__":
    app.run(debug=True, host='localhost')
