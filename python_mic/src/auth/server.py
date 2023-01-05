import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

#config
server.config['MYSQL_HOST'] = 'localhost'
server.config['MYSQL_USER'] = 'root'
server.config['MYSQL_PASSWORD'] = 'farzan77297797'
server.config['MYSQL_DB'] = 'auth'
server.config['MYSQL_PORT'] = 3306

@SERVER.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    # check db for user

    cur = mysql.connection.cursor()
    res = cur.execute("SELECT email, password FROM users WHERE email=%s", (auth.username,))

    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.username != email or auth.password != password:
            return "invalid credentials", 401
        else:
            return createJWT(auth.username, os.environ.get('JWT_SECRET'), True)

    else:
        return "user does not exit", 401

