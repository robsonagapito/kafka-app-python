from confluent_kafka import KafkaError
from services.message import Message
from services.kafka import Kafka

message = Message()
producer = Kafka()

kafka = Kafka()
kafka.group = 'aplicacao'
consumer = kafka.connect_consumer('tdc-entrada','<<< APLICAÇÃO >>>')

try:
    while True:
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print('Received message: {0}'.format(msg.value()))
            msgAux = message.handle_message(msg.value())
            producer.send_message('tdc-saida',msgAux)
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()