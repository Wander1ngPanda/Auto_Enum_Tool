import subprocess
from argument_parser import arguments as args

ip, port, verbose, flag = args().getArgs()


if port:
    ip = ip + ":" + port

if port == "80":
    procedure = subprocess.Popen(['echo', ip], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = procedure.communicate()
    print(output)

