import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-10de2-default-rtdb.firebaseio.com/"
})

ref= db.reference('Students')

data ={
    "852741":{
        "name":"Vijay",
        "major":"VisCom",
        "starting_year":1999,
        "total_attendance":6,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2023-09-11 00:54:34"
    },
    "963852":{
        "name":"Musk",
        "major":"IT",
        "starting_year":2000,
        "total_attendance":12,
        "standing":"B",
        "year":3,
        "last_attendance_time":"2023-09-10 00:44:34"
    }

}

for key,value in data.items():
    ref.child(key).set(value)
