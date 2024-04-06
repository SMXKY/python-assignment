from modules import database
from modules import sorting

#user database
userDatabase = database.userDatabase

#Department database
systemDb = database.systemDb


#decalring a subject template
def subjectTemplate(subjectName, caMark, examMark):
    subject = {
        "subjectName": subjectName,
        "caMark": caMark,
        "examMark": examMark,
        "totalMark": caMark + examMark,
        "grade" : ""
    }
    
    if subject["totalMark"] >= 80 :
        subject["grade"] = "A"
    elif subject["totalMark"] >= 70 :
        subject["grade"] = "B+"
    elif subject["totalMark"] >= 60 :
        subject["grade"] = "B"
    elif subject["totalMark"] >= 50 :
        subject["grade"] = "C"
    else:
        subject["grade"] = "F"
    
    return subject

#mark input mechanism
def addStudentMark(array, student, semister):
    for i in range(0, len(array)):
        subjectName = array[i].upper()
       
        #check legimacy of mark
        caMark = 0
        isValidCaMark = False
        while(isValidCaMark == False):
            collectCaMark = input(f"Enter student CA mark for {subjectName}: ")
            if collectCaMark.isnumeric():
                if(int(collectCaMark) <= 30):
                    caMark = int(collectCaMark)
                    isValidCaMark = True
                else:
                    print("❌❌invalid input, mark must be a number and be less than or equal to 30")
            else:
                print("❌❌invalid input, mark must be a number and be less than or equal to 30")
                
                caMark = 0
        
        examMark = 0 
        isValidExamMark = False
        while(isValidExamMark == False):
            collectExamMark = input(f"Enter student Examination mark for {subjectName}: ")
            if collectExamMark.isnumeric():
                if(int(collectExamMark) <= 70):
                    examMark = int(collectExamMark)
                    isValidExamMark = True
                else:
                    print("❌❌invalid input, mark must be a number and be less than or equal to 70")
            else:
                print("❌❌invalid input, mark must be a number and be less than or equal to 70")               
        
    
        student[semister].append(subjectTemplate(array[i], caMark, examMark))

#the student structure
def studentStructure(name, department, gender, password, matricule, code):
    student = {
        "matricule": matricule,
        "name": name,
        "department": department,
        "departmentCode": code,
        "gender": gender,
        "status": "student",
        "password": password,
        "results-firstSemister": [],
        "results-secondSemister": []
    }
    
    return student 

#generate department code
def generateDepartmentCode(code):
    deptCode = {
        "name": "",
        "code": ""
    }
    
    if(code == "1"):
        deptCode["code"] = "SWE"
        deptCode["name"] = "Software Engineering"
    elif code == "2" :
        deptCode["code"] = "CE"
        deptCode["name"] = "Civil Engineering"
    elif code == "3":
        deptCode["code"] = "BCE"
        deptCode["name"] = "Bio-Chemical Engineering"
    return deptCode

#rendering the user's gender based on choice
def renderUserGender(choice):
    gender = ""
    if choice == "1":
        gender = "M"
    else:
        gender = "F"
    return gender
    
#the student admin
def adminStructure(name, department, gender, password, matricule, code):
    admin = {
        "matricule": matricule,
        "name": name,
        "department": department,
        "departmentCode": code,
        "gender": gender,
        "status": "admin",
        "password": password
    }
    
    return admin

#generating the appended number in the matricule
def genAppend():
    check = len(userDatabase)
    appendValue = ""
    
    if check < 9:
        appendValue = "00"
    elif check < 100:
        appendValue = "0"
    return appendValue

#Generating matricules
def genarateMatricule(status):
    matriculeStart = "24-ET-"
    studentAppend = "stud-"
    adminAppend = "admin-"
    
    matricule = ""
    
    registerationNumber = len(userDatabase) + 1
    
    if status == "student" :
        matricule = f"{matriculeStart}{studentAppend}{genAppend()}{registerationNumber}"
    else:
        matricule =  f"{matriculeStart}{adminAppend}{genAppend()}{registerationNumber}"

    return matricule

#searching the database
def searchDatabase(category, keyword):
    results = []
    for i in range(0, len(userDatabase)):
        if keyword == userDatabase[i][category]:
            results.append(userDatabase[i])
    return results

def login():
    end = False
    
    userToken = {
            "status": "",
            "isLegit": False,
            "matricule": ""
            }
    
    while(end == False):
        userMatricule = input("Please enter your matricule: ")
        
        userProfile = searchDatabase("matricule", userMatricule)

        if len(userProfile) > 0:
            userpassword = input("Enter you password: ")
            if(userpassword == userProfile[0]["password"]):
                userToken["isLegit"] = True
                userToken["matricule"] = userMatricule
                userToken["status"] = userProfile[0]["status"]
                end = True
                print("Successfully logged in..✅✅")
            else:
                print("Failed authentication, verify your password or matricule...❌❌🛑🛑")
        else:
            print("This matricule does not exist in the database, please try again")
    return userToken

def register():
    print("Welcome to the registration form, please fill in the form follwing the prompts...")
    
    statusIsvalid = False
    
    userStatus = ""
    
    while(statusIsvalid == False):
        status = input("Please are you a student or an admin?: ").lower()
        if status == "admin" or status == "student":
            statusIsvalid = True
            userStatus = status
        else:
            print("Invalid status, please enter status as admin or student...")

    userName = input("Enter your user name: ")
    
    print("----------------------------------------")
    print("|*-----Please Chose a Gender ---------*|")
    print("|*---1. Male -------------------------*|")
    print("|*---2. Female -----------------------*|")
    print("----------------------------------------")
    
    isValidGender = False
    userGenderChoice = ""
    
    while(isValidGender == False):
        choice =  input("Please pick a gender: ")
        if(choice == "1" or choice == "2"):
            userGenderChoice = choice
            isValidGender = True
        else:
            print("❌Invalid choice please chose etheir 1 for male or 2 for female")
            
    userGender = renderUserGender(userGenderChoice)
    userMatricule = genarateMatricule(userStatus)
    userPassword = ""
    
    print("----------------------------------------")
    print("|*-----Please Chose a Department------*|")
    print("|*---1. Software Engineering----------*|")
    print("|*---2. Civil Engineering-------------*|")
    print("|*---3. Bio-Chemical Engineering------*|")
    print("----------------------------------------")
    
    isLegitDepartment = False
    userDepartmentChoice = ''
    
    while(isLegitDepartment == False):
        userDepartment = input("Enter choice here: ")
        
        if(userDepartment == "1" or userDepartment == "2" or userDepartment == "3"):
            userDepartmentChoice = userDepartment
            isLegitDepartment = True
        else:
            print("Invalid choice of department, type either 1, 2 or 3 to chose a department")
            
    userDept = generateDepartmentCode(userDepartmentChoice)
    userDepartment = userDept["name"]
    userDeptCode = userDept["code"]
    
    passwordIsIdentical = False 
    
    while(passwordIsIdentical == False):
        firstPassword = input("Chose a password: ")
        checkPassowd = input("Repeat password: ")

        if(firstPassword == checkPassowd):
            userPassword = firstPassword
            passwordIsIdentical = True
        else:
            print("The two password you entered do match❌❌❌, please try again...")
    
    userToken = {}
    if(userStatus == "admin"):
        userToken = adminStructure(userName, userDepartment, userGender, userPassword, userMatricule, userDeptCode)
    else: 
        userToken = studentStructure(userName, userDepartment, userGender, userPassword, userMatricule, userDeptCode)
    
    userDatabase.append(userToken)
    print("Account successfully created..✅✅")
    return userToken

#Inputing marks for a single student
def inputMarksForOneStudent(matricule, name):
    print("You have initiated the mark inputing system for the following student.....")
    print(f"Name: {name}")
    print(f"Matricule: {matricule}")
    
    studentExist = False
    student = {}
    while studentExist == False:
        findStudent = searchDatabase("matricule", matricule)
        
        if len(findStudent) > 0 :
            student = findStudent[0]
            studentExist = True
        else:
            print("Student matricule not found in the database, please try agian.......")
    
    deparmtment = 0 
    
    if student["departmentCode"] == "CE":
        deparmtment = 1
    else:
        deparmtment = 2

    print("----------------------------------------")
    print("|*-----Please Chose a semister -------*|")
    print("|*---1. First Semister----------------*|")
    print("|*---2. Second Semister---------------*|")
    print("----------------------------------------")
    
    semister  = ""
    dbSemister = ""
    isValidSemister = False
    
    while isValidSemister == False:
        semisterChoice = input("Select a semister: ")

        if(semisterChoice == "1" or semisterChoice == "2"):
            if(semisterChoice == "1"):
                semister = "firstSemeister"
                dbSemister = "results-firstSemister"
            else: 
                semister = "secondSemister"
                dbSemister = "results-secondSemister"
                
            isValidSemister = True
            
        else: 
            print("❌invalid semister choice, chose 1, for the first semister, and 2, for the second semister")
    
    addStudentMark(systemDb["departments"][deparmtment]["courses"][semister], student, dbSemister) 
    
    for i in range(0, len(userDatabase)):
        if(userDatabase[i]["matricule"] == student["matricule"]):
            userDatabase[i]= student          
    
#Enter marks for all the students in a given department
def inputDepartmentMarks():
    sorting.sortDatabase()
    department = 0
    
    def deptMenu():
        print("----------------------------------------")
        print("|*-----Please Chose a department------*|")
        print("|*---1. Software Engineering----------*|")
        print("|*---2. Civil Engineering-------------*|")
        print("|*---3. Bio-Chemical Engineering------*|")
        print("----------------------------------------")
    
    deptMenu()
    
    isValidDepartment = False
    
    while isValidDepartment == False:
        choseDepartment = input("select department: ")
        if choseDepartment == "1" or choseDepartment == "2" or choseDepartment == "3":
            department = int(choseDepartment) -1
            isValidDepartment = True
        else:
            print("❌❌Invalid department choice, please try agian")
            deptMenu()
    
    if len(systemDb["departments"][department]["students"]) > 0:
        for student in systemDb["departments"][department]["students"]:
            inputMarksForOneStudent(student["matricule"], student["name"])
    else:
        print("😥😣😥Sorry, this department has yet to have any registered students")


#User Driven menu

#selection module

def select(title, array):
    def menu():
        print("------------------------------------------------------------------------")
        
        titleCheck = f"|*--------== {title.upper()} ==---------------------------------------------------------*|"
        
        if int(len(titleCheck)) > 72:
                characters = int(len(titleCheck)) - 72
                titleCheck = titleCheck[:-characters - 2] + "*|"
                print(titleCheck)
                
        for i in range(0, len(array)):
            text = f"|*--------{i + 1}. {array[i]}--------------------------------------------------------------*|"
            
            if int(len(text)) > 72:
                characters = int(len(text)) - 72
                text = text[:-characters - 2] + "*|"
                print(text)
        
        print("------------------------------------------------------------------------")
        
    menu()
    
    myLoop = ""
    
    for i in range(0, len(array)):
        myLoop += f" or option == '{i + 1}'"
    
    userOption = 0
    isValidOption = False
    
    
    while isValidOption == False:
        option = input("select an option: ")
        if option.isnumeric():
            if int(option) <= len(array) and int(option) > 0:
                isValidOption = True
                userOption = int(option)
            else:
                print("❌❌Invalid choice, please try agian")
                menu()
        else:
            print("❌❌Invalid choice, please try agian")
            menu()
            
    return userOption

#Displaying search results
def displaySearch(array):
    if len(array) > 0:
        print(f"----------Results: {len(array)}-----------")
        for user in array:
            print(f"""
---------------------------------------------------
Name: {user["name"]} 
Matricule: {user["matricule"]} 
Gender: {user["gender"]} 
Department: {user["department"]} 
Status: {user["status"]}
---------------------------------------------------
                  """)
    else:
        print("Sorry user cannot be found in our database")
        
#Delete a student
def deleteStudent(matricule):
    for i in range(0, len(userDatabase)):
        if(userDatabase[i]["matricule"] == matricule):
            userDatabase.pop(i) 
    print("User has been successfully deleted....✅❎")
    
#Display results
def displayResults(array):
    if len(array) > 0:
        for subject in array:
            print(
    f"""
------------------------------------------------------
Course: {subject["subjectName"]}
CA Mark: {subject["caMark"]}
Exam Mark: {subject["examMark"]} 
Total Mark: {subject["totalMark"]} 
Grade: {subject["grade"]}
------------------------------------------------------
    """
                  )
    else:
        print("Results for this session are not available at the momment❎❎")
   
#Running the application
def app():
    initialMenuOption = select("Menu", ["Register", "Login", "end"])
    loggedInUser = {}
    
    if initialMenuOption == 1:
       loggedInUser = searchDatabase("matricule", register()["matricule"])[0]
    elif initialMenuOption == 2:
        loggedInUser = searchDatabase("matricule", login()["matricule"])[0]
    else:
        return
        
    if loggedInUser["status"] == "admin":
        isLogedOut = False
        while isLogedOut == False:
            adminMenu = select("Admin Menu", ["Input Marks", "Search Category", "Delete student", "logout"])   
            
            if adminMenu == 1:
                inputDepartmentMarks()
            elif adminMenu == 2:
                category = select("Categories", ["Search by matricule", "Search by gender", "Search by department", "Search by status", "Search by name", "All"]) 

                if category == 1:
                    key = input("Enter the user's matricule: ")
                    displaySearch(searchDatabase("matricule", key))
                elif category == 2:
                    key = ""
                    genkey = select("Gender", ["Male", "Female"])
                    
                    if(genkey == 1):
                        key = "M"
                    else:
                        key = "F"
                        
                    displaySearch(searchDatabase("gender", key))
                elif category == 3:
                    key = input("Enter the user's department: ")
                    displaySearch(searchDatabase("department", key))
                elif category == 4:
                    key = ""
                    genkey = select("Status", ["Student", "Admin"])
                    
                    if(genkey == 1):
                        key = "student"
                    else:
                        key = "admin"
                        
                    displaySearch(searchDatabase("status", key))
                elif category == 5:
                    key = input("Enter the user's name: ")
                    displaySearch(searchDatabase("name", key))
                else:
                    displaySearch(userDatabase)
                    
            elif adminMenu == 3:
                matricule = input("Enter studen matricule number: ")
                deleteStudent(matricule)
            else:
                print("🖐🏿🖐🏿🙌Good Bye... Thank you for using the sytem, see you next time") 
                app()
                isLogedOut = True 
    else:
        isLogedOut = False
        while isLogedOut == False:
            studentMenu = select("Student Menu", ["View Details", "View Results", "logout"])
            
            if studentMenu == 1:
                user = loggedInUser
                print(f"""
---------------------------------------------------
Name: {user["name"]} 
Matricule: {user["matricule"]} 
Gender: {user["gender"]} 
Department: {user["department"]} 
Status: {user["status"]}
---------------------------------------------------
                  """)
            elif studentMenu == 2:
                print("Chose a session")
                semister = select("Session", ["First semister", "Second semister"]) 
                if semister == 1:
                    displayResults(loggedInUser["results-firstSemister"])
                else:
                    displayResults(loggedInUser["results-secondSemister"])
            else:
                print("🖐🏿🖐🏿🙌Good Bye... Thank you for using the sytem, see you next time") 
                app()
                isLogedOut = True 

app()