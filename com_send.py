
from concurrent.futures import thread
from curses.ascii import isdigit
from socket import timeout
from threading import Thread
import serial, time
import keyboard

#Версия для Windows

''' Скрипт отпрвяет каждые 300мс 0x01 на датчик тока, что соответствует ASM-1500
В терминал выводит, что получил от датчиика.(12 байт 2bffff 2bтокA 2bтокB 2bТокC 4bCRC)
Можно подключиться к uart или через переходник к rs485


Чуть позже изменю скрипт, чтобы он предлагал табличку с asm-мами и номерами
и отправлял команду соответствующую датчику тока.
Для тест пока asm1500'''


run = 1

def exit_check():
    global run
    while run == 1:
        if keyboard.is_pressed("P"):
            run = 0
            exit()

def com_work():
    global run

    print("\n\n**********************************")
    print("Введите номер COM порта для соединения или пустую строку для выхода.")
    print("Во времня обмена данными для выхода нажмите <P>")
    print("**********************************")

    com_n_str = input()

    if not com_n_str:
        print("Выход")
        exit()
    
    if not com_n_str.isdigit():
        print("Вводите только числовые значения\nВыход")
        exit()

    SERIAL_PORT = "COM" + str(com_n_str)     # Пользователи Windows, замените на "COMx"

    try:
        ser = serial.Serial(SERIAL_PORT, 115200, timeout=1, parity=serial.PARITY_NONE)
    except:
        print("Ошибка подключения к COM ")
        exit()


    print("***Старт***")

    byte_list = []

    while run == 1:
        ser.write(0x01)
        byte_list = ser.read(12)
        print(byte_list)
        time.sleep(0.3)



if __name__ == "__main__":
    thread1 = Thread(target=exit_check)
    thread2 = Thread(target=com_work)
    thread1.start()
    thread2.start()
