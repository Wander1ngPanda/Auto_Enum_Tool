import argparse

class arguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Process an IP address')
        self.parser.add_argument('-ip', help='IP address', type=str, required=True)
        self.parser.add_argument('-p', '--port', help='Port number', required=False)
        self.parser.add_argument('-v', '--verbose', help='Increase output verbosity', required=False, action='store_true')
        self.parser.add_argument('-fg', '--flag', help='Flag Prefix', required=False) 
        self.args = self.parser.parse_args()

    def getArgs(self):
        return (self.args.ip, self.args.port, self.args.verbose, self.args.flag)