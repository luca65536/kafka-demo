import requests
from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer


consumer_configs = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'consumer-group-1',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_configs)

kafka_topic = 'wikimedia_raw'
consumer.subscribe([kafka_topic])

schema = """
    {
        "title": "Recent Change",
        "type": "object"
    }
"""

json_deserializer = JSONDeserializer(schema_str=schema)

while True:
    message = consumer.poll(1.0)

    if message is None:
        continue

    if message.error():
        print("Error reading message: ", message.error())
        continue

    new_change = json_deserializer(data=message.value(), ctx=SerializationContext(
        topic=message.topic(), field=MessageField.VALUE))

    print("Successfully read message:", message.key())
    print(new_change)

    url = "http://localhost:9200/" + kafka_topic + \
        "/_doc/" + new_change['meta']['id']
    response = requests.put(url=url, json=new_change)

    print(response)

consumer.close()
