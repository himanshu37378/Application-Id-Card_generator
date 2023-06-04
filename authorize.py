import cv2
import numpy as np
from pyzbar.pyzbar import decode
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    port = 4306,
    user="hello",
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

#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

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