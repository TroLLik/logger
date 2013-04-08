#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#Serial Logger v3.3

import os, sys, serial, datetime, time, csv, configg

try:
    import serial
except ImportError:
    print("Cannot find 'serial' module. Please install it and try again.")
    sys.exit(0)

dt = datetime.datetime.now()
try:
    ser = serial.Serial(configg.SERIAL_PORT, configg.SERIAL_SPEED)
except :
    print("COM port error!")
    sys.exit(0)

buf1 = 'empy'
buf2 = 'empy'

logfile1 = open(str(dt.strftime('%Y')+'-'+dt.strftime('%m')+'-'+dt.strftime('%d')+'_'+dt.strftime('%H')+'-'+dt.strftime('%M')+'-'+dt.strftime('%S'))+'_serial_logger_Sensor1.log', 'w', encoding='UTF-8')
logfile2 = open(str(dt.strftime('%Y')+'-'+dt.strftime('%m')+'-'+dt.strftime('%d')+'_'+dt.strftime('%H')+'-'+dt.strftime('%M')+'-'+dt.strftime('%S'))+'_serial_logger_Sensor2.log', 'w', encoding='UTF-8')
logtable = csv.writer(open(str(dt.strftime('%Y')+'-'+dt.strftime('%m')+'-'+dt.strftime('%d')+'_'+dt.strftime('%H')+'-'+dt.strftime('%M')+'-'+dt.strftime('%S'))+'_serial_logger.csv', 'w', newline='', encoding='windows-1251'), dialect='excel')

logtable.writerow(['Sensor1','Sensor2'])

def start_log ():

    return

    serstr = ser.readline().strip()
    print (serstr.decode('utf-8'))
    if serstr.decode('utf-8')[:3] == 'a1:':
            log1 = logfile1.write(serstr.decode('utf-8')[3:]+'\n')
            buf1=str(serstr.decode('utf-8'))[3:]
            type (log1)
    elif serstr.decode('utf-8')[:3] == 'a2:':
            log2 = logfile2.write(serstr.decode('utf-8')[3:]+'\n')
            buf2=str(serstr.decode('utf-8'))[3:]
            type (log2)
    else:
        print ('Damaged incoming string!')
    return

if os.name == 'posix':
    import select, termios
    t1 = time.clock()
    def kbhit():
        r = select.select([sys.stdin], [], [], 0)
        return bool(r[0])

    if __name__ == '__main__':
        fd = sys.stdin.fileno()
        old_term = termios.tcgetattr(fd)
        new_term = termios.tcgetattr(fd)
        new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

        try:
            termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

            while True:
                if kbhit():
                    ch = sys.stdin.read(1)
                    break
                #Действие
                if buf1 != 'empy' and buf2 != 'empy':
                    logtable.writerow([buf1, buf2])
                    buf1 = 'empy'
                    buf2 = 'empy'

                serstr = ser.readline().strip()
                print (serstr.decode('utf-8'))
                if serstr.decode('utf-8')[:3] == 'a1:':
                    log1 = logfile1.write(serstr.decode('utf-8')[3:]+'\n')
                    buf1=str(serstr.decode('utf-8'))[3:]
                    type (log1)
                elif serstr.decode('utf-8')[:3] == 'a2:':
                    log2 = logfile2.write(serstr.decode('utf-8')[3:]+'\n')
                    buf2=str(serstr.decode('utf-8'))[3:]
                    type (log2)
                else:
                    print ('Damaged incoming string!')
            #Действие по anykey
            t2 = time.clock()
            dt=t2-t1
            print ('\nTime: '+str(round(dt*100,2))+'s.')
            log1 = logfile1.write('\nTotal time: '+str(round(dt*100,2))+'s.\n')
            type (log1)
            log2 = logfile2.write('\nTota time: '+str(round(dt*100,2))+'s.\n')
            type (log2)
            logtable.writerow([])
            logtable.writerow(['Total time: '+str(round(dt*100,2))+'s.'])
            logfile1.close()
            logfile2.close()
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

elif os.name == 'nt':
    import msvcrt
    t1 = time.clock()
    while not msvcrt.kbhit():
        if buf1 != 'empy' and buf2 != 'empy':
            logtable.writerow([buf1, buf2])
            buf1 = 'empy'
            buf2 = 'empy'

        serstr = ser.readline().strip()
        print (serstr.decode('utf-8'))
        if serstr.decode('utf-8')[:3] == 'a1:':
            log1 = logfile1.write(serstr.decode('utf-8')[3:]+'\n')
            buf1=str(serstr.decode('utf-8'))[3:]
            type (log1)
        elif serstr.decode('utf-8')[:3] == 'a2:':
            log2 = logfile2.write(serstr.decode('utf-8')[3:]+'\n')
            buf2=str(serstr.decode('utf-8'))[3:]
            type (log2)
        else:
            print ('Damaged incoming string!')
    #Действие по anykey
    t2 = time.clock()
    dt=t2-t1
    print ('\nTime: '+str(round(dt,2))+'s.')
    log1 = logfile1.write('\nTotal time: '+str(round(dt,2))+'s.\n')
    type (log1)
    log2 = logfile2.write('\nTota time: '+str(round(dt,2))+'s.\n')
    type (log2)
    logtable.writerow([])
    logtable.writerow(['Total time: '+str(round(dt,2))+'s.'])
    logfile1.close()
    logfile2.close()
else:
    print ('Wrong configg!');