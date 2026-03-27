import grpc
from concurrent import futures
from src.grpc_gen import user_pb2, user_pb2_grpc


class UserServiceServicer(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f"Received request for user id: {request.id}")
        return user_pb2.UserResponse(
            id=request.id,
            name=f"User {request.id}",
            email=f"user{request.id}@example.com",
            is_active=True
        )


def serve(port: int = 50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"gRPC mock server started on port {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()