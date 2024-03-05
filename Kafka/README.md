# Kafka

1. Kafka is an event streaming platform. It is used for stream processing. It is a message stream where messages are persisted indefinitely as per deletion policy.
2. Internally, Kafka has topics. Each topic can be considered a queue. Lets say you publish a message in kafka, you publish a message for a topic in kafka and it is stored for that message
3. Each topic has partitions. We push a parition key along with the message, and the message goes to that parition of the topic. The parition key is used to make sure that the messages are ordered.
4. Ordering is guaranteed only within a partition, not across partitions.
5. Each partition has only one consumer, but a consumer can consume from multiple partitions. This is a limitation of Kafka. 
6. Consumers can commit to kafka periodically that they have consumed the message, and kafka will delete the message from the broker. This is called offset commit.
7. Kafka provides high throughput, it is easily scalable, it is fault tolerant.


## Components of Kafka
1. Message: It is the data that is being sent from one system to another.
2. Producer: It is the system that sends the message.
3. Consumer: It is the system that receives the message.
4. Topic: It is the category of the message. This is a queue where the messages are stored.
5. Broker: It is the server that stores the messages.
6. Zookeeper: It is the server that manages the brokers.
7. Cluster: It is a group of brokers.

## Setup
1. Install python-kafka package. `pip install kafka-python`
2. 

