from math import floor
from PyQt6.QtWidgets import QInputDialog, QMessageBox
import mysql.connector
import pickle

diagnosis_list = ['CHF', 'High Blood Sugar', 'Respiratory Infection', 'UTI', 'Broken Bone', 'Gastrointestinal Virus', 'Hypertensive Crisis']

def registerId(self):

        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969",
                                           database="capstone"
                                           , auth_plugin="mysql_native_password")
        except mysql.connector.Error as err:
            print("Failed Connection")
            print(err)

        print("Connetion successful")

        mycursor = mydb.cursor()

        query = "INSERT INTO login_info (username, password) VALUES (%s,%s)"

        username = self.input_username.text()
        password = self.input_password.text()

        print(username)
        print(password)

        val = (username, password)

        mycursor.execute(query, val)
        mydb.commit()

        self.displaytext.setText("User Registered! Please Login to continue")
        self.input_username.setText("")
        self.input_password.setText("")
    
def verifyId(self):

        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969",
                                           database="capstone"
                                           , auth_plugin="mysql_native_password")
        except mysql.connector.Error as err:
            print("Failed Connection")
            print(1 + " " + err)

        print("Connetion successful")

        mycursor = mydb.cursor()

        username = self.input_username.text()
        password = self.input_password.text()

        query = "SELECT * FROM login_info WHERE username like %s and password like %s"
        value = username, password
        mycursor.execute(query, value)
        result = mycursor.fetchall()
        print(result)
        if result == []:
            return False
        else:
            return True

def submitPatient(self):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969",
                                        database="capstone"
                                        , auth_plugin="mysql_native_password")

    except mysql.connector.Error as err:
        print("Failed Connection")
        print(2 + " " + err)

    print("Connetion successful")

    mycursor = mydb.cursor()

    breath = chestpain = fever = trauma = nausea = abdominalpain = headache = dizziness = cough = weakness = syncope = diarrhea = painfulurination = mentalstatus = tachypnea = hypertension = pain = frequenturination = 0

    name = self.enterName.text()

    age = self.Age.value()

    time = self.timeOfEntry.time().toString()

    if self.breath.isChecked():
        breath = 1
    if self.chestpain.isChecked():
        chestpain = 1
    if self.cough.isChecked():
        cough = 1
    if self.diarrhea.isChecked():
        diarrhea = 1
    if self.fever.isChecked():
        fever = 1
    if self.frequentUrination.isChecked():
        frequenturination = 1
    if self.headache.isChecked():
        headache = 1
    if self.hypertension.isChecked():
        hypertension = 1
    if self.mentalStatus.isChecked():
        mentalstatus = 1
    if self.nausea.isChecked():
        nausea = 1
    if self.pain.isChecked():
        pain = 1
    if self.painUrination.isChecked():
        painfulurination = 1
    if self.syncope.isChecked():
        syncope = 1
    if self.tachypnea.isChecked():
        tachypnea = 1
    if self.trauma.isChecked():
        trauma = 1
    if self.weakness.isChecked():
        weakness = 1
    if self.dizziness.isChecked():
        dizziness = 1

    data = [chestpain, breath, fever, trauma,  nausea,  abdominalpain, headache, dizziness, cough, weakness, syncope, diarrhea, painfulurination, mentalstatus, tachypnea, hypertension, pain, frequenturination]
    
    print(data)
    
    model = pickle.load(open('new_RRTS_model.sav', 'rb'))

    new_patient = [data]

    result = model.predict(new_patient)

    print(result)

    diagnosis = diagnosis_list[result[0]]

    text,ok = QInputDialog.getText(self, 'Diagnosis Overwrite', 'RRTS predicts: ' + diagnosis +  '\n Would you like to overwrite the diagnosis? If not press cancel!')
    print(text)
    if ok:
        diagnosis = text

    if(diagnosis == 'CHF'):
        floor = 'Cardiovascular'
    elif(diagnosis == 'High Blood Sugar'):
        floor = 'Medsurg'
    elif(diagnosis == 'Respiratory Infection'):
        floor = 'Pulmonary'
    elif(diagnosis == 'UTI'):
        floor = 'Medsurg'
    elif(diagnosis == 'Broken Bone'):
        floor = 'Ortho/Trauma'
    elif(diagnosis == 'Gastrointestinal Virus'):
        floor = 'Medsurg'
    elif(diagnosis == 'Hypertensive Crisis'):
        floor = 'Cardiovascular'
    else:
        floor = 'Unknown'

    try:
        query = 'INSERT INTO patients (name, age, arriveTime, chestpain, shortnessofbreath, fever, trauma, nausea, abdominalpain, headache, dizziness, cough, weakness, syncope, diarrhea, painfulurination, mentalstatus, tachypnea, hypertension, pain, frequenturination, diagnosis, floor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        val = name, age, time, chestpain, breath, fever, trauma, nausea, abdominalpain, headache, dizziness, cough, weakness, syncope, diarrhea, painfulurination, mentalstatus, tachypnea, hypertension, pain, frequenturination, diagnosis, floor
        mycursor.execute(query, val)
        mydb.commit()       
        
        return True
    
    except mysql.connector.Error as err:
        print("Task Failed")
        print(err)
        return False
def msgButtonClick(self):
    print("")

def refresh(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969",
                                            database="capstone"
                                            , auth_plugin="mysql_native_password")
            mycursor = mydb.cursor(buffered=True)
            query = "SELECT * FROM patients WHERE floor='Cardiovascular'"
            mycursor.execute(query)
            mydb.commit()
            results = mycursor.fetchall()
            for patient in results:
                self.listWidget.addItem(patient[0])
        except mysql.connector.Error as err:
            print("Task Failed")
            print(err)

def searchPatient(self):
    self.data.clear()
    name = self.enter_name.text()
    print("NAME " + name)
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969",
                                        database="capstone"
                                        , auth_plugin="mysql_native_password")

        query = """SELECT * FROM patients WHERE name=%s"""
        cursor = mydb.cursor()
        command = cursor.execute(query, (name,))

        results = cursor.fetchall()

        print(results)

        toDisplay = []

        for row in results:
            for item in row:
                if type(item) == int:
                    if(item == 0):
                        toDisplay.append("No")
                    elif(item == 1):
                        toDisplay.append("Yes")
                    else:
                        toDisplay.append(str(item))
                else:
                    toDisplay.append(item)
        try:
            for item in toDisplay:
                print(item)
                self.data.addItem(item)
        except Exception as e:
            print(e)
        mydb.commit()

    except mysql.connector.Error as e:
        print("Failed 4")
        print(e)

def refresh(self, floor_name):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969",
                                        database="capstone"
                                        , auth_plugin="mysql_native_password")
        mycursor = mydb.cursor(buffered=True)
        query = ("SELECT * FROM patients WHERE floor= %(floor)s")
        print(query)
        mycursor.execute(query, {'floor' : floor_name})
        mydb.commit()
        results = mycursor.fetchall()
        for patient in results:
            self.listWidget.addItem(patient[0])
    except mysql.connector.Error as err:
        print("Task Failed")
        print(err)