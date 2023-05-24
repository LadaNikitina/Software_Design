import grpc
from datetime import datetime
import chat_pb2
import chat_pb2_grpc
import time

def run():
    channel = grpc.insecure_channel('localhost:50053')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    # Register the client
    name = input("Enter your name: ")
    # stub.RegisterClient(chat_pb2.Client(name=name))

    # Start sending and receiving messages
    try:
        while True:
            message = input("Enter a message: ")
            if message.lower() == 'exit':
                break
            stub.SendMessage(chat_pb2.ChatMessage(sender_name=name, text=message, timestamp=int(time.time())))
            responses = stub.ReceiveMessage(chat_pb2.Empty())
            for response in responses:
                print(f"{response.sender_name}: {response.text} {datetime.fromtimestamp(response.timestamp)}")
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()
