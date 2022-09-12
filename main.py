from lib2to3.pgen2 import driver
from urllib import request

from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
import grpc
import log

import rides_pb2 as pb
import rides_pb2_grpc as rpc

def new_ride_id():
        return uuid4().hex

class Rides(rpc.RidesServicer):
        def Start(self, req, context):
                log.info('ride: %r', req) 

                ## TODO: Store ride in Database

                ride_id = new_ride_id()
                return pb.StartRequest(id=ride_id)


def start_service():
        import config
        server = grpc.server(ThreadPoolExecutor())
        rpc.add_RidesServicer_to_server(Rides(), server)

        addr = f'[::]:{config.port}'
        server.add_insecure_port(addr)
        server.start()

        log.info('server ready on %s', addr)
        server.wait_for_termination()

request = pb.StartRequest(
        car_id = 95,
        driver_id = "McQueen",
        passenger_ids=['p1', 'p2', 'p3'],
)

def chapter1():
        print(request)

        ## region Marshal
        data = request.SerializeToString()

        request2 = pb.StartRequest()
        request2.ParseFromString(data)

        print(data)
        print(request2)

if __name__ == '__main__':
        # chapter1()
        start_service()
