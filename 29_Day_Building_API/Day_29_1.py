from flask import Flask,  Response
import json
import pymongo
import os

try:

    app = Flask(__name__)

    MONGODB_URI='mongodb+srv://soyansoon:dUuiEuBaARLwocjH@mycluster.yix1qqc.mongodb.net/?retryWrites=true&w=majority'

    client = pymongo.MongoClient(MONGODB_URI)

    # accessing the database
    db = client['thirty_days_of_python']
    
    student = db.students.find_one()
    
    # print the collesion
    print(student)

    
    @app.route('/api/v1.0/students', methods = ['GET'])

    def students ():
        return Response(json.dumps(student), mimetype='application/json')


    # if __name__ == '__main__':
    #     port = int(os.environ.get("PORT", 82))
    #     app.run(debug=True, host='0.0.0.0', port=port)

except:
    print('permission denied')



