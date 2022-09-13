import pymongo
from flask import Flask, render_template
import os 
from flask import Flask,  Response
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo

try:
    MONGODB_URI = 'mongodb+srv://soyansoon:dUuiEuBaARLwocjH@mycluster.yix1qqc.mongodb.net/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(MONGODB_URI)
    
    # accessing the database
    db = client['thirty_days_of_python']
    # accessing database collection
    
    student = db.students.find_one()
    
    # print the collesion
    print(student)

    app = Flask(__name__)
    
    @app.route('/api/v1.0/students', methods = ['GET'])

    def students ():
        return Response(json.dumps(student), mimetype='application/json')


    @app.route('/api/v1.0/students/<id>', methods = ['GET'])
    def single_student (id):
        student = db.students.find({'_id':ObjectId(id)})
        return Response(dumps(student), mimetype='application/json')
        
    if __name__ == '__main__':
        port = int(os.environ.get("PORT", 82))
        app.run(debug=True, host='0.0.0.0', port=port)

except:
    print("permision denied")