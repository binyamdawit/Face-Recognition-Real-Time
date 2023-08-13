import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-89d20-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "312654":
        {
            "name": "Elizabeth White",
            "major": "Communications",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-08-08 00:54:34"
        },
    "852741":
        {
            "name": "Benjamin Mensah",
            "major": "Accounting",
            "starting_year": 2018,
            "total_attendance": 5,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2023-08-08 00:54:34"
        },
    "963852":
        {
            "name": "Mark Zuckerberg",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-08-08 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)