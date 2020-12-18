#!/usr/bin/env python3

import pika
from random import randrange

def die_randomly():
    from sys import exit, stderr
    if randrange(10) < 2:
        stderr.write("decided to die randomy :(\n")
        exit(1)

def callback(ch, method, properties, body):
    die_randomly()
    print(" [x] Received %r" % body)
    ch.basic_publish(exchange='',routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                     body=str(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    QUEUE_NAME = 'best_queue_ever'
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    main()