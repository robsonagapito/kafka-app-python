from confluent_kafka import Producer, Consumer

class Kafka():

	def __init__(self):
		self.brokers =  'localhost:9092'
		self.group = ''

	def send_message(self, topico, message):
		p = Producer({'bootstrap.servers': self.brokers})
		p.produce(topico, key='1', value=message)
		p.flush(30)

	def connect_consumer(self, topico, titulo):
		settings = {
				'bootstrap.servers': self.brokers,
				'group.id': self.group,
				'client.id': 'client-1',
				'enable.auto.commit': True,
				'session.timeout.ms': 6000,
				'default.topic.config': {'auto.offset.reset': 'smallest'}
				}
		print(titulo)
		c = Consumer(settings)
		c.subscribe([topico])
		return c



