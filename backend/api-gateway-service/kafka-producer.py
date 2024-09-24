from kafka import KafkaProducer
import json

kafka_producer = KafkaProducer(
    bootstrap_server=['broker:9092'],
    value_serializer=lambda x: json.dump(x).encode('utf-8')
)

def send_log(log_data:str):
    kafka_producer.send('log_data',log_data)
    kafka_producer.flush()