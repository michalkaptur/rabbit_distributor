#!/usr/bin/env python3

import pika
from random import randrange
import config

def log(string):
    print('[worker] {}'.format(string))

def die_randomly():
    from sys import exit, stderr
    if randrange(10) < 2:
        stderr.write("decided to die randomly :(\n")
        exit(1)

def callback(ch, method, properties, body):
    die_randomly()
    log("received %r" % body)
    ch.basic_publish(exchange='',routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                     body=str(body)+' and some magic dust')
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=config.QUEUE_NAME)
    channel.basic_consume(queue=config.QUEUE_NAME, on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    main()