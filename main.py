#!/usr/bin/env python
from datetime import datetime

import sys
import time

import datetime as datetime
import requests
import requests as requests
from PyQt6.QtWidgets import QApplication, QLabel, QWidget


def display_time():
    current_time = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M:%S')
    label.setText(current_time)
    print('current_time:', current_time)

if __name__ == '__main__':

    # cmd = 'sudo digitemp_DS9097U  -a  -c /home/pi/Desktop/BMS/digitemp1.conf'
    # window()
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
        print("label")
        label = QLabel("START1")
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
                print(S[0], S[1], S[3], S[4], S[5], S[6])
                my_date = datetime.fromtimestamp(float(S[0])).strftime('%Y-%m-%d %H:%M:%S')
                print(my_date)
            #     mydate = datetime.datetime.fromtimestamp(float(S[0])).strftime('%Y-%m-%d')
            #     # print mydate
                mytime = datetime.fromtimestamp(float(S[0])).strftime('%H:%M:%S')
                print(mytime)
                # print S[0]
                my_string = S[0] + " " + S[1] + " " + S[6] + " " + S[4]
                print(my_string)
                try:
                    # Execute the SQL command
                    r = requests.post('https://tempapi.ct8.pl/addtemp', json={'my_epoch': S[0], 'nr_hex': S[1],'temp': S[6],'nr_czujnika': S[4]})
                except:
                    # Rollback in# case there is any error
                    print("błąd wysłania do API" )

            #     #     db2.rollback()
            #     #   try:
            #     # Execute the SQL command
            #     #      cursor.execute("""
            #     #      INSERT INTO pomiary2 (my_epoch, nr_hex, temp,nr_czujnika )
            #     #      VALUES
            #     #      (%s,%s,%s,%s)
            #     #    """, (int(S[0]), S[1],S[6], S[4] ));
            #     # Commit your changes in the database
            #     #     db.commit()
            #     # print "zapis ", time.strftime('%Y-%m-%d %H:%M:%S')
            #     #   except:
            #     # Rollback in# case there is any error
            #     #    db.rollback()
            #
            #     # try:
            #     #     # Execute the SQL command
            #     #     cursor2.execute("""
            #     #     INSERT INTO pomiary2 (my_epoch, nr_hex, temp,nr_czujnika )
            #     #     VALUES
            #     #     (%s,%s,%s,%s)
            #     #     """, (int(S[0]), S[1], S[6], S[4]));
            #     #
            #     #     # Commit your changes in the database
            #     #     db2.commit()
            #     #     # print "zapis ", time.strftime('%Y-%m-%d %H:%M:%S')
            #     #
            #     # except:
            #     #     # Rollback in# case there is any error
            #     #     db2.rollback()

        # disconnect from server
        # db.close() # poza if
        # db2.close()  # poza if


