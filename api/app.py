from os import uname
from flask import Response
from flask import Flask, json
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from test import psaux

app = Flask(__name__)
CORS(app)
api = Api(app)

cred = []
# credentials
cred_put_args = reqparse.RequestParser()
cred_put_args.add_argument("ip", type=str, help="host IP address")
cred_put_args.add_argument("uname", type=str, help="User name")
cred_put_args.add_argument("pwd", type=str, help="Password")

#fields
cred_get_args = reqparse.RequestParser()
cred_get_args.add_argument("ip", type=str, help="host IP address")
cred_get_args.add_argument("uname", type=str, help="User name")
cred_get_args.add_argument("pwd", type=str, help="Password")



class SerVer(Resource):
    def put(self):
        args = cred_put_args.parse_args()
        cred = args
        return cred, 201

    
    def get(self):
        return ['data', psaux]


api.add_resource(SerVer,
                 '/request',
                 '/psaux'),
cross_origin(origin='*')

if __name__ == '__main__':
    app.run(debug=True)
