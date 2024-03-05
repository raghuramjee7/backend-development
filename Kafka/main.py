import json
from kafka import KafkaProducer

folderName = "certs/"
producer = KafkaProducer(
    bootstrap_servers='raghu-kafka-raghu-dev.a.aivencloud.com:12530', # instance URI
    security_protocol="SSL", # instance protocol
    # auth files
    ssl_cafile=folderName + "ca.pem",
    ssl_certfile=folderName + "service.cert",
    ssl_keyfile=folderName + "service.key",
    # key and value serializers
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)

producer.send('test', # topic
                key={"name": 1}, 
                value={"full_name": "raghu"})

producer.flush() # flush blocks until all messages are sent