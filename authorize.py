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

#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,440)
cap.set(4,480)

# with open('myDataFile.text') as f:
#     myDataList = f.read().splitlines()

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        # print(myData)

        myDataList = myData.split()
        try:
            uurn = myDataList[4]
            scan ="SELECT scans FROM cards WHERE urn = %s"
            mycursor.execute(scan, (uurn,))
            hey = mycursor.fetchall()
            hey = str(hey).strip('[](),')
            print(hey)
            # print(str("('" + myDataList[4] + "',)"))
            scancount = int(hey)

        
            urnst = str("('" + myDataList[4] + "',)")
            if urnst in output_list:
                myOutput = 'Authorized'
                myColor = (0,255,0)
                scancount = scancount + 1
                update = "UPDATE cards SET scans = %s WHERE urn = %s"
                mycursor.execute(update, (scancount,uurn,))

        # elif myData in output_list:
        #     myOutput = 'Un-Authorized'
        #     myColor = (0, 0, 255)

        except:
            myOutput = 'Un-Authorized'
            scancount = 0
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput+ ":-" + str(scancount),(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)

    cv2.imshow('Result',img)
    cv2.waitKey(1000)
    