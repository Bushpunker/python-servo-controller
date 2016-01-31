#
# Module providing PWM servo control through the parallel port.
#
# servo/servo.py
#
# Copyright (c) 2015-2016, Darryl Bartlett
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of author nor the names of any contributors may be
#    used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
import time


#
# The 'Servo' class
#

class Servo():
    '''
    Usage:  from servo import Servo
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
    '''

    def __init__(self, ppp):
        self.ppp = ppp
        self.freq = 1.0/50    # frequency = 50Hz

    def controller(self, pos):
        while True:
            total = 0
            for i in range(len(pos)):
                pulse = (pos[i] / 100000) + 0.0005
                total += pulse
                self.ppp.setData(1 << i)
                time.sleep(pulse)
                self.ppp.setData(0)
            time.sleep(self.freq - total)
