import xlsxwriter
from random import randint
import pickle
import mysql.connector

diagnosis_list = ['CHF', 'High Blood Sugar', 'Respiratory Infection', 'UTI', 'Broken Bone', 'Gastrointestinal Virus', 'Hypertensive Crisis']

def main():
    filename = "names.txt"
    f = open(filename, "r")
    listNames = f.read().splitlines()
    patient = []

    workbook = xlsxwriter.Workbook('model_check.xlsx')
    worksheet = workbook.add_worksheet()

    data = ["name", "age", "arriveTime", "chestpain", "shortnessofbreath", "fever", "trauma", "nausea", "abdominalpain",
            "headache", "dizziness", "cough", "weakness", "syncope", "diarrhea", "painfulurination", "mentalstatus",
            "tachypnea", "hypertension", "pain", "frequenturination"]
    row = 0
    col = 0
    for item in data:
        worksheet.write(0, col, item)
        col += 1
    row = 1
    for name in listNames:
        disease = randint(0,6)
        if(disease == 0):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                #nasuea fever abdominal pain
                if(i == 4 or i == 3 or i == 5):
                    patient.append(1)
                else:
                    patient.append(0)
            patient.append("gastrointestinal virus")

        elif (disease == 1):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                # SOB Chestpain tachypnea
                if (i == 0 or i == 1 or i == 14):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            patient.append("hypertensive crisis")

        elif (disease == 2):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                # FrequentUrination PainfulUrination mentalstatus
                if (i == 14 or i == 13 or i == 17):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            patient.append("UTI")


        elif (disease == 3):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                # Trauma Fall
                if (i == 3 or i == 15):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            patient.append("broken bone")

        elif (disease == 4):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
            # Headache Dizziness Weakness Nausea Frequent Urination
                if(i == 6 or i == 7 or i == 4 or i == 9 or i == 17):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            patient.append("High Blood Sugar")

        elif (disease == 5):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
            # Cough Dizziness tachypnea SOB
                if(i == 7 or i == 8 or i == 1 or i == 14):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            patient.append("Respiratory Infection")

        elif (disease == 6):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
            #Cough Chest Pain Hypertension
                if(i == 0 or i == 8 or i == 15):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            patient.append("CHF")

        col = 0
        for item in patient:
            worksheet.write(row, col, item)
            col+=1
        row+=1
        patient.clear()
    workbook.close()

def get_extra(patient):
    extras_added = 0
    while extras_added < 3:
        index = randint(3, 20)
        if(patient[index] == 0):
            patient[index] = 1
            extras_added = extras_added + 1
    
def add_patients_to_database():

    filename = "names.txt"
    f = open(filename, "r")
    listNames = f.read().splitlines()
    patient = []
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="$Ilovechess6969",
                                           database="capstone"
                                           , auth_plugin="mysql_native_password")

    except mysql.connector.Error as err:
        print("Failed Connection")
        print(2 + " " + err)

        print("Connetion successful")

    mycursor = mydb.cursor()

    for i in range(100):
        
        name = listNames[i]

        disease = randint(0,6)
        if(disease == 0):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                #nasuea fever abdominal pain
                if(i == 4 or i == 3 or i == 5):
                    patient.append(1)
                else:
                    patient.append(0)
                #patient.append("gastrointestinal virus")

        elif (disease == 1):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                # SOB Chestpain tachypnea
                if (i == 0 or i == 1 or i == 14):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            #patient.append("hypertensive crisis")

        elif (disease == 2):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                # FrequentUrination PainfulUrination mentalstatus
                if (i == 14 or i == 13 or i == 17):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            #patient.append("UTI")


        elif (disease == 3):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
                # Trauma Fall
                if (i == 3 or i == 15):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            #patient.append("broken bone")

        elif (disease == 4):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
            # Headache Dizziness Weakness Nausea Frequent Urination
                if(i == 6 or i == 7 or i == 4 or i == 9 or i == 17):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            #patient.append("High Blood Sugar")

        elif (disease == 5):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
            # Cough Dizziness tachypnea SOB
                if(i == 7 or i == 8 or i == 1 or i == 14):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            #patient.append("Respiratory Infection")

        elif (disease == 6):
            patient.append(name)
            patient.append(randint(10, 80))
            patient.append("NA")
            for i in range(18):
            # Cough Chest Pain Hypertension
                if(i == 0 or i == 8 or i == 15):
                    patient.append(1)
                else:
                    patient.append(0)
            get_extra(patient)
            #patient.append("CHF")

        model = pickle.load(open('new_RRTS_model.sav', 'rb'))

        new_patient = [patient[3:]]

        result = model.predict(new_patient)

        diagnosis = diagnosis_list[result[0]]

        patient.append(diagnosis)

        if(result[0] == 0):
            floor = 'Cardiovascular'
        elif(result[0] == 1):
            floor = 'Medsurg'
        elif(result[0] == 2):
            floor = 'Pulmonary'
        elif(result[0] == 3):
            floor = 'Medsurg'
        elif(result[0] == 4):
            floor = 'Ortho/Trauma'
        elif(result[0] == 5):
            floor = 'Medsurg'
        elif(result[0] == 6):
            floor = 'Cardiovascular'
        patient.append(floor)
        
        val = []
        try:
            query = 'INSERT INTO patients (name, age, arriveTime, chestpain, shortnessofbreath, fever, trauma, nausea, abdominalpain, headache, dizziness, cough, weakness, syncope, diarrhea, painfulurination, mentalstatus, tachypnea, hypertension, pain, frequenturination, diagnosis, floor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            val = patient
            mycursor.execute(query, val)
            mydb.commit()
        except Exception as err:
            print("Task Failed")
            print(err)
        patient.clear()



if __name__ == '__main__':
    #add_patients_to_database()
    main()






