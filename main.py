import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QApplication, QMainWindow)
from PyQt6.QtGui import QAction
from PyQt6.uic import loadUi

from functions import registerId, searchPatient, submitPatient, verifyId, refresh

diagnosis_list = ['CHF', 'High Blood Sugar', 'Respiratory Infection', 'UTI', 'Broken Bone', 'Gastrointestinal Virus', 'Hypertensive Crisis']

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("UI/mainMenu.ui", self)
        menu(self)

class LoginScreen(QMainWindow):

    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("UI/loginscreen.ui", self)
        self.submit.clicked.connect(self.wrapper1)
        self.register_2.clicked.connect(self.wrapper2)
    def wrapper1(self):
        if(verifyId(self) == True):
            widget.setCurrentIndex(1)
        else:
            self.displaytext.setText("Invalid Username or Password")
            self.input_username.setText("")
            self.input_password.setText("")
        
    def wrapper2(self):
        registerId(self)
        

class NewPatientScreen(QMainWindow):
    def __init__(self):
        super(NewPatientScreen, self).__init__()
        loadUi("UI/new_patient.ui", self)
        self.submit.clicked.connect(self.wrapper)
        menu(self)
    
    def wrapper(self):
        if(submitPatient(self) == True):
            widget.setCurrentIndex(1)

class Cardiovascular(QMainWindow):
    def __init__(self):
        super(Cardiovascular, self).__init__()
        loadUi("UI/cardiovascular.ui", self)
        self.refresh_button.clicked.connect(self.wrapper)
        menu(self)
    def wrapper(self):
        refresh(self, "Cardiovascular")

class Pulmonary(QMainWindow):
    def __init__(self):
        super(Pulmonary, self).__init__()
        loadUi("UI/pulmonary.ui", self)
        menu(self)
        self.refresh_button.clicked.connect(self.wrapper)
    def wrapper(self):
        refresh(self, "Pulmonary")
    

class Medsurg(QMainWindow):
    def __init__(self):
        super(Medsurg, self).__init__()
        loadUi("UI/medsurg.ui", self)
        menu(self)
        self.refresh_button.clicked.connect(self.wrapper)
    def wrapper(self):
        refresh(self, "Medsurg")
    

class Trauma(QMainWindow):
    def __init__(self):
        super(Trauma, self).__init__()
        loadUi("UI/trauma.ui", self)
        menu(self)
        self.refresh_button.clicked.connect(self.wrapper)
    def wrapper(self):
        refresh(self, "Ortho/Trauma")

class SearchScreen(QMainWindow):
    def __init__(self):
        super(SearchScreen, self).__init__()
        loadUi("UI/search_screen.ui", self)
        self.search.clicked.connect(self.wrapper)
        menu(self)

    def wrapper(self):
        searchPatient(self)

def menu(self):
        self.menuBar = self.menuBar()

        mainMenu = self.menuBar.addMenu("Main Menu")
        go_home = QAction('Home', self)

        mainMenu.addAction(go_home)
        
        patients = self.menuBar.addMenu('Patients')
        new_patient = QAction('New Patient', self)
        patient_lookup = QAction('Patient Lookup', self)

        patients.addAction(new_patient)
        patients.addAction(patient_lookup)
        
        overview = self.menuBar.addMenu('Overview')
        Trauma = QAction('Trauma', self)
        Medsurg = QAction('Medsurg', self)
        Pulmonary = QAction('Pulmonary', self)
        Cardiovascular = QAction('Cardiovascular', self)
        
        overview.addAction(Trauma)
        overview.addAction(Medsurg)
        overview.addAction(Pulmonary)
        overview.addAction(Cardiovascular)


        go_home.triggered.connect(home_screen)
        new_patient.triggered.connect(to_new_patient)
        patient_lookup.triggered.connect(to_search)
        Trauma.triggered.connect(to_trauma)
        Medsurg.triggered.connect(to_medsurg)
        Pulmonary.triggered.connect(to_pulmonary)
        Cardiovascular.triggered.connect(to_cardiovascular)

def to_new_patient():
    widget.setCurrentIndex(2)
def to_search():
    widget.setCurrentIndex(4)
def home_screen():
    widget.setCurrentIndex(1)
def to_pulmonary():
    widget.setCurrentIndex(6)
def to_medsurg():
    widget.setCurrentIndex(7)
def to_trauma():
    widget.setCurrentIndex(5)
def to_cardiovascular():
    widget.setCurrentIndex(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    application = QApplication(sys.argv)
    
    widget = QtWidgets.QStackedWidget()
    mainMenu = MainMenu()
    widget1 = LoginScreen()
    window2 = NewPatientScreen()
    window3 = Cardiovascular()
    window4 = SearchScreen()
    window5 = Trauma()
    window6 = Pulmonary()
    window7 = Medsurg()

    
    widget.addWidget(widget1)
    widget.addWidget(mainMenu)
    widget.addWidget(window2)
    widget.addWidget(window3)
    widget.addWidget(window4)
    widget.addWidget(window5)
    widget.addWidget(window6)
    widget.addWidget(window7)

    widget.setFixedHeight(650)
    widget.setFixedWidth(800)

    widget.show()

    sys.exit(app.exec())