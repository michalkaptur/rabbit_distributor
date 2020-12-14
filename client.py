#!/usr/bin/env python3

import pika
from random import randrange
from sys import exit, stderr

def callback(ch, method, properties, body):
    if randrange(10) < 2:
        stderr.write("decided to die")
        exit(1)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(queue='hello', on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    main()