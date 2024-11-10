import datetime
from confluent_kafka import Consumer
import joblib
import json
from sqlalchemy.orm import sessionmaker
import pandas as pd
import sys
sys.path.append("../database")
from connection import connection

# Cargar el modelo
model = joblib.load("../Model/model.pkl")

# Conectar a la base de datos
conn = connection()

# Configurar el consumidor de Confluent Kafka
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'PLAINTEXT',
    'group.id': 'happiness-consumer-group',
    'auto.offset.reset': 'latest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['happiness'])

# Preparar DataFrame para almacenar resultados
results = pd.DataFrame(columns=['happiness_score', 'gdp_per_capita', 'social_support',
                                'health_life_expectancy', 'freedom', 'perceptions_of_corruption',
                                'generosity', 'year', 'continent_africa', 'continent_asia',
                                'continent_europe', 'continent_north_america', 'continent_oceania',
                                'continent_south_america'])

while True:
    message = consumer.poll(1.0)
    if message is None:
        continue
    if message.error():
        print(f"Consumer error: {message.error()}")
        continue

    kafka_value = json.loads(message.value().decode('utf-8'))
    new = pd.DataFrame([kafka_value], columns=['happiness_score', 'gdp_per_capita', 'social_support',
                                               'health_life_expectancy', 'freedom', 'perceptions_of_corruption',
                                               'generosity', 'year', 'continent_africa', 'continent_asia',
                                               'continent_europe', 'continent_north_america', 'continent_oceania',
                                               'continent_south_america'])
    
    df = new.copy()
    df.drop(columns=("happiness_score"), inplace=True)

    predicted = model.predict(df)[0]
    kafka_value['Predicted_Score'] = predicted
    new = pd.concat([new, pd.DataFrame([kafka_value])], ignore_index=True)

    # Cargar el DataFrame a Postgres
    Session = sessionmaker(bind=conn)
    session = Session()
    new.to_sql("happiness", con=conn, if_exists="append", index=False)

    print(f"[{datetime.datetime.now()}] - Datos cargados exitosamente en la tabla 'happiness'")
