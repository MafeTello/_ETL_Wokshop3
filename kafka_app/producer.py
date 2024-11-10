from confluent_kafka import Producer
import pandas as pd
import json
import time

# Leer datos limpios y enviar a Kafka
data = pd.read_csv("../data/datos_limpios.csv")

# Configuración del productor de Confluent Kafka
producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'PLAINTEXT'
}
producer = Producer(producer_conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Mensaje fallido: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")
print("enviando datos")



for _, row in data.iterrows():
    message = row[['happiness_score', 'gdp_per_capita', 'social_support',
                   'health_life_expectancy', 'freedom', 'perceptions_of_corruption',
                   'generosity', 'year', 'continent_africa', 'continent_asia',
                   'continent_europe', 'continent_north_america', 'continent_oceania',
                   'continent_south_america']].to_dict()

    producer.produce("happiness", value=json.dumps(message), callback=delivery_report)
    print("Mensaje enviado al tópic happiness", message)
    time.sleep(1)

producer.flush()
print("Mensajes enviados al tópico de Kafka.")
