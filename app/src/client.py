"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging
import argparse

import grpc
# import echo_pb2_grpc
# import echo_pb2

protos = grpc.protos("echo.proto")
services = grpc.services("echo.proto")


_DESCRIPTION = "Get a greeting from a server."


def run(server_address):
    with grpc.insecure_channel(server_address) as channel:
        stub = services.EchoServerStub(channel)
        response = stub.SayHello(protos.EchoRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    parser.add_argument("server",
                        default=None,
                        help="The address of the server.")
    args = parser.parse_args()
    logging.basicConfig()
    run(args.server)
