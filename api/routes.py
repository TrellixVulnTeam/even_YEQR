from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
psauxes = {}


class SerVer(Resource):
    def get(self, psaux_id):
        return {psaux_id: psauxes[psaux_id]}

    def put(self, psaux_id):
        psauxes[psaux_id] = request.form['data']
        return {psaux_id: psauxes[psaux_id]}


api.add_resource(SerVer, '/<procesi:psaux_id>')

if __name__ == '__main__':
    app.run(debug=True)
