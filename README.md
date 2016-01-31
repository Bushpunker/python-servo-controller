# python-servo-controller
Python module to allow easy control of servo motors connected to the parallel port.

USAGE:
from servo import Servo


Usage:
from servo import Servo
import parallel
from multiprocessing import Process, Array

  servos = Servo(parallel.Parallel(0))
  pos = Array('d', [180, 180, 180])
  cont = Process(target=servos.controller, args=(pos,))
  cont.start()

  pos[0] = 90
	pos[1] = 52

This starts the servo controller in it's own seperate process, and by
changing the values (servo angles) in pos[] in your main code, the physical
position of the relevant servo will also be changed.

Connect the control wires of your servos to the data pins on the parallel
port (D0, D1, etc).

Using the above sample code: pos[0] controls the servo connected to D0, and
pos[1] controls the servo connected to D1, etc.
