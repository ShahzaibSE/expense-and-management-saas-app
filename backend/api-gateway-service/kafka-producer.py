from kafka import KafkaProducer

kafka_producer = KafkaProducer()

def send_log(log_data:str):
    kafka_producer.send(log_data)