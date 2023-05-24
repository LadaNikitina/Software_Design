import grpc
from concurrent import futures
import time
from datetime import datetime

import chat_pb2
import chat_pb2_grpc


class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.messages = []
        self.clients = []

    def SendMessage(self, request, context):
        message = {'sender_name': request.sender_name, 'text': request.text, 'timestamp': request.timestamp}
        self.messages.append(message)
        print(f"Received message from {request.sender_name}: {request.text} {datetime.fromtimestamp(request.timestamp)}")
        self.BroadcastMessage(request)
        return chat_pb2.Empty()

    def ReceiveMessage(self, request, context):
        for message in self.messages:
            yield chat_pb2.ChatMessage(sender_name=message['sender_name'], text=message['text'],
                                       timestamp=message['timestamp'])
            # self.messages.remove(message)

    def BroadcastMessage(self, request):
        for client in self.clients:
            if client['name'] != request.sender_name:
                response = chat_pb2.ChatMessage(sender_name=request.sender_name, text=request.text,
                                                timestamp=request.timestamp)
                try:
                    client['stub'].ReceiveMessage(response)
                except:
                    print(f"Unable to send message to client {client['name']}")

    def RegisterClient(self, request, context):
        client = {'name': request.name,
                  'stub': chat_pb2_grpc.ChatServiceStub(context.invocation_metadata()[0][1])}

        self.clients.append(client)
        print(f"Registered client {request.name}")
        return chat_pb2.Empty()


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Chat server started...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()
