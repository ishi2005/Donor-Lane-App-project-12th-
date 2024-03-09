import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
from PyQt5.QtGui import QPixmap
import mysql.connector as ms


class Homepage(QDialog):
    def __init__(self):
        super(Homepage,self).__init__()
        loadUi("homepage.ui",self)
        self.signin.clicked.connect(self.gotologinscreen)
        self.signup.clicked.connect(self.gotocreatescreen)
        self.admin.clicked.connect(self.gotoadminscreen)


        image=QPixmap(r'C:\Users\User\Desktop\Python\Donor Lane App(project 12th)\icon.png')
        self.label.setPixmap(image)

    def gotologinscreen(self):                               #sign in function
        loginscreen = LoginScreen()
        widget.addWidget(loginscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreatescreen(self):                              #sign up function
        createscreen = CreateScreen()
        widget.addWidget(createscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoadminscreen(self):                               #admin function
        adminscreen = adminScreen()
        widget.addWidget(adminscreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):               #for login screen
    def gotohomepage(self):
        homescreen = Homepage()
        widget.addWidget(homescreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("Login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signin.clicked.connect(self.loginfunction)
        self.back.clicked.connect(self.gotohomepage)


    def loginfunction(self):              #to extract the details
        user=self.usernamefield.text()
        password=self.passwordfield.text()

        if len(user)==0 or len(password)==0:           #validifying
            self.error.setText("Please fill the required details")
        elif len(user)<=5 or len(password)<=5:
            self.error.setText("Username and password must have 6 characters")


        else:                                  #establishing conection
            con=ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
            cur=con.cursor()
            query='SELECT COUNT(*) FROM LOGIN_CREDENTIALS WHERE username=\''+user+"\'"
            cur.execute(query)
            result_usercount=cur.fetchone()[0]

            if result_usercount>0:
                query='SELECT password FROM LOGIN_CREDENTIALS WHERE username=\''+user+"\'"
                cur.execute(query)
                result_pass=cur.fetchone()[0]
                if result_pass==password:
                    print("Successfully logged in")
                    self.error.setText("")
                else:
                    self.error.setText("Invalid Username or Password ")
            else:
                self.error.setText("Invalid Username or Password ")
            userinfo = userinfoScreen()             #connecting to userinfo screen
            widget.addWidget(userinfo)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class CreateScreen(QDialog):                          #signup screen

    def gotohomepage(self):
        homescreen = Homepage()
        widget.addWidget(homescreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(CreateScreen,self).__init__()
        loadUi("Create.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.back.clicked.connect(self.gotohomepage)


    def signupfunction(self):
        user=self.usernamefield.text()                           #extracting details
        password=self.passwordfield.text()
        confirmpassword=self.confirmpasswordfield.text()


        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:  # validifying
            self.error.setText("Please fill the required details")
        elif password!=confirmpassword:
            self.error.setText("Passwords do not match")
        elif len(user) <= 5 or len(password) <= 5:
            self.error.setText("Username and password must have 6 characters")
        else:
            con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
            if con.is_connected()==False:
                print("connection not established")
            else:
                cur=con.cursor()
                cur.execute('INSERT INTO LOGIN_CREDENTIALS(USERNAME,PASSWORD) VALUES("{}","{}")'.format(user,password))
                con.commit()
                con.close()
            userinfo=userinfoScreen()        #connecting to userinfo screen
            widget.addWidget(userinfo)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class userinfoScreen(QDialog):                     #user information
    def __init__(self):
        super(userinfoScreen, self).__init__()
        loadUi("userinfo.ui", self)
        self.proceed.clicked.connect(self.userinfo)


    def userinfo(self):
        global info1,info2,info3,info4,info5,info6,info7,info8,info9,info10,info11,info12
        user=self.usernamefield.text()                  #extracting the information
        nameD=self.namefield.text()
        nameG=self.Guardianfield.text()
        email=self.emailidfield.text()
        city=self.cityfield.text()
        add=self.addressfield.text()
        ph=self.phnofield.text()
        dob=self.dobfield.text()
        pin=self.pinfield.text()
        gender=self.genderfield.currentText()
        blood=self.bgfield.currentText()
        state=self.statefield.currentText()

        if len(user)==0 or len(nameD)==0 or len(nameG)==0 or len(email)==0 or len(city)==0 or len(add)==0 or len(ph)==0\
                or len(dob)==0 or len(pin)==0 or len(gender)==0 or len(blood)==0 or len(state)==0:
            self.error.setText("Please fill the required details")
        elif len(ph)>10 or len(ph)<10:                                                     # validifying
            self.error.setText("Phone No. should have 10 digits")

        else:
            info1, info2, info3, info4, info5, info6, info7, info8,\
            info9, info10, info11, info12=user,nameD,nameG,email,city,add,ph,gender,blood,dob,state,pin
            questionnaire=questionnaireScreen()         #connecting to questionnaire screen
            widget.addWidget(questionnaire)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class questionnaireScreen(QDialog):               #user questionnaire
    def __init__(self):
        super(questionnaireScreen, self).__init__()
        loadUi("questionnaire.ui", self)
        self.submit.clicked.connect(self.questionnaire)

    def questionnaire(self):
        global info1, info2, info3, info4, info5, info6, info7, info8, info9, info10, info11, info12
        a=self.A.isChecked()                     #extracting questionnaire essentials
        b=self.B.isChecked()
        c=self.C.isChecked()
        d=self.D.isChecked()
        e=self.E.isChecked()
        f=self.F.isChecked()
        g=self.G.isChecked()
        h=self.H.isChecked()
        i=self.I.isChecked()
        j=self.J.isChecked()
        k=self.K.isChecked()
        l=self.L.isChecked()
        m=self.M.isChecked()
        n=self.N.isChecked()
        o=self.O.isChecked()
        p=self.P.isChecked()
        q=self.Q.isChecked()

        if a==True or b==True or c==True or d==True or e==True or f==True or g==True or h==True or i==True or j==True \
                or k==True or l==True or m==True or n==True or o==True or p==True or q==True:
            self.error.setText("SORRY! YOU ARE NOT ELIGIBLE TO DONATE")          #validifying
        else:           #establishing connection btw python nd sql
            con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
            cur = con.cursor()
            query = ('INSERT INTO DONOR_INFO VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",{})'.format
                     (info1, info2, info3, info4, info5, info6, info7, info8, info9, info10, info11, int(info12)))
            cur.execute(query)
            con.commit()
            con.close()
            thankyou=thankyouScreen()        #connecting to thankyou screen
            widget.addWidget(thankyou)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class thankyouScreen(QDialog):                  #thanking the user
    def __init__(self):
        super(thankyouScreen, self).__init__()
        loadUi("thankyou.ui", self)
        image = QPixmap(r'C:\Users\User\Desktop\Python\Donor Lane App(project 12th)\icon.png')
        self.label.setPixmap(image)
        self.mail()

    def mail(self):
        global info1, info2, info3, info4, info5, info6, info7, info8, info9, info10, info11, info12
        import yagmail                            #generating certificate for appreciation
        from_ = 'donorlanemi@gmail.com'
        password = 'kmqfmoyfzczphztd'              #inapp password
        receiver = info4
        body = 'Thankyou for helping in this noble cause!'
        filename = r'C:\Users\User\Desktop\donorlane certificate.pdf'  # this file path should be given correctly
        yag = yagmail.SMTP(from_, password)
        yag.send(
            to=receiver,
            subject="text email",
            contents=body,
            attachments=filename)
        print("mail sent")


class adminScreen(QDialog):                    #admin function
    def gotohomepage(self):
        homescreen = Homepage()
        widget.addWidget(homescreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(adminScreen,self).__init__()
        loadUi("admin.ui",self)

        image = QPixmap(r'C:\Users\User\Desktop\Python\Donor Lane App(project 12th)\icon.png')
        self.label.setPixmap(image)

        self.view.clicked.connect(self.gotoviewscreen)          #connecting all the buttons
        self.remove.clicked.connect(self.gotoremovescreen)
        self.search.clicked.connect(self.gotosearchscreen)
        self.update.clicked.connect(self.gotoupdatescreen)
        self.back.clicked.connect(self.gotohomepage)


    def gotoviewscreen(self):                 #viewing records screen
        viewscreen = viewScreen()
        widget.addWidget(viewscreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoremovescreen(self):                #deleting records screen
        removescreen = removeScreen()
        widget.addWidget(removescreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotosearchscreen(self):                #searching records screen
        searchscreen = searchScreen()
        widget.addWidget(searchscreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoupdatescreen(self):                #updating record screen
        updatescreen = updateScreen()
        widget.addWidget(updatescreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class viewScreen(QDialog):               #Viewing the data
    def gotoadminpage(self):             #back button
        admin = adminScreen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(viewScreen,self).__init__()
        loadUi("view.ui",self)
        self.back.clicked.connect(self.gotoadminpage)
        self.tableWidget.setColumnWidth(0, 250)                  #setting the respective dimensions for columns
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setColumnWidth(3, 350)
        self.tableWidget.setColumnWidth(4, 250)
        self.tableWidget.setColumnWidth(5, 350)
        self.tableWidget.setColumnWidth(6, 250)
        self.tableWidget.setColumnWidth(7, 200)
        self.tableWidget.setColumnWidth(8, 200)
        self.tableWidget.setColumnWidth(9, 200)
        self.tableWidget.setColumnWidth(10, 300)
        self.tableWidget.setColumnWidth(11, 200)
        self.tableWidget.setHorizontalHeaderLabels(["Username", "Donor_Name", "Guardian_Name", "Email", "City",
                                                    "Address", "Phone_Number", "Gender","Blood_Grp", "DOB", "State", "Pincode"])
        self.loaddata()

    def loaddata(self):                  #connecting and loading the data in the table
        con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
        cur = con.cursor()
        q = 'SELECT * FROM DONOR_INFO LIMIT 50'

        self.tableWidget.setRowCount(50)
        tablerow = 0
        cur.execute(q)
        data = cur.fetchall()
        for row in data:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
            tablerow += 1
            print(data)
        con.close()



class removeScreen(QDialog):             #to remove a data
    def gotoadminpage(self):             #back button
        admin = adminScreen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(removeScreen,self).__init__()
        loadUi("remove.ui",self)
        self.submit.clicked.connect(self.removefunction)
        self.back.clicked.connect(self.gotoadminpage)


    def removefunction(self):
        user=self.usernamefield.text()                    #extracting info

        if len(user)==0:           #validifying
            self.error.setText("Please fill the details")
        elif len(user)<=5:
            self.error.setText("Username must have 6 characters")
        else:                                            #establishing connection
            con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
            cur = con.cursor()
            query = ("DELETE FROM DONOR_INFO WHERE USERNAME LIKE ('{}')").format(user)
            cur.execute(query)
            query1 = ("DELETE FROM LOGIN_CREDENTIALS WHERE USERNAME LIKE ('{}')").format(user)
            cur.execute(query1)
            con.commit()
            con.close()
            display = removedisplayScreen()            #connecting to display screen
            widget.addWidget(display)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class removedisplayScreen(QDialog):      #displaying the data after deletion

    def gotoadminpage(self):             #back button
        admin = adminScreen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(removedisplayScreen, self).__init__()
        loadUi("removedisplay.ui", self)
        self.back.clicked.connect(self.gotoadminpage)
        self.tableWidget.setColumnWidth(0,250)          #setting dimensions
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,250)
        self.tableWidget.setColumnWidth(3,350)
        self.tableWidget.setColumnWidth(4,250)
        self.tableWidget.setColumnWidth(5,350)
        self.tableWidget.setColumnWidth(6,250)
        self.tableWidget.setColumnWidth(7,200)
        self.tableWidget.setColumnWidth(8,200)
        self.tableWidget.setColumnWidth(9,200)
        self.tableWidget.setColumnWidth(10,300)
        self.tableWidget.setColumnWidth(11,200)
        self.tableWidget.setHorizontalHeaderLabels(["Username","Donor_Name","Guardian_Name","Email",
                                                    "City","Address","Phone_Number","Gender","Blood_Grp","DOB","State","Pincode"])
        self.loaddata()

    def loaddata(self):          #loading data and establishing connection
        con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
        cur = con.cursor()
        q = 'SELECT * FROM DONOR_INFO LIMIT 50'

        self.tableWidget.setRowCount(50)
        tablerow = 0
        cur.execute(q)
        data=cur.fetchall()
        for row in data:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
            tablerow += 1
            print(data)
        con.close()


class searchScreen(QDialog):         #searching data
    def gotoadminpage(self):           #back button
        admin = adminScreen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(searchScreen,self).__init__()
        loadUi("search.ui",self)
        self.submit.clicked.connect(self.searchdata)
        self.submit.clicked.connect(self.loaddata)
        self.back.clicked.connect(self.gotoadminpage)
        self.back.clicked.connect(self.gotoadminpage)
        self.tableWidget.setColumnWidth(0,250)             #setting dimensions
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,250)
        self.tableWidget.setColumnWidth(3,350)
        self.tableWidget.setColumnWidth(4,250)
        self.tableWidget.setColumnWidth(5,350)
        self.tableWidget.setColumnWidth(6,250)
        self.tableWidget.setColumnWidth(7,200)
        self.tableWidget.setColumnWidth(8,200)
        self.tableWidget.setColumnWidth(9,200)
        self.tableWidget.setColumnWidth(10,300)
        self.tableWidget.setColumnWidth(11,200)
        self.tableWidget.setHorizontalHeaderLabels(["Username","Donor_Name","Guardian_Name","Email","City",
                                                    "Address","Phone_Number","Gender","Blood_Grp","DOB","State","Pincode"])
        self.loaddata()

    def searchdata(self):
        nameD = self.namefield.text()          #extracting info

        if len(nameD) == 0:
            self.error.setText("Please fill the required details")

    def loaddata(self):                     #loading data and establishing connection
        nameD = self.namefield.text()
        con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
        cur = con.cursor()
        query = ("SELECT * FROM DONOR_INFO WHERE DONOR_NAME LIKE ('{}')").format(nameD)
        self.tableWidget.setRowCount(50)
        tablerow = 0
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
            tablerow += 1
            print(data)
        con.close()



class updateScreen(QDialog):     #updating a record

    def gotoadminpage(self):     #back button
        admin = adminScreen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(updateScreen,self).__init__()
        loadUi("update.ui",self)
        self.submit.clicked.connect(self.updatefunction)
        self.back.clicked.connect(self.gotoadminpage)


    def updatefunction(self):
        user=self.usernamefield.text()       #extracting details
        ph=self.phonefield.text()

        if len(user)==0 or len(ph)==0:           #validifying
            self.error.setText("Please fill the details")
        elif len(user)<=5:
            self.error.setText("Username must have 6 characters")
        elif len(ph)>10 or len(ph)<10:
            self.error.setText("Phone number should have 10 digits")

        else:                                   #establishing connection
            con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
            cur = con.cursor()
            query = ("UPDATE DONOR_INFO SET PHONE_NUMBER = {} WHERE USERNAME LIKE ('{}')").format(ph,user)
            cur.execute(query)
            con.commit()
            con.close()
            display = updatedisplayScreen()          #connecting to display screen
            widget.addWidget(display)
            widget.setCurrentIndex(widget.currentIndex() + 1)



class updatedisplayScreen(QDialog):           #displaying all the record after updation

    def gotoadminpage(self):                  #back button
        admin = adminScreen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def __init__(self):
        super(updatedisplayScreen, self).__init__()
        loadUi("updatedisplay.ui", self)
        self.back.clicked.connect(self.gotoadminpage)
        self.tableWidget.setColumnWidth(0,250)          #setting dimensions
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,250)
        self.tableWidget.setColumnWidth(3,350)
        self.tableWidget.setColumnWidth(4,250)
        self.tableWidget.setColumnWidth(5,350)
        self.tableWidget.setColumnWidth(6,250)
        self.tableWidget.setColumnWidth(7,200)
        self.tableWidget.setColumnWidth(8,200)
        self.tableWidget.setColumnWidth(9,200)
        self.tableWidget.setColumnWidth(10,300)
        self.tableWidget.setColumnWidth(11,200)
        self.tableWidget.setHorizontalHeaderLabels(["Username","Donor_Name","Guardian_Name","Email","City","Address",
                                                    "Phone_Number","Gender","Blood_Grp","DOB","State","Pincode"])
        self.loaddata()

    def loaddata(self):             #loading data and establishing connection
        con = ms.connect(host='localhost', user='root', password='DPSBN', database='DONORLANE')
        cur = con.cursor()
        q = 'SELECT * FROM DONOR_INFO LIMIT 50'

        self.tableWidget.setRowCount(50)
        tablerow = 0
        cur.execute(q)
        data=cur.fetchall()
        for row in data:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(str(row[11])))
            tablerow += 1
            print(data)
        con.close()



#main
app=QApplication(sys.argv)
homepage=Homepage()
widget=QStackedWidget()
widget.addWidget(homepage)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
info1=''
info2=''
info3=''
info4=''
info5=''
info6=''
info7=''
info8=''
info9=''
info10=''
info11=''
info12=''

try:
    sys.exit(app.exec())
except:
    print("THANKYOU FOR USING DONORLANE! Exiting...")
    print("Exited")
