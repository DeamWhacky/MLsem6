from kafka import KafkaConsumer

# Connect to local Kafka broker
consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True
)

print("Listening to Kafka topic 'test-topic'...")

for msg in consumer:
    print(msg.value.decode("utf-8"))
