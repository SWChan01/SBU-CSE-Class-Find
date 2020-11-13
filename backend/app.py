from flask import Flask
from flask_restful import Resource,Api,reqparse
from flask_cors import CORS
from flask_pymongo import PyMongo,MongoClient

from bson import Binary, Code
from bson.json_util import dumps



parser = reqparse.RequestParser()
parser.add_argument("subj",type=str)
parser.add_argument("course",type=str)
parser.add_argument("section",type=str)
parser.add_argument("days",type=str)
parser.add_argument("startTime",type=str)
parser.add_argument("endTime",type=str)
parser.add_argument("duration",type=str)
parser.add_argument("room",type=str)
parser.add_argument("courseName",type=str)


cluster = MongoClient("mongodb+srv://143512:143512@cluster0.tfuyf.mongodb.net/SBUClassFind?retryWrites=true&w=majority")
db = cluster['SBUClassFind']
schedules = db['schedules']

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/SBUClassFind"
mongo = PyMongo(app)

CORS(app, support_credentials=True)


class Schedules(Resource):
    def post(self):
        args = parser.parse_args()
        schedules.insert_one(args)
    

    def get(self):
        res = schedules.find()
        return {'result' : dumps(res)}


api.add_resource(Schedules,'/scheduleOPS')



if __name__ == '__main__':
    app.run(debug=True)