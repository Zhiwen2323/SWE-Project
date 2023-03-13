import pika
from google.cloud import storage

# Set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue for logs
channel.queue_declare(queue='logs')

# Set up GCS client
storage_client = storage.Client()
bucket = storage_client.bucket('my_bucket')


# Callback function to consume logs and write to GCS
def callback(ch, method, properties, body):
    # TODO Write log to GCS
    return


# Set up consumer to consume logs from RabbitMQ and call callback function
channel.basic_consume(queue='logs', on_message_callback=callback, auto_ack=True)

# Start consuming logs
print('Consuming logs...')
channel.start_consuming()

from collections import OrderedDict