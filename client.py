#!/usr/bin/env python3

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    main()