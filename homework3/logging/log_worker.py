import pika
import boto3

# Set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue for logs
channel.queue_declare(queue='logs')

# Set up S3 client
s3 = boto3.client('s3')


# Callback function to consume logs and write to S3
def callback(ch, method, properties, body):
    # TODO Write log to S3
    return


# Set up consumer to consume logs from RabbitMQ and call callback function
channel.basic_consume(queue='logs', on_message_callback=callback, auto_ack=True)

# Start consuming logs
print('Consuming logs...')
channel.start_consuming()