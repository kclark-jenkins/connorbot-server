import configparser
import zerorpc
from ConnorBotRPC import ConnorBotRPC

class ConnorBot:
    configFile = 'connorbot.ini'
    config = None

    def __init__(self):
        print "ConnorBot constructor"
        self.config = configparser.ConfigParser()

        self.readConfig()
        self.startRpcServer()

    def readConfig(self):
        self.config.read(self.configFile);

    def buildRpcUrl(self):
        return self.config['rpc']['protocol'] + '://' + self.config['rpc']['listenAddress'] + ':' + self.config['rpc']['port']

    def showRunning(self, listeningOn):
        print 'ConnorBot RPC Server is online and listening at ' + listeningOn

    def startRpcServer(self):
        s = zerorpc.Server(ConnorBotRPC(self.buildRpcUrl()))
        s.bind(self.buildRpcUrl())
        s.run()

cbot = ConnorBot()