from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from pywikibot.comms.eventstreams import EventStreams


producer_configs = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_configs)

schema_registry_configs = {'url': 'http://0.0.0.0:8081'}
schema_registry_client = SchemaRegistryClient(conf=schema_registry_configs)


wikimedia_stream = EventStreams(streams='recentchange')
kafka_topic = 'wikimedia_raw'
string_serializer = StringSerializer('utf-8')


schema = """
    {
        "title": "Recent Change",
        "type": "object"
    }
"""

json_serializer = JSONSerializer(
    schema_str=schema, schema_registry_client=schema_registry_client)


def delivery_status_callback(error, message):
    if error is not None:
        print("Error delivering message: ", error)
    else:
        print("Successfully delivered message: ", message.key())
        print("Topic: ", message.topic())
        print("Partition: ", message.partition())


while True:
    producer.poll(0)
    new_change = next(iter(wikimedia_stream))
    print(new_change)
    producer.produce(topic=kafka_topic, key=string_serializer(new_change['meta']['id']), value=json_serializer(
        new_change, SerializationContext(topic=kafka_topic, field=MessageField.VALUE)), callback=delivery_status_callback)
