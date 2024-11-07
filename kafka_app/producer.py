from kafka import KafkaProducer
import pandas as pd
import json

# Leer datos limpios y enviar a Kafka
data = pd.read_csv("../data/datos_limpios.csv")

producer = KafkaProducer(bootstrap_servers="localhost:9092",
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for _, row in data.iterrows():
    message = row[['happiness_score', 'gdp_per_capita', 'social_support',
        'health_life_expectancy', 'freedom', 'perceptions_of_corruption',
       'generosity', 'year', 'continent_africa', 'continent_asia',
       'continent_europe', 'continent_north_america', 'continent_oceania',
       'continent_south_america']].to_dict()
    
    producer.send("happiness", message)

print("Mensajes enviados al tópico de Kafka.")
producer.flush()