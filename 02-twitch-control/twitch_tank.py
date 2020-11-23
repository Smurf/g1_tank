import RPi.GPIO as GPIO
import sys, os, time
from smurf.codes import G1Tank
import requests
import twitch

#Create our tank
my_tank = G1Tank()

def check_chat(message):
    global my_tank
    #{'channel': 'smurf_codes', 'sender': 'mr_roverboto', 'text': 'test', 'helix': None, 'chat': <twitch.chat.chat.Chat object at 0xb5fa11b0>}
    print(message.text)
    if(message.text[:1] == "!"):
        cmd = message.text[1:] #Remove first char
        print(f"Found cmd {cmd}")
        if(cmd == "forward"):
            my_tank.forward(0.5)
        elif(cmd == "left"):
            my_tank.spin_left(0.25)
        elif(cmd == "right"):
            my_tank.spin_right(0.25)
        elif(cmd == "about face"):
            my_tank.spin_right(1.65)
        elif(cmd == "reverse"):
            my_tank.reverse(0.5)
        elif(cmd == "stop"):
            my_tank.brake()
        elif(cmd == "beep"):
            my_tank.beep(0.5)
        elif(cmd == "cam up"):
            my_tank.gimbal_y(20)
        elif(cmd == "cam down"):
            my_tank.gimbal_y(-20)
        elif(cmd == "cam left"):
            my_tank.gimbal_x(20)
        elif(cmd == "cam right"):
            my_tank.gimbal_x(-20)
        elif(cmd == "illuminate"):
            my_tank.toggle_led()
    #Update HUD
    with open('tank_telemetry.txt', 'w') as telem:
        telem_str = f"""Gimbal X Angle: {my_tank.gimbal_x_angle}/180\nGimbal Y Angle: {my_tank.gimbal_y_angle}/180
\n\n\n\n\n\n\n\n\n\n\n
Front                               Rear"""
        telem.write(telem_str)

def main():
    #Initialize Tank
    my_tank.gimbal_x_angle = 90
    my_tank.gimbal_y_angle = 90
    my_tank.gimbal_y(0)
    my_tank.gimbal_x(0)

    #First lets get our oauth2 key from a local file
    with open("twitch_oauth2", 'r') as f:
        oauth2_code = f.read()
        f.close() #Be sure to clean up

    #Connect to twitch chat
    twitch.Chat(channel='#smurf_codes', nickname='smurf_codes', oauth=f"oauth:{oauth2_code}").subscribe(
            lambda message: check_chat(message))
main()
if __name__ == "main":
    main()
