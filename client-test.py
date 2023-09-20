#!/usr/bin/env python3

import subprocess
import time
import string
import random

#file=open('file.txt','rb')
input_data = random.randbytes(100_000_000)
print("start test worker")
worker = subprocess.Popen(["./server-test.py"], stdout=1, stdin=subprocess.PIPE)
print("after start test worker")
start1 = time.time()
worker.stdin.write(input_data)
end1 = time.time()
print("stdin.write took %s" % (end1 - start1))
