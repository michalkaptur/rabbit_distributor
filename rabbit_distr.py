import pika
import uuid

import config

class RpcRunner:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(queue=self.callback_queue, on_message_callback=self.on_resp, auto_ack=True)

        self.response = None

    def on_resp(self, ch, method, properties, body):
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self, value):
        self.corr_id = str(uuid.uuid4())
        props = pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.corr_id)
        self.channel.basic_publish(exchange='', routing_key=config.QUEUE_NAME, body=str(value), properties=props)
        while not self.response:
            self.connection.process_data_events()
        return self.response

def go():
    result = RpcRunner().call("foo")
    print("got response: {}".format(result.decode()))