from Movement import Movement
import zerorpc

class ConnorBotRPC:
    movement = None

    def __init__(self, status):
        print "ConnorBotRPC online and listening on " + status
        self.movement = Movement()

    @zerorpc.stream
    def move(self, direction, speed):
        self.movement.move(1, 1)
        return self.movement.move(direction, speed)