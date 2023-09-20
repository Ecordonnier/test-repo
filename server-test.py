#!/usr/bin/env python3

import fcntl
import os
import select
import sys
import time

class TestWorker(object):
    def __init__(self, din):
        self.input = din
        fcntl.fcntl(din, fcntl.F_SETFL, fcntl.fcntl(din, fcntl.F_GETFL) | os.O_NONBLOCK)
        self.build_pipes = {}
        self.queue = bytearray()

    def serve(self):
        while True:
            (ready, _, _) = select.select([self.input] + [i.input for i in self.build_pipes.values()], [] , [], 1)
            if self.input in ready:
                try:
                    r = self.input.read()
                    if len(r) == 0:
                        # EOF on pipe, server must have terminated
                        quit()
                    self.queue.extend(r)
                except (OSError, IOError):
                    pass
            if len(self.queue):
                    print("len(r)= %s" % (len(r)))
                    time.sleep(0.1)

worker = TestWorker(os.fdopen(sys.stdin.fileno(), 'rb'))
worker.serve()
