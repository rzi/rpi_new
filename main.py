#!/usr/bin/env python
#
import time,sys
import requests
# from datetime import datetime, date, time, timezone
import json
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# cmd = 'sudo digitemp_DS9097U  -a  -c /home/pi/Desktop/BMS/digitemp1.conf'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmd = 'digitemp1.conf'
    cmd1 = './temp'
    timefmt = '%Y-%m-%d %H:%M:%S'

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("PyQt App")
    window.setGeometry(100, 100, 280, 80)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)
    window.show()
    sys.exit(app.exec())

    while True:
        print("START1")
        # print(time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(2)
        fo = open(cmd1, "r+")
        Lines = fo.readlines()
        # print(Lines)
        count = 0
        for line in Lines:
            S = str.split(line, " ")
            # G = S[3]
            # print(G)
            # print(S)
            # count += 1
            # print("Line{}: {}".format(count, line.strip()))
            if S[2] == "Sensor":
            #     print (S)
                print (S[0], S[1], S[3], S[4],S[5], S[6])
                my_date = datetime.fromtimestamp(float(S[0])).strftime('%Y-%m-%d %H:%M:%S')
                print (my_date)
            #     mydate = datetime.datetime.fromtimestamp(float(S[0])).strftime('%Y-%m-%d')
            #     # print mydate
                mytime = datetime.fromtimestamp(float(S[0])).strftime('%H:%M:%S')
                print (mytime)
                # print S[0]
                my_string = S[0] + " " + S[1] + " " + S[6] + " " + S[4]
                print (my_string)
                try:
                    # Execute the SQL command
                    r = requests.post('https://tempapi.ct8.pl/addtemp', json={'my_epoch': S[0], 'nr_hex': S[1],'temp': S[6],'nr_czujnika': S[4]})
                except:
                    # Rollback in# case there is any error
                    print("błąd wysłania do API" )