import grpc
from src.grpc_gen import user_pb2, user_pb2_grpc


class GrpcUserClient:
    def __init__(self, host: str = "localhost", port: int = 50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    def get_user(self, user_id: int):
        request = user_pb2.UserRequest(id=user_id)
        try:
            response = self.stub.GetUser(request)
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()} - {e.details()}")
            return None

    def close(self):
        self.channel.close()