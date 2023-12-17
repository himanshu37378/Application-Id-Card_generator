from kivymd.app import MDApp 
from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    port = 4306,
    user="root",
    passwd="",
    database="id_card"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT urn FROM cards")
myresult = mycursor.fetchall()
 
output_list = []
for row in myresult:
    output_list.append(str(row))

print(output_list)


KV = '''
MDScreen:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
    MDTopAppBar:
        id: toolbar
        title: "Authentication Application.."
        elevation: 4
        pos_hint: {'top': 1}

    Image:
        size_hint_y: 0.7
        size_hint_x: 0.7
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        source: "assets/logo-gne.png"

    MDRaisedButton:
        id: 'auth_button"
        text: "AUTHENTICATE"
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_release: app.authenticate()
'''

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen

    def authenticate(self):


        #authenticate Screen
        # authenticate_screen = Toplevel(master)
        # authenticate_screen.title('Authentication App')
        # authenticate_screen.minsize(height=850,width=380)
        # authenticate_screen.configure(bg='#D9FFF4')

        # #Labels
        # Label(authenticate_screen, text = "Authentication System", font=('Calibri',22),bg='#D9FFF4',anchor = 'center', width = 27).grid(row=0,sticky=N,pady=25)

        #funtioning

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3,240)
        self.capture.set(4,280)

        # with open('myDataFile.text') as f:
        #     myDataList = f.read().splitlines()

        while True:

            success, img = self.capture.read()
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                # print(myData)

                myDataList = myData.split()
                
                # print(myDataList)
                # print(str("('" + myDataList[4] + "',)"))

                try:
                    if str("('" + myDataList[4] + "',)") in output_list:
                        myOutput = 'Authorized'
                        myColor = (0,255,0)
                
                # elif myData in output_list:
                #     myOutput = 'Un-Authorized'
                #     myColor = (0, 0, 255)

                except:
                    myOutput = 'Un-Authorized'
                    myColor = (0, 0, 255)

                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,myColor,5)
                pts2 = barcode.rect
                cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,myColor,2)

            cv2.imshow('Result',img)
            cv2.waitKey(1)


ma = MainApp()
ma.run()