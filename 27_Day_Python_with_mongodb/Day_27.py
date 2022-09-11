# Inserting many documents to collection

import pymongo

from flask import Flask, render_template
import os
MONGODB_URI = 'mongodb+srv://soyansoon:dUuiEuBaARLwocjH@mycluster.yix1qqc.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

db = client.thirty_days_of_python

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
]

for student in students:
    db.students.insert_one(student)

print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 82))
    app.run(debug=True, host='0.0.0.0', port=port)
