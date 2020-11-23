import RPi.GPIO as GPIO
import sys, os, time
from smurf.codes import G1Tank
import requests
import argparse
import asyncio
import json
import logging
import platform
import ssl

from aiohttp import web


#Create our tank
my_tank = G1Tank()

ROOT = os.path.dirname(__file__)
ROOT = os.path.join(ROOT, "www")

class TankServer:

    def __init__(self, server_root:str, tank_obj:G1Tank, args):
        self.tank = tank_obj
        self.args = args
        if self.args.cert_file:
            ssl_context = ssl.SSLContext()
            ssl_context.load_cert_chain(self.args.cert_file, args.key_file)
        else:
            ssl_context = None

        self.root = server_root
        self.app = web.Application()
        #self.app.on_shutdown.append(self.on_shutdown)
        self.app.router.add_get("/", self.index)
        self.app.router.add_post("/robo/cam_up", self.cam_up)
        self.app.router.add_post("/robo/cam_down", self.cam_down)
        self.app.router.add_post("/robo/cam_left", self.cam_left)
        self.app.router.add_post("/robo/cam_right", self.cam_right)
  

        self.app.router.add_post("/robo/forward", self.forward)
        self.app.router.add_post("/robo/reverse", self.reverse)
        self.app.router.add_post("/robo/spin_left", self.spin_left)
        self.app.router.add_post("/robo/spin_right", self.spin_right)
        web.run_app(self.app, host=self.args.host, port=args.port, ssl_context=ssl_context)

    async def index(self, request):
        content = open(os.path.join(ROOT, "index.html"), "r").read()
        return web.Response(content_type="text/html", text=content)
    async def cam_up(self, request):
        self.tank.gimbal_y(5)
        return web.Response(status=200)
    
    async def cam_down(self, request):
        self.tank.gimbal_y(-5)
        return web.Response(status=200)

    async def cam_left(self, request):
        self.tank.gimbal_x(5)
        return web.Response(status=200)

    async def cam_right(self, request):
        self.tank.gimbal_x(-5)
        return web.Response(status=200)
    
    async def forward(self, request):
        self.tank.forward(0.5)
        return web.Response(status=200)

    async def reverse(self, request):
        self.tank.reverse(0.5)
        return web.Response(status=200)
    
    async def spin_left(self, request):
        self.tank.spin_left(0.5)
        return web.Response(status=200)
    
    async def spin_right(self, request):
        self.tank.spin_right(0.5)
        return web.Response(status=200)



   



def main():
    global ROOT
    parser = argparse.ArgumentParser(description="MJPEG webcam")
    parser.add_argument("--cert-file", help="SSL certificate file (for HTTPS)")
    parser.add_argument("--key-file", help="SSL key file (for HTTPS)")
    parser.add_argument(
        "--host", default="0.0.0.0", help="Host for HTTP server (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port", type=int, default=8080, help="Port for HTTP server (default: 8080)"
    )
    parser.add_argument("--verbose", "-v", action="count")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    #Initialize Tank
    my_tank.gimbal_x_angle = 90
    my_tank.gimbal_y_angle = 90
    my_tank.gimbal_y(0)
    my_tank.gimbal_x(0)
    server = TankServer(ROOT, my_tank, args)

main()
if __name__ == "main":
    main()
