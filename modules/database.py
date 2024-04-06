userDatabase = [{
        "matricule": "admin",
        "name": "test",
        "department": "test",
        "status": "admin",
        "password": "test",
        "gender": "M"
    }, {
        "matricule": "test",
        "name": "test",
        "department": "test",
        "departmentCode": "CE",
        "status": "stud",
        "results-firstSemister": [],
        "results-secondSemister": [],
        "password": "test",
        "gender": "F"
    },{
        "matricule": "22-ET-stud-001",
        "name": "Okoro Junior",
        "department": "Software Engineering",
        "departmentCode": "SWE",
        "gender": "M",
        "status": "student",
        "password": "mike",
        "results-firstSemister": [ {
        "subjectName": "Analysis",
        "caMark": 30,
        "examMark": 70,
        "totalMark": 100,
        "grade" : "A"
    },  {
        "subjectName": "Maths",
        "caMark": 20,
        "examMark": 50,
        "totalMark": 70,
        "grade" : "B+"
    }],
        "results-secondSemister": [ {
        "subjectName": "French",
        "caMark": 22,
        "examMark": 33,
        "totalMark": 55,
        "grade" : "C"
    },
    {
        "subjectName": "Law",
        "caMark": 25,
        "examMark": 35,
        "totalMark": 60,
        "grade" : "B"
    }]
    }]

systemDb = {
    "admins": [],
    "departments":[
        {
        "departmentName" : "Sofware engineering",
         "students": [],
         "courses": {
            "firstSemeister": ["analysis", "statistics", "english", "french", "introduction to law"],
            "secondSemister": ["analysis II", "statistics II", "english II", "french II", "labour law"]
         }
        },
        {
        "departmentName" : "Civil engineering",
         "students": [],
         "courses": {
            "firstSemeister": ["engineering mathematics", "Building and Construction", "english", "french", "introduction to law"],
            "secondSemister": ["engineering mathematics II", "material production", "english II", "french II", "labour law"]
         }
         },
        {
        "departmentName" : "Bio-Chemical engineering",
         "students": [],
         "courses": {
            "firstSemeister": ["engineering mathematics", "chemical theory", "english", "french", "introduction to law"],
            "secondSemister": ["engineering mathematics II", "Organic Chemistry", "english II", "french II", "labour law"]
         }
        },
    ]
}
