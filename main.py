import argparse, subprocess, os, sys


parser = argparse.ArgumentParser(description='Process an IP address')
parser.add_argument('-ip', help='IP address', type=str, required=True)
parser.add_argument('-p', '--port', help='Port number', required=False)
parser.add_argument('-v', '--verbose', help='Increase output verbosity', required=False, action='store_true')
parser.add_argument('-fg', '--flag', help='Flag Prefix', required=False) 
args = parser.parse_args()

ip = args.ip
port = args.port
verbose = args.verbose
flag = args.flag

if port:
    ip = ip + ":" + port

if port == "80":
    subprocess.run(['curl', ip, '-s'], shell=True)

