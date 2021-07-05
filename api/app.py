from flask import Flask
from flask_restful import Resource, Api, reqparse
from paramiko import SSHClient, AutoAddPolicy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


# server
cred = []

# credentials
cred_put_args = reqparse.RequestParser()
cred_put_args.add_argument("ip", type=str, help="host IP address")
cred_put_args.add_argument("uname", type=str, help="User name")
cred_put_args.add_argument("pwd", type=str, help="Password")


class SerVer(Resource):
    def put(self):
        args = cred_put_args.parse_args()
        cred = args
        return cred, 201
# paramiko
for it in cred:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(it.ip, it.uname, it.pwd)
    stdin, stdout, stderr = client.exec_command('ps aux')
    psaux = f'STDOUT: {stdout.read().decode("utf8")}'

    def get(self):
        return {'data': psaux}, 203


api.add_resource(SerVer, '/test', '/request', '/psaux')

if __name__ == '__main__':
    app.run(debug=True)
