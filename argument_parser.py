import argparse

class arguments:
    def __init__(self):
        self.args = self.parseArgs()

    def getArgs(self):
        return (self.args.ip, self.args.port, self.args.verbose, self.args.flag)
    
    def parseArgs(self):
        parser = argparse.ArgumentParser(description='Process an IP address')
        
        parser.add_argument('-ip', help='IP address', type=str, required=True)
        parser.add_argument('-p', '--port', help='Port number', required=False)
        parser.add_argument('-v', '--verbose', help='Increase output verbosity', required=False, action='store_true')
        parser.add_argument('-fg', '--flag', help='Flag Prefix', required=False) 
        
        
        return parser.parse_args()