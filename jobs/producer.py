import pika
import json

params = pika.URLParameters('amqps://zmolfmcm:Bi54NdynRS3s2kzskFKkFhZL9H9zu2A_@chimpanzee.rmq.cloudamqp.com/zmolfmcm')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
    print('published')