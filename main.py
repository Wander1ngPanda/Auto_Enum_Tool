import subprocess
from argument_parser import arguments as args

ip, port, verbose, flag, wordlist = args().getArgs()

if port == "80":
    url = f"http://{ip}:{port}/FUZZ.html"
    command = f"ffuf -w {wordlist}:FUZZ -u {url} -ic"
    procedure = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = procedure.communicate()
    print(output)

