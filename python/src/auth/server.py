import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

#config
server.config['MYSQL_HOST'] = 'localhost'
server.config['MYSQL_USER'] = 'root'
server.config['MYSQL_PASSWORD'] = 'root'
server.config['MYSQL_DB'] = 'auth'
server.config['MYSQL_PORT'] = 3333

@SERVER.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    # check db for user

