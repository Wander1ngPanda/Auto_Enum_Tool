import argparse, subprocess
from argument_parser import arguments as args

ip, port, verbose, flag = args().getArgs()

print("IP: ", ip)

if port:
    ip = ip + ":" + port

if port == "80":
    subprocess.run(['curl', ip, '-s'], stdout=open('output.txt', 'w'))

