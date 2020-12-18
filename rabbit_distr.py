import pika
import uuid

class RcpRunner:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(queue=self.callback_queue, on_message_callback=self.on_resp, auto_ack=True)

    def on_resp(self, ch, method, properties, body):
        print("recived response %s" % body.decode())

    def call(self, value):
        self.corr_id = str(uuid.uuid4())
        props = pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.corr_id)
        self.channel.basic_publish(exchange='', routing_key='best_queue_ever', body=str(value), properties=props)
        self.channel.start_consuming()

def go():
    runner = RcpRunner()
    runner.call("foobar")