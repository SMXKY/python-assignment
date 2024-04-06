from . import database

userDatabase = database.userDatabase
systemDb = database.systemDb

def sortDatabase():
    for i in range(0, len(userDatabase)):
        if userDatabase[i]["status"] == "admin":
            systemDb["admins"].append(userDatabase[i])
        else:
            if userDatabase[i]["departmentCode"] == "SWE":
              systemDb["departments"][0]["students"].append(userDatabase[i])  
            elif userDatabase[i]["departmentCode"] == "CE":
                systemDb["departments"][1]["students"].append(userDatabase[i]) 
            else:
                systemDb["departments"][2]["students"].append(userDatabase[i])