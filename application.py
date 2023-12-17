from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import mysql.connector





# Host: sql12.freesqldatabase.com
# Database name: sql12658209
# Database user: sql12658209
# Database password: 1lwtJTZjGN
# Port number: 3306

# ..........................................................................
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

# ............................................................................


def authenticate():

    #funtioning

    cap = cv2.VideoCapture(0)
    cap.set(3,840)
    cap.set(4,380)

    # with open('myDataFile.text') as f:
    #     myDataList = f.read().splitlines()

    while True:
 
        success, img = cap.read()
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

# .............................................................................
master = Tk()
master.title('Authentication App')
master.minsize(height=850,width=380)
master.configure(bg='#D9FFF4')


img = Image.open('logo-gne.png')
img = img.resize((280,280))
img = ImageTk.PhotoImage(img)

Label(master, text = "Authentication System", font=('Calibri',22),bg='#D9FFF4').grid(row=0,sticky=N,pady=25)
Label(master, text = "It is the authentication system for GNE students", font=('Calibri',16),bg='#D9FFF4').grid(row=1,sticky=N,)
Label(master, image=img,bg='#D9FFF4').grid(row=2,sticky=N,pady=25)

Button(master, text="Authenticate", font=('Calibri',16),width=25,command=authenticate, bg='#2DA79D').grid(row=3,sticky=N,pady=50)


master.mainloop()
# ..................................................................................