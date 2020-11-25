# 01-local-ssh-control

This example gives simple keyboard and mouse control of the G1 tank.

## Using This Example

> **NOTE:** You will need the dependencies installed to use this example. See the main README file for information.

### Starting the Example
1. SSH into the Pi.
2. Start the webcam stream in the background **(optional)**.
    - `nohup ./start_stream.sh </dev/null &`
3. Start the `local_tank.py` script.
    - `python3 local_tank.py`
4. With focus still on the terminal use the controls below to move the tank and camera.

#### Stopping the Example
1. Press `T` to exit the python script.
2. Run `killall streameye` to stop the webcam stream.

### Tank Controls

The tank itself is controlled with the following keys.

> **NOTE** You must have an active SSH session **with keyboard focus** to the pi running the `local_tank.py` for the controls to work. See **Using This Example** above for details.

|    Action    | Button |
|:------------:|:------:|
|    Forward   |    W   |
|    Reverse   |    S   |
|  Rotate Left |    A   |
| Rotate Right |    D   |
| Beep         |    B   |

### Camera Gimbal Controls

The camera is controlled with the following keys.

|   Action  | Button |
|:---------:|:------:|
|  Tilt Up  |    I   |
| Tilt Down |    K   |
|  Pan Left |    J   |
| Pan Right |    L   |
