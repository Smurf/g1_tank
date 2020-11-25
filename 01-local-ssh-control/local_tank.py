import RPi.GPIO as GPIO
import sys, termios, tty, os, time
import enum
from threading import Thread
from smurf.codes import G1Tank
import requests
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    my_tank = G1Tank()
    my_tank.gimbal_x_angle = 90
    my_tank.gimbal_y_angle = 90
    my_tank.gimbal_y(0)
    my_tank.gimbal_x(0)
    while True:
        char = getch()
        if(char == "a"):
            my_tank.spin_left(1.0)
        elif(char == "d"):
            my_tank.spin_right(1.0)
        elif(char == "s"):
            my_tank.reverse(1.0)
        elif(char == "z"):
            my_tank.brake()
        elif(char == "w"):
            my_tank.forward(1.0)
        elif(char == "b"):
            my_tank.beep(0.5)
        elif(char == "i"):
            my_tank.gimbal_y(5)
        elif(char == "k"):
            my_tank.gimbal_y(-5)
        elif(char == "j"):
            my_tank.gimbal_x(5)
        elif(char == "l"):
            my_tank.gimbal_x(-5)
        elif(char == "t"):
            exit(1)
main()
if __name__ == "main":
    main()
