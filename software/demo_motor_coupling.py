#!/usr/bin/env python3
from motor_usb import MotorUsbController

KP = 1.0
KD = 0.03


def main(kp=KP, kd=KD):
    with MotorUsbController(timeout_ms=20) as robot:
        robot.initialize()
        q0_start = robot.m0.q
        q1_start = robot.m1.q

        while True:
            robot.m0.set(q=q0_start + robot.m1.q - q1_start, v=robot.m1.v, kp=kp, kd=kd)
            robot.m1.set(q=q1_start + robot.m0.q - q0_start, v=robot.m0.v, kp=kp, kd=kd)
            robot.update()


if __name__ == "__main__":
    main()
