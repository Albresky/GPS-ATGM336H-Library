import serial
import time

gpsSerial = serial.Serial("/dev/ttyAMA0",9600)

while True:
    line=str(str(gpsSerial.readline()))
    # 显示当前GPS信息
    if line.startswith("b\'$GNGGA"):
        print(line)
        line=str(line).split(',')
        try:
            if line[1]!=0 and line[3]!=0:
                jd=float(line[1][:2])+float(line[1][2:])/60
                wd=float(line[3][:3])+float(line[3][3:])/60
                print("经度 = {}\n维度 = {}\n".format(jd,wd))
        except:
            print("Locate ERROR!")
    elif line.startswith("b\'$GNRMC"):
        print(line)
        line=str(line).split(',')
        try:
            if line[0]!=0:
                hh =int(line[1][:2])+8
                mm=str(line[1][2:4])
                ss=str(line[1][4:6])
                print('Time = {}:{}:{}'.format(hh,mm,ss))
        except:
            print('Time ERROR!')
    time.sleep(0.5)
