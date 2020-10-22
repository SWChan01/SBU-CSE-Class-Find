from flask import Flask
from flask_restful import Resource,Api
from flask_cors import CORS
from flask_pymongo import PyMongo,MongoClient

from bson import Binary, Code
from bson.json_util import dumps



cluster = MongoClient("mongodb+srv://143512:143512@cluster0.tfuyf.mongodb.net/SBUClassFind?retryWrites=true&w=majority")
db = cluster['SBUClassFind']
schedules = db['schedules']

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/SBUClassFind"
mongo = PyMongo(app)

CORS(app, support_credentials=True)


class HelloWorld(Resource):
    def get(self):
        string = schedules.find_one({"test":"testing"})
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(string)
        return {"hello":dumps(string)}

api.add_resource(HelloWorld,'/hello')





if __name__ == '__main__':
    app.run(debug=True)