# Yahboom G1 Tank Examples

This repository contains example code for controlling the [Yahboom G1 Tank Raspberry Pi kit](https://www.yahboom.net/study/G1-T-PI).

# Installing

#### 1. Clone to the Pi
SSH into the Pi and clone the repository.
```
$ git clone https://github.com/Smurf/g1_tank.git
$ cd g1_tank
```
#### 2. Install Dependencies
Use `pip3` to install the python dependencies for this project.
```
$ pip3 install -r requirements.txt
```

# Overview

READMEs are currently being generated for each example.

### 01-local-ssh-control

An example of using streameye to create a local stream on your LAN. The tank is controlled via keypresses in a SSH session.

### 02-twitch-control

This is a more complex example where the tank camera output is sent to a twitch.tv stream and can be controlled by chat.

### 03-web-control

Run a web server on the tank and host a low latency (~1 second) stream.

# TODO

- [ ] Add READMEs for each example with usage examples

